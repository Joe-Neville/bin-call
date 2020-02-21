import requests
import pprint
import pytest


url = "https://httpbinx.org/"

r = requests.get(url + "get")
print(f"Call Status Code: {r.status_code}")


def test_response():
    assert r.status_code == 200