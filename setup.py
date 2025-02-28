"""
CMLibs Widgets

A collection of Qt widgets and utilities building on the Python bindings for the Zinc Visualisation Library.
"""
import io
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'src', 'cmlibs', 'widgets', '__init__.py')) as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


readme = readfile("README.rst", split=True)
readme.append('License')
readme.append('=======')
readme.append('')
readme.append('')

software_licence = readfile("LICENSE")

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    "Programming Language :: Python",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Topic :: Scientific/Engineering :: Medical Science Apps.",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

doc_lines = __doc__.split("\n")

requires = [
    'cmlibs.maths >= 0.3',
    'cmlibs.utils >= 0.4',
    'PySide6',
    'cmlibs.zinc',
    'cmlibs.argon >= 0.4.0',
]

setup(
    name='cmlibs.widgets',
    version=version,
    author='H. Sorby',
    author_email='h.sorby@auckland.ac.nz',
    long_description='\n'.join(readme) + software_licence,
    long_description_content_type='text/x-rst',
    platforms=['any'],
    url='https://github.com/CMLibs-Python/cmlibs.widgets/',
    license='Mozilla Public License',
    license_files=("LICENSE",),
    packages=find_packages("src"),
    package_dir={"": "src"},
    description=doc_lines[0],
    classifiers=classifiers,
    install_requires=requires,
)
