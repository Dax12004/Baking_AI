from flask import Flask, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

# Load the CSV file
df_recipes = pd.read_csv('recipes.csv')

# Function to extract density measurements
def extract_density_measurements(ingredients_str):
    if isinstance(ingredients_str, str):
        cups = re.findall(r'(\d+\s*(?:\d+/\d+)?)\s*cup(?:s)?', ingredients_str)
        tablespoons = re.findall(r'(\d+\s*(?:\d+/\d+)?)\s*tablespoon(?:s)?', ingredients_str)
        spoons = re.findall(r'(\d+\s*(?:\d+/\d+)?)\s*spoon(?:s)?', ingredients_str)
        return cups, tablespoons, spoons
    return [], [], []

df_recipes['cups'], df_recipes['tablespoons'], df_recipes['spoons'] = zip(*df_recipes['ingredients'].apply(extract_density_measurements))

# Function to calculate averages
def calculate_average_measurement(measurement_list):
    if not measurement_list:
        return 0
    try:
        numeric_measurements = [float(re.sub(r'[^\d.]', '', measurement)) for measurement in measurement_list]
        return sum(numeric_measurements) / len(numeric_measurements)
    except ValueError:
        return 0

df_recipes['avg_cups'] = df_recipes['cups'].apply(calculate_average_measurement)
df_recipes['avg_tablespoons'] = df_recipes['tablespoons'].apply(calculate_average_measurement)
df_recipes['avg_spoons'] = df_recipes['spoons'].apply(calculate_average_measurement)

# Function to convert to grams
def convert_to_grams(row):
    return (row['avg_cups'] * 120) + (row['avg_tablespoons'] * 15) + (row['avg_spoons'] * 5)

df_recipes['total_grams'] = df_recipes.apply(convert_to_grams, axis=1)

@app.route('/get_recipe', methods=['GET'])
def get_recipe():
    recipe_name = request.args.get('name')
    recipe_data = df_recipes[df_recipes['recipe_name'].str.contains(recipe_name, case=False, na=False)]
    if recipe_data.empty:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(recipe_data[['recipe_name', 'ingredients', 'total_grams']].to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
