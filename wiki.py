string = "A string"
integers = 99
floats = 1.125
lst = ["Item 1", "item 2", 156, 3.14, ["new list inside"]]
tpl = ("item 1", floats)
sets = {"item1", "item2"}
dictionary = {
    "key": "value",
    "key2": "value 2"
}
booleans = True  # or False /// Nebo 1 - 0
none = None


# (!Ale v shellu) když chci tak za datatyp dám . a ono by se mě mělo ukázat metody pro ten datatyp <!------------------------
# toto je docela dobré k prozkoumávání co je možné s nějakou datatype dělat


# print(1_000_000_000) -> _ je tam kvůli human readable
# print(string.capitalize())


# mutable vs immutable (changeable vs unchangeable) <!------------------------
# strings are immutable -> you can just overwrite it. ROzdíl je vtom, že třeba pokud přidáme (append) item do listu tak to není potřeba uložit, ale když změníš string třeba na uppercase tak to musíš uložit znovu pod tím variable


# lists: <!------------------------
# list inside lists possible
# lst.append("new item in list")
# lst.remove("Item 1")
# last_variable = lst.pop() => last_variable = "new item in list"
# lists jsou MUTABLE narozdíl od tuples, které jsou IMUTABLE -> například můžeme změnit pořadí itemů v listu přes .sort()
#
#
# list enumeration -> prostě dodá itemům v listu index <!------------------------
# for animal in enumarate(animals):
# toto nám dá a list of tuples s pořadím:
#   (0, 'dog')
#   (1, 'cat')
#   (2, 'zebra')
# for index, animal in enumarate(animals):
#   0 dog
#   1 cat
#   2 zebra
# můžeme s tím udělat:
# for index, animal in enumarate(animals):
#   if index % 2 == 0: (ukaž každou druhou item)
#       continue
#
#   cat
#
#
# list comprehension -> if we want to create a new list out of a old list <!------------------------
# list comprehension -> shorter syntax when you want to create a new list based on the values of an existing list
# numbers = [x for x in [1, 3, 5, 7, 9]]
# numbers2 = [x**2 for x in [1, 3, 5, 7, 9]] -> vytvoř nový list a itemy v nich vynásob na druhou


# dictionary <!------------------------
# person = {
#     "name": "David",
#     "age": 31,
#     "position": "noob"
# }
# print(person['age'])
# lol = person.values()
# print(lol)
# Přidám do person dictionary další věc
# person['instagram'] = "@lolec"
# print(person)
# del person['age']
# print(person)
#
#
# dictionary comprehension -> if we want from list of tuples create dictionary <!------------------------
# list_tuples = [('name', 'Kalob'), ('occupation', 'coder')]
# d = {key:value for key, value in list_tuples}
# ještě lepší
# d= dict(list_tuples)
#
#
# getting dictionary values <!------------------------
# person = {
#     "name": "David",
#     "age": 31,
#     "position": "noob"
# }
# print(person.get("name", None) -> to None je default, pokud tam key nebude. Můžeme to přepsat default na nějakou třeba string


# tuples <!------------------------
# na tuples také můžeme použít forloop, to znamená že jsou iterable. Tedy můžeme projít jednotlivé itemy v tuple a použít nějaké akce na každou item
# tuples are restricted lists
# rozdíl mezi tuples a listem = IMMUTABLE (not changible)
# například nemůžeme změnit pořadí přes .sort(). U Tuples můžeme akorát .count() a .index()
# foods = ("Pizza", "Orange", "Apple")
# jakmile je tuple nastaveno tak je nastaveno a nemůžu měnit
# je to proto, že je to trochu memory performance sufficient


# sets <!------------------------
# s = {"item", "item2", "item3"}
# 1) sets nemají pořadí, což je dělá trochu efficient
# 2) item musejí být unique, když tam bude stejný tak to mergne
# můžeme přidávat nebo odebírat itemy


# iterable is anything you can loop through -> list, tuple, set even strings <!------------------------


# type casting <!------------------------
# type() - zjistíme co je to za datatype
# turn string = "28" into int -> string = int(string)
# grocery_list = ["Apples", "oranges", "Apples"]
# grocery_list = set(grocery_list) -> sice se změní pořadí, ale nebude tam 2x apples


# print formating <!------------------------
# přidávání variables do stringů
# name = "David"
# 1. nejlepší způsob: welcome_message = f"Hello {name} welcome to python"
# 2. starší: welcome_message = "Hello {} welcome to python".format(name)
# 3. nejstarší: welcome_message = "Hello %s (s jakože string) welcome to python" % name


