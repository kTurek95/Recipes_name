""" Main module """
from recipes import get_ingredients_from_user_and_save_in_file, get_recipes, save_recipes_name_to_file


def main():
    """
    Main function that takes ingredients from the user, until they write 'end',
    calling the remaining functions
    contained within the program.
    """
    ingredients = []
    while True:
        user_ingredients = \
            input('Please provide the ingredients you have (or type "end" to finish): ')
        if user_ingredients.lower() == 'end':
            break

        ingredients.append(user_ingredients)

    get_ingredients_from_user_and_save_in_file(ingredients)
    get_recipes(ingredients)
    save_recipes_name_to_file(get_recipes(ingredients))


if __name__ == '__main__':
    main()
