import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vZDEyMDcxYTAtMGM4OS0xMWVjLWFjYTktODlhNDA2MzVmMDhh",
  "text": "hUHU AUS Python"
})
headers = {
  'Authorization': 'Bearer NWNjODc0YzctYmJkYi00ZmM5LThjOWItNTY0Y2Q5NDVhODNjNDQ0NmE2NTYtYjYz_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
