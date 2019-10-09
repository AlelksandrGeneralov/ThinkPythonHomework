#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:36:12 2019

@author: aleksandr
"""

import dbm

db = dbm.open('captons.db', 'c')

db['cleese.png'] = 'photo of John Cleese'

print(db['cleese.png'])