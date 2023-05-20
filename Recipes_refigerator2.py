import function_recpies

ingredients = []

while True:
    user_ingredients = input('Please provide the ingredients you have (or type "end" to finish): ')
    if user_ingredients.lower() == 'end':
        break
    else:
        ingredients.append(user_ingredients)


function_recpies.get_ingredients_from_user_and_save_in_file(ingredients)
function_recpies.get_recipes(ingredients)
function_recpies.save_recipes_name_to_file(function_recpies.get_recipes(ingredients))
