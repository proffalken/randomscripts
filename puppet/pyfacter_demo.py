#!/usr/bin/env python
from pyfacter import pyfacter

init_fact = pyfacter()

fact_hash = init_fact.get_facts()

print fact_hash['lsbdistdescription']
