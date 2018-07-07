#!/usr/bin/env python
# encoding:utf-8

import sys
filename = sys.argv[1]
source = open(filename, 'r').read() + '\n'
try:
    compile(source, filename, 'exec')
except Exception as e:
    print 'ddd'
    print e