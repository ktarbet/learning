# Karl Tarbet and Andy Gaines  
# June 2019

# Script to inport irregular interval time series data
# in CSV file with the following format:

#Date,"Discharge, cfs"
#1/3/1973,938000.00
#1/5/1973,888000.00
#2/2/1973,842000.00
#2/8/1973,881000.00
#2/12/1973,839000.00


from hec.script import *
from hec.heclib.dss import *
from hec.heclib.util import *
from hec.io import *
import java

import csv

################# Input
input_csv= "c:\py\TarbertOBSQ_MeasurementsQ.csv"
input_dss= "C:/py/testimport2.dss"
path = "/BASIN/tarbertOBSQ-FLOW/tarbert//IR-YEAR/OBSQ/"
time_start="0800"
unit_data="ft"
type_data="INST-VAL"
dss_version = 6
date_column = 1   # which column has the date
value_column = 2    # which column has the flow/elevation, etc...

########## END of INPUT ######################################################

Heclib.zset("DSSV", "", dss_version)
myDss = HecDss.open(input_dss)
times = [] 
values = []
with open(input_csv) as f:
	reader = csv.reader(f)
	next(reader) # skip first row
	for row in reader:
	   	t = HecTime(row[date_column-1], time_start)
		times.append(t.value())
		d = float(row[value_column-1])
		values.append(d)
		print t, d


tsc = TimeSeriesContainer()
tsc.fullName = path
tsc.startTime =  times[0];
tsc.times = times
tsc.values = values
tsc.numberValues = len(values)
print tsc.numberValues
tsc.units = unit_data
tsc.type = type_data
myDss.put(tsc)
		

		
