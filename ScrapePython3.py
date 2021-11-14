import requests
import string
from bs4 import BeautifulSoup

URL = "https://www.allrecipes.com/recipe/11679/homemade-mac-and-cheese/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

ingredient_parse = soup.find_all("input", class_="checkbox-list-input")
direction_parse = soup.find_all("div", class_="paragraph")

unicode_quantities = []
unicode_units = []
unicode_ingredients = []
unicode_type = []

for ingredient in ingredient_parse:
    val = ingredient.attrs
    if u'data-quantity' in val.keys():
        unicode_quantities.append(val[u'data-init-quantity'])
    if u'data-unit' in val.keys():
        unicode_units.append(val[u'data-unit'])
    if u'data-ingredient' in val.keys():
        unicode_ingredients.append(val[u'data-ingredient'])
    if u'data-ingredient' in val.keys():
        unicode_type.append(val[u'data-unit_family'])

quantities = []
units = []
ingredients = []
types = []
descriptors = []

for quantity, unit, ingredient, type in zip(unicode_quantities, unicode_units, unicode_ingredients, unicode_type):
    quantities.append(float(quantity))
    units.append(unit.encode("ascii", "ignore").translate(None, string.punctuation).strip())
    types.append(type.encode("ascii", "ignore").translate(None, string.punctuation).strip())
    ingredients.append(ingredient.encode("ascii", "ignore").translate(None, string.punctuation).strip())

directions = []

for step in direction_parse:
    step_text = step.text
    directions.append(step_text.encode("ascii", "ignore").strip())

print("Quantities: " + str(quantities) + "\n")
print("Units: " + str(units) + "\n")
print("Ingredients: " + str(ingredients) + "\n")
print("Ingredient Type: " + str(types) + "\n")

for index, step in enumerate(directions):
    print("Step #" + str(index) + ": " + str(step) + "\n")



