#DICTIONARY =  a changable , unorered colletion of unique key:value pairs
#              fast because they use hashing, allowing quick access!

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Bejing",
            "Russia":"Moscow",
            "UK":"London"}
print(capitals["USA"])
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get("Germany"))
# we can always use for loop to display items of dictionary!!!
#lemme just use regular syntax and try printing items of dictionary to see if it's works?
for x in capitals:
    print(x)
#it just prints key only!!!
for key,value in capitals.items():
    print(key,value)
capitals.update({"Germany":"Berlin"}) # *** {} *** the syntax is important
capitals.update({"USA":"New York"})    #we can also update existing value!!!
capitals.pop("UK") # we can remove any keya;value pair!!! **** here syntax is diferent ****
capitals.clear()
for key,value in capitals.items():
    print(key,value)

#INDEX OPERATOR!!

#index operator = it gives access to sequence's element.
#                      ***includes these not limited to these(str,list,tuples)***

name = "xiang tzu!"
#to check if element is lowercase (need to check fisrt letter or element  of string or sequence)
if (name[0].islower()):    #to check we have ***islower()*** method
    name = name.capitalize()
print(name)

#to extract or to create sub string
first_name = name[:5].upper()
print(first_name)
last_name = name[6:].lower()
print(last_name)
#to work with negative index
last_character = name[-1]
print(last_character)



#a = 78
#b = 35
#x = a - b
#print(x)
