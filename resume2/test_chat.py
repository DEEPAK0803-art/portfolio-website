import requests
import json

def test_chat():
    url = "http://127.0.0.1:5000/chat"
    payload = {"message": "What is Deepak's current CGPA?"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_chat()
