#!/usr/bin/env python
import os
import yaml

if __name__ == "__main__":
	# open the output of facter with puppet facts in YAML format as a file
	cmd = os.popen("facter -p --yaml")

	# read the YAML into a dict
	fact_array = yaml.load(cmd)

	# Print out a few selected facts
	print fact_array['hostname']+" "+ fact_array['lsbdistdescription']+" "+ fact_array['swapfree']
	

