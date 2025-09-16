import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={
  'scope': 'SALUTE_SPEECH_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '9995ee0a-981c-41e1-8a99-efd7cad58cdd',
  'Authorization': 'Basic <Authorization key>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)