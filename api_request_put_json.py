import requests
import json
import jsonpath

url="https://reqres.in/api/users/2"
#read the file with file handling module
with open ("C:\\Users\\USER\\post user api.json","r")as fil:
    jsonfil=fil.read()
    json_req=json.loads(jsonfil)
    
# make put requests json object
res=requests.put(url,json_req)

#validate post response code, if ans is blank , successful
assert res.status_code==200

#fetch header from requests or to find specific header content use ,get
#print(res.headers.get("Date"))
#print(res.headers)
new_json=json.loads(res.text)
sub=jsonpath.jsonpath(new_json,'name')
print(sub[0])