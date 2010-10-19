#!/usr/bin/env python

# import the relevant libraries
import sys
import hashlib

while True:
    request = sys.stdin.readline().strip()
    response = hashlib.md5(request).hexdigest()[-4:]
    if response:
        sys.stdout.write(response + '\n')
    else:
        sys.stdout.write('NULL\n')
    sys.stdout.flush()
	
