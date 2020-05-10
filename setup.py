from setuptools import setup
import os.path
import sys


from setuptools import setup


NAME = "psidialogs"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

URL = "https://github.com/ponty/psidialogs"
DESCRIPTION = "python simple dialogs"
LONG_DESCRIPTION = """psidialogs (Python Simple Dialogs) is a common API
+for different standard dialogs like message, ask_string.

Documentation: https://github.com/ponty/psidialogs/tree/"""
LONG_DESCRIPTION += VERSION
PACKAGES = [
    "psidialogs",
    "psidialogs.plugins",
    "psidialogs.api",
    "psidialogs.examples",
]


# extra = {}
# if sys.version_info >= (3,):
#     extra["use_2to3"] = True
#     extra["use_2to3_exclude_fixers"] = ["lib2to3.fixes.fix_import"]

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

install_requires = ["path.py", "argparse", "EasyProcess", "entrypoint2"]

# compatible with distutils of python 2.3+ or later
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=classifiers,
    keywords="GUI common dialog",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    install_requires=install_requires,
)
