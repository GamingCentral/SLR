import json
import requests

policeNearest = { #import/return from the other module
    'station Man': 69,
    'station Car': 93,
    'station Naanu': 6993,
}

def sendData():
    url = "http://localhost:3000/receiver"  # Replace with Node.js API URL
    headers = {"Content-Type": "application/json"}
    data = json.dumps(policeNearest)
    response = requests.post(url, data=data, headers=headers)
    print(response.status_code, response.text)

if __name__ == "__main__":
    sendData()
