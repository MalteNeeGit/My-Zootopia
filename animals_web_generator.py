import json


def load_data(file_path):
    """Loads JSON File"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_html(html_page):
    """Reads the template"""
    with open(html_page, "r", encoding="utf-8") as website:
        return website.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object to HTML"""
    output = ""

    #Open new list element for animal
    output += '<li class="cards__item">'

    #Title for the name
    output += '<div class="card__title">'
    output += f"{animal_obj['name']}<br/>\n"
    output += '</div>'

    #Text element for the bbody
    output += '<p class="card__text">'

    #Check diet
    try:
        if animal_obj['characteristics']['diet']:
            output += '<strong>Diet:</strong> '
            output += f"{animal_obj['characteristics']['diet']}<br/>\n"
    except KeyError:
        pass

    #Check location
    try:
        if animal_obj['locations'][0]:
            output += '<strong>Location:</strong> '
            output += f"{animal_obj['locations'][0]}<br/>\n"
    except (KeyError, IndexError):
        pass

    #Check type
    try:
        if animal_obj['characteristics']['type']:
            output += '<strong>Type:</strong> '
            output += f"{animal_obj['characteristics']['type']}<br/>\n"
    except KeyError:
        pass

    #Close text and list element
    output += '</p>'
    output += '</li>'

    return output


def get_animals_information(data):
    """Loops through the data and serializes all animals"""
    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def write_new_html(file_name, content):
    """Writes a new html-file with the information we got in our Python Project"""
    with open(file_name, "w", encoding="utf-8") as html_website:
        html_website.write(content)


def main():
    animals_data = load_data("animals_data.json")
    html = read_html("animals_template.html")
    data_of_all_animals = get_animals_information(animals_data)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", data_of_all_animals)
    write_new_html("animals.html", new_html)


if __name__ == "__main__":
    main()