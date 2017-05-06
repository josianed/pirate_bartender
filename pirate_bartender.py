import random
import sys

if __name__ == '__main__':
    main()

def main():
    '''Creates a drink based on users' drink style preferences'''

    customer_name = input("Ho there matey! How are ye called? ")
    regular_customer = customer_preferences.get(customer_name, "empty")
    if regular_customer != "empty":
        print("The usual for ya, the {}!".format(regular_customer))
        print(*cocktails[regular_customer], sep=", ")
        place_order = input("Would ye like another? ")
        order(customer_name, place_order)
    else:
        place_order = input("Would ye like a drink, {}? ".format(customer_name))
        order(customer_name, place_order)

def order(customer_name, place_order):
    '''Takes customer's order and makes drink if desired, or exits program if not'''
    while place_order == "yes" or place_order == "y":
        drink_preferences()
        drink = make_drink(preferences)
        #generate name
        name = cocktail_name()
        #save to cocktail dictionary
        cocktails[name] = drink
        #save customer preference
        customer_preferences[customer_name] = name
        print("Here's the {}, {}!".format(name, customer_name))
        print(*drink, sep=", ")
        place_order = input("Would ye like another? ")
    if place_order == "no" or place_order == "n":
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
            while not stock_control(ingredient):
                ingredient = random.choice(ingredients[flavour])
            # print("Added {} to yer drink!".format(ingredient))
            drink.append(ingredient)

    check_stock()

    return drink


def cocktail_name():
    '''Generates a cocktail name by randomly selecting an adjective and noun from lists'''
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    name = "{} {}".format(adjective, noun)
    return name

def stock_control(ingredient):
    '''Checks if ingredient for drink is available; if it is, removes item from inventory'''
    if stock[ingredient] == 0:
        return False
    else:
        stock[ingredient] -= 1
        return True

def check_stock():
    '''Checks if supplies are low'''
    sum = 0
    for item, amount in stock.items():
        sum += stock[item]
    if sum < len(stock):
        restock()

def restock():
    '''Adds inventory to each item in in stock'''
    for item, amount in stock.items():
        stock[item] = 5

#Dictionaries
stock = {
    "glug of rum": 2,
    "slug of whisky": 2,
    "splash of gin": 2,
    "olive on a stick": 2,
    "salt-dusted rim": 2,
    "rasher of bacon": 2,
    "shake of bitters": 2,
    "splash of tonic": 2,
    "twist of lemon peel": 2,
    "sugar cube": 2,
    "spoonful of honey": 2,
    "spash of cola": 2,
    "slice of orange": 2,
    "dash of cassis": 2,
    "cherry on top": 2,
}

preferences = {}

cocktails = {
    "salty president": ["salt-dusted rim", "shake of bitters", "slice of orange", "glug of rum"],
}

customer_preferences = {
    "Bailey": "salty president",
}

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

