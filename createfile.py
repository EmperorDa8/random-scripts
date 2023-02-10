#!/usr/bin/env python3

import os
import sys


filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w")as fil:
        fil.write("file created"*10)
else:
    print(f"error file {filename} already exist")
    sys.exit(1)
