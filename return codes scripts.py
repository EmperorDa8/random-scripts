#!/usr/bin/env python3

import os, sys

filename=sys.argv[0]

if not os.path.exists(filename):
    with open("lock","w") as lok:
        lok.write("this is very fun\n")
        
else:
    print("error!, {} already exist".format(filename))
    sys.exit(1)
    
