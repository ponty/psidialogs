from setuptools import setup
import os.path
import sys

if os.environ.get('distutils_issue8876_workaround_enabled', False):
    # sdist_hack: Remove reference to os.link to disable using hardlinks when
    #             building setup.py's sdist target.  This is done because
    #             VirtualBox VMs shared filesystems don't support hardlinks.
    del os.link

NAME = 'psidialogs'
URL = 'https://github.com/ponty/psidialogs'
DESCRIPTION = 'python simple dialogs'
PACKAGES = ['psidialogs',
            'psidialogs.plugins',
            'psidialogs.api',
            'psidialogs.examples',
            ]

# get __version__
__version__ = None
exec(open(os.path.join(NAME, 'about.py')).read())
VERSION = __version__

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
    extra['use_2to3_exclude_fixers'] = ['lib2to3.fixes.fix_import']

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    'Programming Language :: Python :: 2',
    #    "Programming Language :: Python :: 2.3",
    #    "Programming Language :: Python :: 2.4",
    #"Programming Language :: Python :: 2.5",
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    #    "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 3",
#     'Programming Language :: Python :: 3.0',
    #     "Programming Language :: Python :: 3.1",
#     'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

install_requires = open("requirements.txt").read().split('\n')

# compatible with distutils of python 2.3+ or later
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='GUI common dialog',
    author='ponty',
    # author_email='',
    url=URL,
    license='BSD',
    packages=PACKAGES,
#     include_package_data=True,
#     test_suite='nose.collector',
#     zip_safe=False,
    install_requires=install_requires,
    **extra
)
