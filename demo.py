import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTg3NjZjYjAtZWI5OS0xMWViLWI0Y2MtOTlkZGIzYTIxM2E1",
  "text": "Hi vom API"
})
headers = {
  'Authorization': 'Bearer N2ZkZGM5MmMtYzExOS00OWY2LTliMDUtZDBlNDZkMWMyMTA4NDdjMmUzNDUtMDk5_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
