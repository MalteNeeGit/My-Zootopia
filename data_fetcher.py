import requests
import json

API_KEY = "H3rYTGX5DBJb9oqzTkDIPtd6HdMwH8l0O0xHKyU2"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = f"https://api.api-ninjas.com/v1/animals?x-api-key={API_KEY}&name={animal_name}"
    res = requests.get(url)
    data = res.json()
    return data

#old method for the zootopia tasK

def load_data(file_path):
    """Loads JSON File"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)
