import requests
import pprint
import pytest


url = "https://httpbin.org/"

r = requests.get(url + "get")

print(f"Call Status Code: {r.status_code}")
# print(f"Call Status Code: {r.status_code}")

def test_response():
    # url = "https://httpbin.org/"
    # r = requests.get(url + "get")
    assert r.status_code == 200