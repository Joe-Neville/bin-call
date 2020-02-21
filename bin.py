import requests
import pprint


url = "https://httpbin.org/"

r = requests.get(url + "get")
print(f"Call Status Code: {r.status_code}")
# print(f"Call Status Code: {r.status_code}")
