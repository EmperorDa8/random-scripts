#! /usr/bin/env python
import requests
import argparse
import os


par= argparse.ArgumentParser()
par.add_argument("prompt", help="to send prompt input to open-ai api")
par.add_argument("filename", help="to send prompt input to open-ai api")
argu= par.parse_args()

api_ep= "https://api.openai.com/v1/completions"
api_key= os.getenv("Open_ai_key")


req_headers={

     "Content-Type": "application/json",
     "Authorization": "Bearer " + api_key
}


req_data={

   "model": "text-davinci-003",
    
   "prompt": f"write python scripts {argu.prompt}",

    "max_tokens": 500,
    
    "temperature": 0.5
}

rr=requests.post(api_ep, headers=req_headers, json=req_data)

if rr.status_code == 200:
    req_text= rr.json()["choices"][0]["text"]
    with open(argu.filename, "w") as fil:
        fil.write(req_text)
else:
    print(f"the request failed with status_code : {str(rr.status_code)}")
