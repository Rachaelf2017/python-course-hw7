import sys
import csv

extension = ".jso"


if extension == '.csv' or extension =='.txt' :
	print "CVS"
elif extension == '.json' :
	print "JSON"
else: raise Exception('Reader not found for file type %s' % extension)

print "stop"
