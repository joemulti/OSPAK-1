import requests

url = "https://webexapis.com/v1/people/me"

payload={}
headers = {
  'Authorization': 'Bearer NmI5M2U1MWItZmFhOS00ZGIxLTg4MWQtN2QyNWNiMzRiNGUzMTVhYWIxN2MtOThm_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)