#!/usr/bin/env python3
import json
import io
import pandas as pd
db=pd.read_csv("file_path")
nwdb=db.to_dict(orient="indent")
with open("filename.json","w",encoding="utf-8")as fil:
    fil.write(json.dumps(nwdb,indent=1))
    fil.close()
print(fil)
    
