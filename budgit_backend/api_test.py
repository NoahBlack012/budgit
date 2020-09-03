import requests

base = "http://127.0.0.1:5000/"
api_key = "x{lhtTaQz58QJ7ZK;a~`/t!:D"
res = requests.post(base + "api/login",
    json={"password": "123", "username": "abc", "api_key": api_key}
)
json_response = res.json()
if json_response["status_code"] == 200:
    hash = json_response["hashed"]
    print (hash)
else:
    print ("You do not have access")
