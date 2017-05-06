import random

if __name__ == '__main__':
    main()

def main():
    '''Creates a drink based on users' drink style preferences'''

    drink_preferences()
    drink = make_drink(preferences)
    print("Here's yer drink matey!")
    print(*drink, sep=", ")


def drink_preferences():
    '''Asks each question in the questions dictionary and saves all the responses in a new dictionary'''

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


def make_drink(preferences):
    '''Takes the customer's preferences and creates a drink using the ingredients dictionary'''

    drink = []

    for flavour, isPreference in preferences.items():
        if preferences[flavour] == True:
            ingredient = random.choice(ingredients[flavour])
            # print("Added {} to yer drink!".format(ingredient))
            drink.append(ingredient)

    return drink


#Dictionaries
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

preferences = {}


#Tests
# drink_preferences()
#
# for flavour, isPreference in preferences.items():
#     print(flavour, isPreference)
#
# drink = make_drink(preferences)
# print(*drink, sep='\n')
