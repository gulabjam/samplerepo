import requests,json, http

response = http.get ("https://httpbin.org/get?email=23f3002677@ds.study.iitm.ac.in")
ans = response.json()
print (json.dumps(ans))
