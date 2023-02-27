import re
from distutils.core import setup


kwds = {}
try:
    kwds['long_description'] = open('README.rst').read()
except IOError:
    pass


setup(
    name = "ilan-dev",
    author = "Ilan Schnell",
    author_email = "ilanschnell@gmail.com",
    license = "BSD",
    classifiers = [
        "License :: OSI Approved :: Python Software Foundation License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    description = "a few personal tools I use for development",
    py_modules = ["perfect_hash"],
    scripts = ['cleanup'],
    **kwds
)
