import requests, json, random, wikipedia, warnings
from tqdm import tqdm

warnings.filterwarnings("ignore")

version = 1.0

def monero_to_usd():
    print("Downloading Monero price information from the Internet..")

    price = json.loads(requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR,ETH,GBP").content)

    print()

    try:
        amount = float(input("How many Moneroj do you have? "))
    except:
        print("ERROR! INVALID VALUE!")
        return

    for i in price.keys():
        print(f"{i}\t{price[i]*amount}")


def orbit_scan():
    '''still not ready for use'''
    
    print("Performing orbit scan via the Internet (this will take a while)..")

    for i in trange(1, 5):
        orbit = json.loads(requests.get("https://tle.ivanstanojevic.me/api/tle/").content)

        for j in orbit["member"]:
            pass
    
def help_cmd():
    for i in responses.keys():
        print("Command:\t", i)
        
def monero_price():
    print("Downloading Monero price information from the Internet..")

    price = json.loads(requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR,ETH,GBP").content)

    for i in price.keys():
        print(f"{i}\t{price[i]}")

def hello():
    print("Hello there!")

def install_addons():
    '''still not ready for use'''
    
    exec(requests.get("https://raw.githubusercontent.com/PPPDUD/henbot/main/addons.py").content, globals())


def install_addonsbeta():
    '''still not ready for use'''
    
    exec(requests.get("https://raw.githubusercontent.com/PPPDUD/henbot/Unapproved/addons.py").content, globals())
    
def palindrome():
    '''still not ready for use'''
    print("Downloading English word information from the Internet..")

    words = json.loads(requests.get("https://github.com/dwyl/english-words/raw/master/words_dictionary.json").content)

    print("Processing info..")

    words = list(words.keys())

    for i in range(200):
        word = random.choice(words)
        if True: #word.lower() == word.lower()[::-1]:
            print(word)
            
def pass_func():
    pass

def chatbot(statement):
    do_break = False
    for i in responses.keys():
        similarity = nlp(statement).similarity(nlp(i))
        #print(similarity)

        if similarity>=0.5:
            responses[i]()
            do_break = True
            break
    if not do_break:
        #similarity = nlp(statement).similarity(nlp(wikipedia.suggest(statement[:-3])))
        
        #if similarity>=0.5:

        try:
            print(wikipedia.summary(statement, sentences=1))

        except:
            print("ERROR: COMMAND NOT RECOGNIZED")

print("Loading Henbot v1.0..")

responses = {"Hello!":hello, "Hi":hello, "deprecated_mjprices":monero_price, "Get all commands":help_cmd, "Convert XMR to other currencies":monero_to_usd, "Generate a list of palindromes":pass_func, "Install addons":install_addons,\
"Install addons beta":install_addonsbeta}

import spacy
nlp = spacy.load("en_core_web_md")

while True:
    chatbot(input("User>"))
    print()
