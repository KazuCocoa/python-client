#!/usr/bin/env python

# PyPi expects a reStructuredText (http://docutils.sourceforge.net/rst.html)
# document for its readme. This takes the Github one and makes the requisite
# file. Run when README.md is changed and those changes should be reflected
# on PyPi.

import pypandoc
import os

rst_formatted_output = pypandoc.convert_file('README.md', 'rst')

with open('README.txt', 'w+') as readme:
    readme.write(rst_formatted_output)
