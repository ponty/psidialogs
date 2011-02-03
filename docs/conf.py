# -*- coding: utf-8 -*-

import os

from pkg_resources import parse_version
import pkginfo

def _egg_info(path_to_egg='../'):
    path_to_egg = os.path.join(
        os.path.dirname(__file__), path_to_egg)
    egg_info = pkginfo.Develop(path_to_egg)
    release = egg_info.version
    parsed_version = parse_version(release)
    version = '%s.%s' % tuple([int(x) for x in parsed_version[0:2]])
    return egg_info.name, egg_info.author, version, release

project, author, version, release = _egg_info()
copyright = '2011, ponty'

import sphinx
import sys
from path import path

#sys.path.append(path(__name__).abspath())
proot=(path(__file__).dirname().dirname() ).abspath()
#proot=(path('..')).abspath()
sys.path.append(proot)
import pcdialogs
#version = abandi.__version__
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Extension
extensions = [
     # -*-Extensions: -*-
     'sphinx.ext.autodoc',
     'sphinxcontrib.programoutput',
     'sphinxcontrib.programscreenshot',
     'sphinx.ext.graphviz',
     'sphinx.ext.autosummary',
    ]
intersphinx_mapping = {'http://docs.python.org/': None}

# Source
master_doc = 'index'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_trees = []
pygments_style = 'sphinx'

# html build settings
html_theme = 'default'
html_static_path = ['_static']

# htmlhelp settings
htmlhelp_basename = '%sdoc' % project

# latex build settings
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
    author, 'manual'),
]
