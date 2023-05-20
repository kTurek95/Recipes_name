import csv
import requests


def get_ingredients_from_user_and_save_in_file(ingredients: list):
    """A function that takes input from the user, collects ingredients, and saves them in a CSV file"""
    columns = ['ingredient', 'quantity']

    my_dict = {}
    for item in ingredients:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    with open('ingredients.csv', mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=';')
        writer.writeheader()

        for ingredient, quantity in my_dict.items():
            writer.writerow({'ingredient': ingredient, 'quantity': quantity})


def save_recipes_name_to_file(meals: str):
    """A function that opens a text file and writes meal names in it"""
    with open('recipes name.txt', mode='w') as file:
        for meal in meals:
            file.write(meal)
            file.write('\n')


def get_recipes(ingredients: list):
    """A function that connects to an API, checks if there are any recipes in the database that match the ingredients"""
    # Create the API request parameters required in Spoonacular
    params = {
        'ingredients': ','.join(ingredients),
        'apiKey': '1595cfa2565c4fb896f029738d1d3dc7',
        'number': 20
    }

    # Send an API request and retrieve the response
    response = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=params)

    # Check if the request was successful.
    if response.status_code == 200:
        meals = []
        results = response.json()
        for row in results:
            if row['missedIngredientCount'] < 3:  # We can have a maximum of 2 missing ingredients
                meals.append(row['title'])
        # Check if any recipes were found
        if len(meals) > 1:
            print('You can prepare: ')
            for meal in meals:
                print(meal)
        else:
            print("We're sorry, but we don't have any recipes that match your criteria")

        return meals
