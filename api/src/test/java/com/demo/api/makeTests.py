#!/usr/bin/python

import re

# read in example file
fname = 'TestExample1.java'
with open(fname, 'r+') as f:
    text = f.read()
    f.truncate()
    f.close()
    

# iterate through for the number of times specified

for x in range(3, 61):
    newtext = re.sub('1', str(x), text)
    newfname = 'TestExample'+str(x)+'.java'
    with open(newfname, 'w+') as nf:
	nf.write(newtext)
	nf.truncate()
	nf.close()
		
