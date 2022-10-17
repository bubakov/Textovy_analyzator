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

    #privita uzivatele pokud heslo a jmeno souhlasi
    print(f'Welcome to the app, {username}')

else:
    # ukonci program pokud neni uzivatel ve slovniku nebo je zadana 
    # spatna kombinace jmena a hesla
    print(f'Unregistered user: {username}, terminating program')


