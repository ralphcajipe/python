# Nutrition Facts

# Associate a fruit with its calories
calories_of_fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# Prompts user to input a fruit (case-insensitively)
# and then outputs the number of calories in one portion of that fruit
fruit = input("Item: ").lower()

if fruit in calories_of_fruits:
    print(f"Calories: {calories_of_fruits[fruit]}")
else:
    # Ignore any input that isn’t a fruit.
    # Ignore if it is not in the dictionary.
    pass