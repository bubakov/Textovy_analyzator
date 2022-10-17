"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Jakub Filip
email: comodore@seznam.cy
discord: bubak#2787
"""

#seznam registrovanych uzivatelu ve slovniku 

users = {'bob':  '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'}

#vyzada hodnoty od uzivatele
username = input("Zadejte uzivatelske jmeno".upper())
password = input("Zadejte heslo".upper())

# overi, zda je spravne heslo prirazene k uzivatelskemu jmenu
if users.get(username) == password:

    #privita uzivatele pokud heslo a jmeno souhlasi a oznami pocet textu k analyze
    print(f'Welcome to the app, {username}.\nWe have 3 texts to be analyzed')

else:
    # ukonci program pokud neni uzivatel ve slovniku nebo je zadana 
    # spatna kombinace jmena a hesla
    print(f'Unregistered user: {username}, terminating program')
    
    # nova promenna text
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# vyber cisla textu uzivatelem
vyber = int(input("Enter a number btw. 1 and 3 to select:"))
#print(type(TEXTS))
uprava = TEXTS[vyber - 1]
print(uprava)
hledanaSlova = []
hledanaVelkaSlova = []
hledanaMalaSlova = []
count = 0

# pokud je vybran je ze tri textu, pouzije se nasledujici kod
if 1 <= vyber <= 3:
    # vypocita pocet slov v textu
    pocet_slov = len(uprava.split())
    print(f'There are {pocet_slov} words in the selected text.')
    # najde prvni velke pismeno ve slovu a napise cetnost vyskytu
    for i in uprava.split():
        if i[0].isupper():
            hledanaSlova.append(i)
            print(hledanaSlova)
    
    for i in uprava.split():
        if i.isupper() and i.isalpha():
            hledanaVelkaSlova.append(i)
            print(len(hledanaVelkaSlova))

    for i in uprava.split():
        if i.islower() and i.isalpha():
            hledanaMalaSlova.append(i)
            print(len(hledanaMalaSlova))
        
        



else:
    print("Neumis pocitat do tri?")
