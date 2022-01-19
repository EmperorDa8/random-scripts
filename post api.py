import requests,json
import jsonpath

url="https://reqres.in/api/users"
#read the file with file handling module
with open ("C:\\Users\\USER\\post user api.json","r")as fil:
    jsonfil=fil.read()
    json_req=json.loads(jsonfil)
    
# make post requests json object
res=requests.post(url,json_req)
print(res.content)

#validate post response code, if ans is blank , successful
assert res.status_code==201

#fetch header from requests or to find specific header content use ,get
#print(res.headers.get("Date"))
#print(res.headers)

# parse response into json format
res_json=json.loads(res.text)

# getting id using jsonpath
new=jsonpath.jsonpath(res_json,"id")
print(new[0])