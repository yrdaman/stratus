# filepath: c:\Users\Rakesh\Desktop\stratus-main\server\test_api.py
import requests

BASE_URL = "http://localhost:5000"

def signup(username, password):
    response = requests.post(
        f"{BASE_URL}/signup",
        json={"username": username, "password": password}
    )
    print("Signup:", response.json())

def login(username, password):
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": password}
    )
    print("Login:", response.json())

if __name__ == "__main__":
    signup("testuser", "testpass")
    login("testuser", "testpass")