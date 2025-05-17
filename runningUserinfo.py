import http.client
import json

conn = http.client.HTTPSConnection("www.runninghub.cn")
payload = json.dumps({
   "apikey": "e28e7f2b33294b0e85e9b11f351f6dd6"
})
headers = {
   'Host': 'www.runninghub.cn',
   'Content-Type': 'application/json'
}
conn.request("POST", "/uc/openapi/accountStatus", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))