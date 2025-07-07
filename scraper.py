import requests
import json

url = "https://remoteok.com/api"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()


    for job in data[1:]:
        print(f"{job['position']} — {job['company']}")
        print("Link:", job['url'])
        print("-" * 40)
else:
    print("Failed to fetch data. Status code:", response.status_code)
