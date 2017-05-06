questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {
    # "strong": False,
    # "salty": False,
    # "bitter": False,
    # "sweet": False,
    # "fruity": False,
}

def drink_preferences():
    '''Asks each question in the questions dictionary and saves all the positive responses in a new dictionary'''

    print("Let's see what yer perfect drink is like! Answer yes/y or no/n to each of these questions: ")
    for c, q in questions.items():
        response_valid = False
        response = input(q)
        while not response_valid:
            if response == "y" or response == "yes" or response == "n" or response == "no":
                response_valid = True
                add_to_dictionary(c, response)
            else:
                print("Ye need to answer yes or no!")
                response = input(q)


def add_to_dictionary(flavour, answer):
    '''Takes a flavour and user input and adds its equivalent boolean to a dictionary'''

    if answer == "y" or answer == "yes":
        preferences[flavour] = True
    else:
        preferences[flavour] = False



drink_preferences()

for flavour, like in preferences.items():
    print(flavour, like)
