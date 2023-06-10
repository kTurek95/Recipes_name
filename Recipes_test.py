from function_recipes import save_recipes_name_to_file, get_ingredients_from_user_and_save_in_file
import os


def test_save_recipes_name_to_file():
    meals = []

    save_recipes_name_to_file(meals)
    assert os.path.isfile('recipes name.txt') is True


def test_get_ingredients_from_user_and_save_in_file():
    ingredients = ['chicken', 'tomato', 'mozzarella']

    get_ingredients_from_user_and_save_in_file(ingredients)
    assert os.path.isfile('ingredients.csv') is True

    with open('ingredients.csv', 'r') as file:
        lines = file.readlines()

    expected_lines = [
        "ingredient;quantity\n",
        "chicken;1\n",
        "tomato;1\n",
        "mozzarella;1\n"
    ]
    assert len(lines) == len(expected_lines)

    for line in lines[1:]:
        ingredient, quantity = line.strip().split(";")
        assert ingredient in ingredients
        assert quantity == "1"