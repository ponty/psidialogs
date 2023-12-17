"""
This method moves the mouse over a grid, and compare
the image with the original and finds active regions.

.. note::
     It does not work if the GUI changes during the scan.
     (e.g. blinking cursor)

It can be slow if grid is small or the window is large.

"""

import logging
from time import sleep

from discogui.imglog import img_log, img_log_rects
from discogui.imgutil import focus_wnd, getbbox, grab
from discogui.mouse import PyMouse
from PIL import ImageChops

log = logging.getLogger(__name__)


def is_point_active(img_orig, point, mouse=None):
    """
    Check point on screen:
    1. move mouse over specified point
    2. move mouse to (0,0)

    If screen changes, then returns the bounding rectangle.

    Does not work if other parts of screen are changing (e.g. blinking cursor)

    :rtype: rectangle or None
    """

    if not mouse:
        mouse = PyMouse()

    log.debug("point:" + str(point))

    mouse.move(point[0], point[1])
    # this should be enough time for any change, (gmessage: 0.1 is too low)
    # but not too much because of tooltips. (gtk ~500ms)
    # Disabling tooltip can help.

    sleep(0.5)
    img_hover = grab()
    mouse.move(0, 0)

    # img_log(img_hover, 'img_hover')
    img_log_rects(img_hover, [point + point], "img_hover")

    img_diff = ImageChops.difference(img_orig, img_hover)
    # enhance color for debug
    img_diff = img_diff.point(lambda x: 255 * bool(x))
    img_log(img_diff, "img_diff")

    bbox = getbbox(img_diff)
    if bbox:
        # assert bbox.point_inside(point), (bbox, point)
        if not bbox.point_inside(point):
            log.debug("point%s outside box%s" % (point, bbox))
        return bbox


def active_rectangles(grid=30):
    """
    Return active rectangles found on the specified grid.
    Does not work if other parts of screen are changing (e.g. blinking cursor)

    :rtype: rectangles list
    """
    mouse = PyMouse()

    img_orig = focus_wnd()
    rct_wnd = getbbox(img_orig)

    ls = []
    for y in range(
        int(rct_wnd.top + grid / 2), int(rct_wnd.bottom), int(grid - grid / 2)
    ):
        for x in range(
            int(rct_wnd.left + grid / 2), int(rct_wnd.right - grid / 2), grid
        ):
            bbox = is_point_active(img_orig, (x, y), mouse=mouse)
            if bbox and bbox not in ls:
                ls.append(bbox)

    img_log_rects(img_orig, ls, "img_orig")
    return ls
