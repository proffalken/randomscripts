#!/usr/bin/env python
# This script takes a domain name as an argument and creates the relevant site
# import the relevant libraries
import sys
import os
import hashlib

request = sys.argv[1]
md5hash = hashlib.md5(request).hexdigest()[-4:]
dirpath = '/content/'+md5hash+'/'+request+'/web'
os.makedirs(dirpath)
indexfile = dirpath+'/index.html'
index = open(indexfile,'w')
index.write('This is '+request+'. Please behave')
