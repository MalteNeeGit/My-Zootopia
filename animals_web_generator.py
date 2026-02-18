import json


def load_data(file_path):
    """Loads JSON File"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

#Get the JSON Information about the animals
animals_data = load_data("animals_data.json")


def read_html(html_page):
    """Reads the template"""
    with open(html_page, "r") as website:
        return website.read()

#Read the file and save the Template
html = read_html("animals_template.html")


def get_animals_information(data):
    """Loops through the data and shows picked Informations about the animals.
    If information is missing, we skip the missing part"""
    output = ""
    for animal in data:
        #Open new list element for every animal
        output += '<li class="cards__item">'

        #Title with the name
        output += '<div class="card__title">'
        output += f"{animal['name']}<br/>\n"
        output += '</div>'

        #Text-element for the datails
        output += '<p class="card__text">'

        #Check for Diet
        try:
            if animal['characteristics']['diet']:
                output += '<strong>Diet:</strong> '
                output += f"{animal['characteristics']['diet']}<br/>\n"
        except KeyError:
            pass

        #Check for Location
        try:
            if animal['locations'][0]:
                output += '<strong>Location:</strong> '
                output += f"{animal['locations'][0]}<br/>\n"
        except (KeyError, IndexError):
            pass

        #Check for Type
        try:
            if animal['characteristics']['type']:
                output += '<strong>Type:</strong> '
                output += f"{animal['characteristics']['type']}<br/>\n"
        except KeyError:
            pass

        #Close Text and List element
        output += '</p>'
        output += '</li>'

    return output

#Get the Information we need as a string:
data_of_all_animals = get_animals_information(animals_data)

#Replace the new Information in the template:
new_html = html.replace("__REPLACE_ANIMALS_INFO__", data_of_all_animals)


def write_new_html(file_name, content):
    """Writes a new html-file with the information we got in our Python Project"""
    with open(file_name, "w", encoding="utf-8") as html_website:
        html_website.write(content)

#Create a new html file. We need to give the new name and the adapted Template
write_new_html("animals.html", new_html)