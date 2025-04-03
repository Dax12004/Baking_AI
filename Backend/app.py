import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import re
import numpy as np
import os

app = Flask(__name__)
CORS(app)

density_conversion = {
    'cup': 240,
    'cups': 240,
    'tbsp': 15,
    'tablespoon': 15,
    'tablespoons': 15,
    'tsp': 5,
    'teaspoon': 5,
    'teaspoons': 5
}

def convert_to_grams(value):
    converted_values = []
    matches = re.findall(r'(\d+(?:\.\d+)?)\s*(cup|cups|tbsp|tablespoon|tablespoons|tsp|teaspoon|teaspoons)', str(value).lower())
    total_grams = 0
    for amount, unit in matches:
        grams = round(float(amount) * density_conversion[unit], 2)
        total_grams += grams
        converted_values.append(f"{amount} {unit} = {grams}g")
    return {
        'converted_values': converted_values,
        'total_grams': round(total_grams, 2) if total_grams > 0 else "N/A"
    }

def clean_data(df):
    for column in ['cook_time', 'prep_time', 'total_time', 'Total Grams']:
        df[column] = df[column].apply(lambda x: "N/A" if pd.isna(x) else x)
    return df

def load_recipes():
    try:
        csv_path = r'C:\Users\dell\OneDrive\Desktop\ExtraClg_DATA\pbakingAI\recipes.csv'
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at: {csv_path}")
        
        df = pd.read_csv(csv_path, on_bad_lines='skip', encoding='utf-8')

        if 'Unnamed: 0' in df.columns:
            df.drop(['Unnamed: 0'], axis=1, inplace=True)

        df['ingredients'].fillna('', inplace=True)
        df['__normalized_name'] = df['recipe_name'].astype(str).str.strip().str.lower()
        df = df.groupby('__normalized_name', as_index=False).first()
        df.drop(columns=['__normalized_name'], inplace=True)
        df[['Converted Ingredients', 'Total Grams']] = df['ingredients'].apply(
            lambda x: pd.Series(convert_to_grams(x))
        )
        df = clean_data(df)
        if df.empty:
            raise ValueError("CSV file is empty or data format issue")
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

@app.route('/get-all-recipes', methods=['GET'])
def get_all_recipes():
    recipes = load_recipes()
    if not recipes:
        return jsonify({'error': 'No recipes found'}), 404

    search_query = request.args.get('search', '').strip().lower()
    if search_query:
        recipes = [recipe for recipe in recipes if search_query in recipe.get('recipe_name', '').lower()]
    
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 20))
    sorted_recipes = sorted(recipes, key=lambda x: x.get('recipe_name', '').lower())
    
    start = (page - 1) * limit
    end = start + limit
    
    formatted_data = [
        {
            'Recipe Name': recipe.get('recipe_name', 'N/A'),
            'Image': recipe.get('img_src', 'N/A'),
            'Cook Time': recipe.get('cook_time', 'N/A'),
            'Prep Time': recipe.get('prep_time', 'N/A'),
            'Ingredients': recipe.get('ingredients', 'N/A'),
            'Converted Ingredients': recipe.get('Converted Ingredients', []),
            'Total Grams': recipe.get('Total Grams', 'N/A'),
            'Directions': recipe.get('directions', 'N/A')
        } for recipe in sorted_recipes[start:end]
    ]
    total_pages = (len(recipes) + limit - 1) // limit
    return jsonify({
        'recipes': formatted_data,
        'total_pages': total_pages,
        'current_page': page,
        'total_recipes': len(recipes)
    })

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Baking AI - Recipes API with Search Functionality!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
