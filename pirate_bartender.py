questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def drink_preferences():
    '''Asks each question in the questions dictionary and saves all the positive responses in a new dictionary'''
    preferences = {}

    print("Let's see what yer perfect drink is like! Answer yes/y or no/n to each of these questions: ")
    for q, a in preferences.items():
        response = input(q)
        if (response == "yes" or response == "y"):

    preferences.update({'item3': 3})
