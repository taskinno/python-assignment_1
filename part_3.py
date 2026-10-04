
# Assignment 1 - Part 3

# 1. Creating a dictionary for Milo
milo = {
    "name": "Milo",
    "species": "Cat",
    "age": 3,
    "weight": 5.0,
    "adopted": True
}

# 2. Displaying the complete milo dictionary
print(milo)
print()

# 3. Displaying specific values using keys
print(milo["name"])
print(milo["age"])
print(milo["weight"])
print()

# 4. Modifying Milo's weight and displaying the updated dictionary
milo["weight"] = 5.2
print(milo)
print()

# 5. Adding a new key 'vaccinated' with value True
milo["vaccinated"] = True

# 6, 7, 8. Displaying keys, values, and items of the dictionary
print(list(milo.keys()))
print(list(milo.values()))
print(list(milo.items()))
print()

# 9. Creating dictionaries for other animals
luna = {
    "name": "Luna",
    "species": "Dog",
    "age": 1,
    "weight": 6.2,
    "adopted": False,
    "vaccinated": True
}

rocky = {
    "name": "Rocky",
    "species": "Dog",
    "age": 2,
    "weight": 28.5,
    "adopted": True,
    "vaccinated": True
}

bella = {
    "name": "Bella",
    "species": "Cat",
    "age": 5,
    "weight": 5.1,
    "adopted": False,
    "vaccinated": False
}

max_dict = {
    "name": "Max",
    "species": "Dog",
    "age": 7,
    "weight": 22.3,
    "adopted": False,
    "vaccinated": True
}

nala = {
    "name": "Nala",
    "species": "Cat",
    "age": 4,
    "weight": 4.8,
    "adopted": False,
    "vaccinated": False
}

# 10. Creating a list called 'animals' containing all six dictionaries
animals = [milo, luna, rocky, bella, max_dict, nala]

# 11. Using indexing and dictionary keys to display specific info
print(animals[0]["name"])   # First animal's name
print(animals[2]["species"]) # Third animal's species
print(animals[-1]["weight"]) # Last animal's weight
