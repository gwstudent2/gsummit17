#!/usr/bin/python

import re

from random import randrange


# read in example file
fname = 'TestExample1.java'
with open(fname, 'r+') as f:
    text = f.read()
    f.truncate()
    f.close()
    

# iterate through for the number of times specified

for x in range(2, 29):
    irand = randrange(0, 5) * 1000
    text1 = re.sub('1', str(x), text)
    newfname = 'TestExample'+str(x)+'.java'
    text2 = re.sub('2000', str(irand), text1)
    with open(newfname, 'w+') as nf:
	nf.write(text2)
	nf.truncate()
	nf.close()
		
