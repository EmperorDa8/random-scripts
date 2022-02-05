import json
import requests

api_url="https://61fd9aeaa58a4e00173c95fc.mockapi.io/employees"

contain=requests.get(api_url)
datas=json.loads(contain.text)
details=[]
for item in datas:
    name=item["name"]
    avatar=item["avatar"]
    ids=item["id"]
    de=f"id: {ids} the name {name} with avatar: {avatar}"
    details.append(de)
    newdetails="\n".join(details)
    with open("testmock.csv", "w") as fil:
        fil.write(str(newdetails))
print("workdone")