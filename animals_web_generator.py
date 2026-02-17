import json

def load_data(file_path):
    """Loads JSON File"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


def get_animals_information(data):
    """Loops through the data and shows picked informations about the animals.
    If information is missing, we skip the missing part"""
    for animal in data:
        try:
            print(f"Name: {animal["name"]}")
            print(f"Diet: {animal["characteristics"]["diet"]}")
            print(f"Location: {animal["locations"][0]}")
            print(f"Type: {animal["characteristics"]["type"]}")
            print()
        except KeyError:
            print()
            continue

get_animals_information(animals_data)