import requests

API_KEY = "H3rYTGX5DBJb9oqzTkDIPtd6HdMwH8l0O0xHKyU2"

def fetch_data(name):
    url = f"https://api.api-ninjas.com/v1/animals?x-api-key={API_KEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    return data

