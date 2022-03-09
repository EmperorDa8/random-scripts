import requests
import pprint


baseurl="https://61fd9aeaa58a4e00173c95fc.mockapi.io/"
end_point="movies"
full_url=baseurl+end_point
listitem=[]
def main():
    content=requests.get(full_url)
    data=content.json()
    return data


def perform():
    total={}
    response=main()
    for item in response: 
        name=item["name"]
        Id=item["id"]
        total[name]=Id
    listitem.append(total)
    cont=pprint.pprint(listitem)

    with open("item-content.json","w")as fil:
        fil.write(str(listitem))
    print("process done")
        
perform()