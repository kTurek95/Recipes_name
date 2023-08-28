# Recipe Finder

Recipe Finder is a simple command-line tool that helps you find recipes based on the ingredients you have available.

## Features

- Takes input from the user for available ingredients.
- Connects to an external API to find recipes that match the provided ingredients.
- Saves the list of ingredients to a CSV file.
- Saves the names of matching recipes to a text file.

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required dependencies using the following command:

    ```sh
    pip install requests
    ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the Recipe Finder:

    ```sh
    python main.py
    ```

4. Follow the prompts to provide your ingredients. Enter "end" to finish.
5. The program will display a list of recipes you can prepare based on the provided ingredients.

## Tests

To run tests for the Recipe Finder functions:

1. Ensure you are in the project directory.
2. Run the following command:

    ```sh
    pytest test_function_recipes.py
    ```

## Contributing

Contributions are welcome! If you find a bug or want to improve the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Recipe data is provided by the Spoonacular API.
- The project structure and some test cases were inspired by online tutorials and resources.
