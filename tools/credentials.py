#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jlmarks
# @Date:   2015-05-26 01:15:37
# @Last Modified 2015-05-26
# @Last Modified time: 2015-05-26 01:21:39

import random
import string

def getRandomID(size=8, chars=string.ascii_uppercase + string.digits):
    # This is a slight mod of this thread on SO: http://stackoverflow.com/a/2257449
    global uniques
    if 'uniques' not in globals():
        uniques = set()
    while True:
        potentialID=''.join(random.choice(chars) for _ in range(size))
        if potentialID not in uniques:
            uniques.add(potentialID)
            break
    return potentialID