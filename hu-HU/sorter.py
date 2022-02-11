#!/usr/bin/python

# This program re-sorts a propery file (inputFile) based on a different property file (sorterFile)'s keys,
# and dumps that into a third file (outFile).
# The process is inefficient but seems to work.
# The remaining (non-matching) rows are dumped at the end of outFile.

import re

sorterFile = open('Bundle_hu.properties.old', 'r', encoding="iso-8859-2")
sorterLines = sorterFile.readlines()
sorterFile.close()

inputFile = open('Bundle_hu.properties.merged', 'r')
inputLines = inputFile.readlines()
inputFile.close()

outLines = []

for ls in sorterLines:
	key=re.sub("^([a-zA-Z0-9_.-]*)=.*\n",r"\1",ls)
	if re.match('[a-z]',key): key+="="
	#print("'"+key+"'")
	foundLines=[]
	for lm in inputLines:
		if lm.startswith(key):
			foundLines.append(lm)
			if "=" not in key: break
	#if len(foundLines)>0: print(foundLines)
	for fl in foundLines:
		outLines.append(fl)
		inputLines.remove(fl)
	#print(outLines)

outLines.append('')
outLines.append('## LINES WITH NO MATCH')
outLines.append('')
outLines.extend(inputLines)

# writing to file
outFile = open('Bundle_hu.properties.merged.sorted', 'w')
outFile.writelines(outLines)
outFile.close()
