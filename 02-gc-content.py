#!/usr/bin/env python

#Lazy GC-calculator, no fancy things

query = str(input()) # save the input as string
query = query.lower() # make the string case insensitive
gc = ((query.count('g') / len(query)) + query.count('c') / len(query)) * 100 # calculation
print('Looks like your GC content is about ' + str(int(gc)) + '%, sir.') # output
