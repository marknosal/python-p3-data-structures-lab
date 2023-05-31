spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    newthing = [thing['name'] for thing in spicy_foods]
    return newthing

def get_spiciest_foods(spicy_foods):
    newthing = [thing for thing in spicy_foods if thing['heat_level'] > 5]
    return newthing

def print_spicy_foods(spicy_foods):
    [print(f"{thing['name']} ({thing['cuisine']}) | Heat Level: {'🌶' * thing['heat_level']}") for thing in spicy_foods]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for thing in spicy_foods:
        if thing['cuisine'] == cuisine:
            return thing

def print_spiciest_foods(spicy_foods):
    [print(f"{thing['name']} ({thing['cuisine']}) | Heat Level: {'🌶' * thing['heat_level']}") for thing in spicy_foods if thing['heat_level'] > 5]

def get_average_heat_level(spicy_foods):
    sum = 0
    for thing in spicy_foods:
        sum = sum + thing['heat_level']
    return sum / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
