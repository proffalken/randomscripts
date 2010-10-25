#!/usr/bin/env python


# import the libraries
from pyfacter import pyfacter

# initalise pyfacter
init_fact = pyfacter()

#get the facts in a HASH
fact_hash = init_fact.get_facts()

# print a given fact to the screen
print fact_hash['lsbdistdescription']
