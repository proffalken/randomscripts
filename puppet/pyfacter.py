#!/usr/bin/env python
import os
import yaml

class pyfacter:
	def __init__(self):
		exec_string = "facter --puppet --yaml"
		cmd = os.popen(exec_string)
		self.fact_dict = yaml.load(cmd)
	def get_facts(self):
		return self.fact_dict
	



