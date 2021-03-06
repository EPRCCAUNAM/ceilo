# -*- coding: utf-8 -*-
"""
Plotting example 1
========================

The gallery is capable of transforming Python files into reStructuredText files
with a notebook structure. For this to be used you need to respect some syntax
rules.

It makes a lot of sense to contrast this output rst file with the
:download:`original Python script <plot_notebook.py>` to get better feeling of
the necessary file structure.

Anything before the Python script docstring is ignored by sphinx-gallery and
will not appear in the rst file, nor will it be executed.
This Python docstring requires an reStructuredText title to name the file and
correctly build the reference links.

Once you close the docstring you would be writing Python code. This code gets
executed by sphinx gallery shows the plots and attaches the generating code.
Nevertheless you can break your code into blocks and give the rendered file
a notebook style. In this case you have to include a code comment breaker
a line of at least 20 hashes and then every comment start with the a new hash.

As in this example we start by first writing this module
style docstring, then for the first code block we write the example file author
and script license continued by the import modules instructions.
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from ceilotools import readmatrixfile, readmlh
matrixfile='/home/jlgf/Documents/Python/scripts/20160212_UNAM_prf.txt'
mlhfile='/home/jlgf/Documents/Python/scripts/20160212_UNAM_mlh.txt'
##############################################################################
# This code block is executed, although it produces no output. Lines starting
# with a simple hash are code comment and get treated as part of the code
# block. To include this new comment string we started the new block with a
# long line of hashes.
#
# The sphinx-gallery parser will assume everything after this splitter and that
# continues to start with a **comment hash and space** (respecting code style)
# is text that has to be rendered in
# html format. Keep in mind to always keep your comments always together by
# comment hashes. That means to break a paragraph you still need to commend
# that line break.
#
# In this example the next block of code produces some plotable data. Code is
# executed, figure is saved and then code is presented next, followed by the
# inlined figure.

z,time,allprf=readmatrixfile(matrixfile)
mlhtime,mlh=readmlh(mlhfile)
plt.figure(figsize=(12,7))
plt.contourf(time,z,allprf,cmap='Spectral',levels=np.arange(0,300,20))
plt.colorbar()
plt.xlabel('Time [h]')
plt.ylabel('Height [m]')
plt.savefig('/home/jlgf/Documents/Python/figs/20160212.png')

###########################################################################
