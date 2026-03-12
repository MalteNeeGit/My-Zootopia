import data_fetcher


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
    diet = animal_obj.get('characteristics', {}).get('diet')
    if diet:
        output += '<strong>Diet:</strong> '
        output += f"{diet}<br/>\n"

    #Check location
    location = animal_obj.get('locations')
    if location:
        output += '<strong>Location:</strong> '
        output += f"{location[0]}<br/>\n"

    #Check type
    type_info = animal_obj.get('characteristics', {}).get('type')
    if type_info:
        output += '<strong>Type:</strong> '
        output += f"{type_info}<br/>\n"

    #Close text and list element
    output += '</p>'
    output += '</li>'

    return output


def get_animals_information(data):
    """Loops through the data and serializes all animals"""
    output = ""
    if not data:
        return ("<h2>😶‍🌫 This animal does not exist 😶‍🌫️</h2>"
                "<p>At least in our Database </p>")

    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def write_new_html(file_name, content):
    """Writes a new html-file with the information we got in our Python Project"""
    with open(file_name, "w", encoding="utf-8") as html_website:
        html_website.write(content)


def main():
    #animals_data = data_fetcher.load_data("animals_data.json") #old method for fetching straight from the json file
    animal_name = input("Give me an animal name: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    html = read_html("animals_template.html")
    data_of_all_animals = get_animals_information(animals_data)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", data_of_all_animals)
    write_new_html("animals.html", new_html)


if __name__ == "__main__":
    main()