# forloop <!------------------------
# we can forloop through dictionary with "for key, value in dictionary.items()"
# může tam být .items nebo .keys nebo .values, ale potom bude muset být jiný forloop, jakože for values in dictionary.values()
# pokud dáme nějakou podmínku a ta bude true můžeme dát "continue" pod if a tím se to skipne
# namísto continue můžeme dát break a tím pádem iterace přestane


# while <!------------------------
# většinou to je forloopa, která má iterovat dokud nějaká podmínka


# Functions <!------------------------
# def somenameoffunction():
#   pass
# calling functions somenameoffunction()
# variable ve funkci je použitelná pouze ve funkci
# pokud máme funkci s parametrem def func(name, food="pizza") tak první je required parametr, který musíme dodat při callu funkce,
# druhý není required, jelikož má defaultní hodnotu, takže pokud ji při callu nendodáme tak bude default
#
# pokud je parametr name=None, se používá k tomu aby ve vnitřku funkce byl if statement if name is None: tak to jméno mohu doplnit tam, Je to tam jako default, ale je prázdný <!------------------------
# pokud chceme uložit funkci do variablue a ta func je bez return tak je None. Musíme něco vracet
#
# pokud ve funkci ale budu hledat "name" jako variable který tam není, tak ta funkce ho bude hledat i výše v kódu, a pokud nenajde vypíše že name is not defined <!------------------------
#
#
#
# *args <!------------------------
# tady jde o pozice, pokud přidám name a potom *args jako 2 parametry, tak name je stále positional parametr a required, takže ho musíš vyplnit a pokud budeš mít více names tak to nechceš vypisovat.
# A proto *args, jelikož dáš parametr *args a zavoláš funkci def func(1,2,3,4,5,9,8,7,6) apod
# vrátí to tuple a accessnout ty čísla můžeš pod tuple se jménem args
#
#
# **kwargs <!------------------------
# jde vlastně metodicky o to samé, ale nevznikne tuple ale vznikne dictionary
# protože je to key, word arguments
# zase můžu accesnout tu dictionary přes kwargs, ale můžeš to taky nazvat jinak třeba **subdodavky


# IN operator <!------------------------
# grocery_list = ["Apples", "oranges", "Apples"]
# if "apples" in grocery_list: pass
# to samé můžeme udělat pro dictionary, kde může být if key in dictionary: ... (hledá to Key)
# setx = {"itema", "itemb", "itemc"}
# if "itema" in setx:
#     print("funguje")


# open FILES <!------------------------
# with open('readme.txt', 'r') as file:
#   print(file.read())

# create FILES <!------------------------
# with open('new_file.txt', 'w') as file:
#     file.write('hello from python')
#     file.write('\nhello from python')
#     file.write('\n\thello from python')
# namísto 'w' 'a' je append takže přidá na konec textu další část. Pokud chcem další řádek \n. \t je pro tabbed řádek

# read multilines and lists in FILES <!------------------------
# with open('readme.txt', 'r') as emails:
#   emails = emails.readlines()
#   for email in emails:
#       if 'gmail' in email:
#           pass
#   email.write("něco napíše do emails file")


# API <!------------------------
# pokud budu chtít nachvíli přestat s FORLOOP aby běžela až třeba za chvíli tak time.sleep(60) -> to znamená že forloop znovu proběhne až úp 60sec
# níže je jednoduchý kód na http request (on to nazval jako jednoduché pythoní API)
# import requests
#
# req = requests.get("http://nějaké-api")
# person = req.json()
#
#
#
# Pokud mám dictionary ale ve stringu jelikož json a chci ji zpracovat tak <!------------------------
# uložim do variable
# dict_string = '''{"key: "value"}'''
# import json
# new = json.loads(dict_string) --–> loads je jako load string
# print(new['key'])
#
#
#
# Try / Except <!------------------------
# num = input("enter number")
# try:
#   print("Trying 1/0")
#   total = 1/0
#   print("This will not show up")
# except ValueError:
#   print(num, "This is not number")
# except Exception as e:
#   print("Exception was caught")
#   print(type(e))
#   total = 0
#
#
# YAML is a data serialization language that is often used for writing configuration files
# JSON Javascript object notation. JSON is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page
#
#
# request and response
# The first computer sends a request for some data and the second responds to the request
# More specifically, it is a message exchange pattern in which a requestor sends a request message to a replier system, which receives and processes the request, ultimately returning a message in response
#
# In django requests objects:
# request.GET, request.POST, request.COOKIES, request.HEADER
# In django requests objects:
# httpresponse, jsonresponse, fileresponse
#
#
# Django classed based views
# Class-based views are the alternatives of function-based views. It is implemented in the projects as Python objects instead of functions. Class-based views don’t replace function-based views, but they do have certain advantages over function-based views. Class-based views take care of basic functionalities such as deleting an item or add an item.