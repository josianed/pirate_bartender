import random
import sys

if __name__ == '__main__':
    main()

def main():
    '''Creates a drink based on users' drink style preferences'''

    place_order = input("Ahoy matey! Would ye like a drink? ")
    while place_order == "yes":
        drink_preferences()
        drink = make_drink(preferences)
        print("Here's yer drink matey!")
        print(*drink, sep=", ")
        place_order = input("Would ye like another? ")
    if place_order == "no":
        print("Fair winds and following seas matey!")
        sys.exit()
    else:
        print("Heave ahead matey, yer drunk!")
        sys.exit()


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

def cocktail_name():



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

nouns = []

adjectives = ["acerbic", "acid", "acidic", "acrid", "aftertaste", "aged", "ambrosial", "ample", "appealing", "appetizing", "aromatic", "astringent", "baked", "balsamic", "beautiful", "bite-size", "bitter", "bland", "blazed",
 "blended", "blunt", "boiled", "brackish", "briny", "brown", "browned", "burnt", "buttered", "caked", "calorie", "candied", "caramelized", "caustic", "center cut", "char-broiled", "cheesy", "chilled", "chocolaty", "choice",
 "chunked", "cinnamon", "classic", "classy", "clove coated", "cold", "cool", "copious", "country", "crafted", "creamed", "creamy", "crisp", "crunchy", "cured", "cutting", "dazzling", "deep-fried", "delectable", "delectable",
 "delicious", "delight", "delightful", "distinctive", "doughy", "dressed", "dripping", "drizzle", "drizzled", "dry", "dulcified", "dull", "edible", "encrusted", "epicurean taste", "ethnic", "extraordinary", "famous", "fantastic",
 "fetid", "fiery", "filet", "fizzy", "flaky", "flat", "flavored", "flavorful", "flavorless", "fleshy", "fluffy", "fragile", "free", "free – range", "fresh", "fried", "frosty", "frozen", "fruity", "full", "full-bodied", "furry", "garlic",
 "garlicky", "generous", "generous portion", "gingery", "glazed", "golden", "gorgeous", "gourmet", "greasy", "grilled", "gritty", "gustatory", "half", "harsh", "heady", "heaping", "heart healthy", "heart smart", "hearty", "heavenly",
 "homemade", "honey", "honeyed", "honey-glazed", "hot", "ice-cold", "icy", "indulgent", "infused", "insipid", "intense", "intriguing", "juicy", "jumbo", "kosher", "large", "lavish", "layered", "lean", "leathery", "lemon", "less", "light",
 "lightly salted", "lightly-breaded", "lip smacking", "lively", "low", "low sodium", "low-fat", "lukewarm", "luscious", "lush", "marinated", "mashed", "mellow", "mil", "minty", "mixed", "mixture of", "moist", "moist", "mouth-watering",
 "nationally famous", "natural", "nectarous", "non-fat", "nutmeg", "nutty", "oily", "open face", "organic", "overpowering", "palatable", "penetrating", "peppery", "perfection", "petite", "pickled", "piquant", "plain", "pleasant", "plump",
 "poached", "popular", "pounded", "prepared", "prickly", "pulpy", "pungent", "pureed", "rancid", "rank", "reduced", "refresh", "rich", "ripe", "roasted", "robust", "rotten", "rubbery", "saccharine", "saline", "salty", "savoury", "Sapid",
 "saporific", "saporous", "satin", "satiny", "sauteed", "savory", "scrumptious", "sea salt", "seared", "seasoned", "sharp", "silky", "simmered", "sizzling", "skillfully", "small", "smelly", "smoked", "smoky", "smooth", "smothered",
 "soothing", "sour", "Southern style", "special", "spiced", "spicy", "spiral-cut", "spongy", "sprinkled", "stale", "steamed", "steamy", "sticky", "stinging", "strawberry", "strong", "stuffed", "succulent", "sugar coated", "sugar free",
 "sugared", "sugarless", "sugary", "superb", "sweet", "sweet-and-sour", "sweetened", "syrupy", "tangy", "tantalizing", "tart", "tasteful", "tasteless", "tasty", "tender", "tepid", "terrific", "thick", "thin", "toasted", "toothsome", "topped",
 "tossed", "tough", "traditional", "treacly", "treat", "unflavored", "unsavory", "unseasoned", "vanilla", "velvety", "vinegary", "warm", "waxy", "weak", "whipped", "whole", "wonderful", "yucky", "yummy", "zesty", "zingy"]

preferences = {}


#Tests
# drink_preferences()
#
# for flavour, isPreference in preferences.items():
#     print(flavour, isPreference)
#
# drink = make_drink(preferences)
# print(*drink, sep='\n')
