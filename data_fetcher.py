from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY not found in .env file")

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

