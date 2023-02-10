#!/usr/bin/env python3

import csv
import sys
import os

#file=sys.argv[1]
file_path="Downloads/economic-survey-of-manufacturing-june-2022-csv.csv"
new=os.path.abspath(file_path)
with open(new) as fil:
    csv_file=csv.reader(fil)
    for item in csv_file:
        print (item)
       # ref,date,figure,currency,indusry,food,department,price,other=item
       # print (f"the ref{ref}, figure:{figure}, currency:{currency},industry:{industry},food:{food},dep:{department},price:{price},other:{other}")
#print("completed")
