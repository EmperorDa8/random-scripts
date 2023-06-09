import threading
import requests
import json
from bs4 import BeautifulSoup
import os

def get_src(url, data):
    try:
        rs = requests.get(url)
        ss = BeautifulSoup(rs.text, "html.parser")
        images = ss.find_all("img")

        for i in images:
            src = i["src"]
            data["images"].append(src)
    except Exception as e:
        print(f"Error downloading image: {e}")
        
def page_links(url, data):
    try:
        rs = requests.get(url)
        ss = BeautifulSoup(rs.text, "html.parser")
        links = ss.find_all("a")

        for i in links:
            data["links"].append(i["href"])
    except Exception as e:
        print(f"Error retrieving page links: {e}")
        
def main():
    links = "https://www3.hilton.com/en/hotels/nigeria/transcorp-hilton-abuja-ABUHITW/about/amenities.html"

    data = {"images": [], "links": []}
    
    t1 = threading.Thread(target=get_src, args=(links, data))
    t2 = threading.Thread(target=page_links, args=(links, data))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    with open("data.json", "w") as f:
        json.dump(data, f)

    print("totally done!")

if __name__ == "__main__":
    main()
