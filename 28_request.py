import requests

res = requests.get("https://jsonplaceholder.typicode.com/users/5",timeout=2)

print("Status:",res.status_code)

if res.status_code == 200:
    data = res.json()
    for key,value in data.items():
        print(f"{key} : {value}")
else:
    print("Something went wrong")