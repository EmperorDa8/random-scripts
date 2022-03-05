import requests

def get_ip():
    response=requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_url_location():
    ip_addrs=get_ip()
    response = requests.get(f'https://ipapi.co/{ip_addrs}/json/').json()
    location_data = {
        "ip": ip_addrs,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country_population": response.get("country_population"),
        "currency": response.get("currency"),
        "lat": response.get("latitude")
    }
    return location_data    

print(get_url_location())
    
    