nouns = ["aardvark", "abacus", "abbey", "abdomen", "ability", "abolishment", "abroad", "abuse", "accelerant",
"accelerator", "access", "accident", "accommodation", "accompanist", "accordion", "account", "accountant", "achiever",
"acid", "acknowledgment", "acoustic", "acoustics", "acrylic", "act", "action", "activity", "actor", "actress",
"acupuncture", "ad", "adapter", "addiction", "addition", "address", "adjustment", "administration", "adrenalin", "adult",
"adulthood", "advance", "advancement", "advantage", "advertisement", "advertising", "advice", "affair", "affect",
"aftermath", "afternoon", "aftershave", "aftershock", "afterthought", "age", "agency", "agenda", "agent", "aggression", "aglet", "agreement",
"aid", "air", "airbag", "airbus", "airfare", "airforce", "airline", "airmail", "airplane", "airport", "airship", "alarm", "alb", "albatross",
"alcohol", "alcove", "alder", "algebra", "alibi", "allergist", "alley", "alligator",
"alloy", "almanac", "almond", "alpaca", "alpenglow", "alpenhorn", "alpha", "alphabet", "alternative", "altitude",
"alto", "aluminium", "aluminum", "ambassador", "ambition", "ambulance", "amendment", "amount", "amusement", "anagram",
"analgesia", "analog", "analogue", "analogy", "analysis", "analyst", "anatomy", "anesthesiology", "anethesiologist", "anger",
"angiosperm", "angle", "angora", "angstrom", "anguish", "apparatus", "apparel", "appeal", "appearance", "appendix",
"applause", "apple", "applewood", "appliance", "application", "appointment", "approval", "apron", "apse", "aquifer",
"arch", "archaeology", "archeology", "archer", "architect", "architecture", "arch-rival", "area", "argument", "arithmetic", "arm",
"armadillo", "armament", "armchair", "armoire", "armor", "arm-rest", "army", "arrival", "arrow", "art", "artichoke", "article",
"artificer", "ascot", "ash", "ashram", "ashtray", "aside", "ask", "asparagus", "aspect", "asphalt", "assignment",
"assist", "assistance", "assistant", "associate", "association", "assumption", "asterisk", "astrakhan", "astrolabe",
"astrologer", "astrology", "astronomy", "atelier", "athlete", "athletics", "atmosphere", "atom", "atrium", "attachment",
"attack", "attempt", "attendant", "attention", "attenuation", "attic", "attitude", "attorney", "attraction", "audience", "auditorium",
"aunt", "author", "authorisation", "authority", "authorization", "automaton", "avalanche", "avenue", "average", "award", "awareness",
"azimuth", "babe", "baboon", "babushka", "baby", "back", "backbone", "backdrop", "background", "backpack", "bacon", "bad", "badge", "badger",
"bafflement", "bag", "bagel", "baggage", "bagpipe", "bail", "bait", "bake", "baker", "bakery", "bakeware", "balaclava", "balalaika", "balance", "balcony", "ball",
"ballet", "balloon", "ballpark", "bamboo", "banana", "band", "bandana", "bandanna", "bandolier", "bangle", "banjo", "bank", "bankbook", "banker", "banquette",
"baobab", "bar", "barbeque", "barber", "barbiturate", "barge", "baritone", "barium", "barn", "barometer", "barracks", "barstool", "base", "baseball", "basement",
"basin", "basis", "basket", "basketball", "bass", "bassinet", "bassoon", "bat", "bath", "bather", "bathhouse", "bathrobe", "bathroom", "bathtub", "batter",
"battery", "batting", "battle", "battleship", "bay", "bayou", "beach", "bead", "beak", "beam", "bean", "beanie", "beanstalk", "bear", "beard", "beast",
"beat", "beautiful", "beauty", "beaver", "bed", "bedroom", "bee", "breastplate", "breath", "breeze", "bribery",
"brick", "bricklaying", "bridge", "brief", "briefs", "brilliant", "british", "broad", "broccoli", "brochure", "broiler", "broker", "calculator", "calculus", "calendar", "calf", "calico",
"call", "calm", "camel", "cameo", "camera", "camp", "campaign", "campanile", "can", "canal", "cancel", "cancer", "candelabra", "candidate", "candle", "candy", "cane", "cannon", "canoe",
"canon", "canopy", "canteen", "canvas", "cap", "cape", "capital", "capitulation", "capon", "cappelletti", "cappuccino", "captain", "caption", "car",
"cardigan", "yeast", "yellow", "yesterday", "yew", "yin", "yoga", "yogurt", "yoke", "you", "young", "youth", "yurt", "zampone", "zebra", "zebrafish", "zephyr", "ziggurat", "zinc"]

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




#Tests
# drink_preferences()
#
# for flavour, isPreference in preferences.items():
#     print(flavour, isPreference)
#
# drink = make_drink(preferences)
# print(*drink, sep='\n')
