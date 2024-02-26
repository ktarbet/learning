import requests

#https://www.webfx.com/web-development/glossary/http-status-codes/
#https://www.latlong.net/Show-Latitude-Longitude.html

url = "http://api.open-notify.org/iss-now.json"
# {'iss_position': {'latitude': '51', 'longitude': '5 '}, 'timestamp': 1708826551, 'message': 'success'}
response = requests.get(url=url)

if response.status_code == 404:
    print("Not found")
if response.status_code != 200:
    print(f"Error.... reading{url}")
print(response.status_code)
data = response.json()
print(data)
print(data['iss_position'])
long = data['iss_position']["longitude"]
lat = data['iss_position']["latitude"]
