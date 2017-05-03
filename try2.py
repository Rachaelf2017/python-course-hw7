import sys
import os.path
import csv
import glob
from pandas import DataFrame, Series
import pandas as pd

def read_all_files(path):
    extension = os.path.splitext(path)[-1]
	file_reader = reader(extension)
    frame = file_reader(path)
    return frame

def reader(extension) :
	if extension == '.csv' or extension =='.txt' :
		return csv_reader
	elif extension == '.json' :
		return json_reader
	else: raise Exception('Reader not found for file type %s' % extension)

def json_reader (path) :
	return pd.read_json(path, orient='records')

def csv_reader (path) :
	return pd.read_csv(path)


print read_all_files(sys.argv[1])
