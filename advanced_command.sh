#!/bin/bash

for logfile in C:/Users/USER/Downloads/sample.log ; do
	echo "processing file : $logfile"
	cut -d" " -f5- $logfile | sort | uniq -c | sort -nr | head  -5
done
