#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 14:55:10
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 18:19:42
import os
from CIA.tools import *
from CIA import storeroom as intel
import assistant
global project
project='messy'
clerk=assistant.fileWorker(project)

pathToMainCSV='products.csv'
fullpathToMainCSV = os.path.abspath(pathToMainCSV)

# step 0:
    # tell the clerk to copy that file to your storage area,
    # and add a column to it with the rowNumber as a value

safeCSV=clerk.moveFileToStorage(fullpathToMainCSV)
numberedRows=clerk.addNumberingColumnToCSV(safeCSV)
clerk.prepare(numberedRows)
clerk.parseCSV()


# Step 1:

    # Parse the large CSV into four smaller CSV Files, one
    # for each type of row.  Assign a new column to the files
    # namedRowNumber.
