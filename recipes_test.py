""" Module with tests for function recipes module """

import os
from recipes import save_recipes_name_to_file, get_ingredients_from_user_and_save_in_file


def test_save_recipes_name_to_file():
    """
    Test function for saving recipe names to a file.

    This function tests the functionality of saving recipe names to a file.

    Raises:
        AssertionError: If the file 'recipes name.txt' does not exist after the function call.
    """
    meals = []

    save_recipes_name_to_file(meals)
    assert os.path.isfile('recipes name.txt') is True


def test_get_ingredients_from_user_and_save_in_file():
    """
    Test function for getting user ingredients and saving them to a file.

    This function tests the functionality of getting a list of ingredients from the user
    and saving them to a CSV file named 'ingredients.csv'.
    Raises:
        AssertionError: If the file 'ingredients.csv' does not exist after the function call,
                       or if the contents of the file do not match the expected format or values.
    """
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
