

# Assignment 1 - Part 5

# Assuming the 'animals' list of dictionaries from previous parts is available:
animals = [
    {"name": "Milo", "species": "Cat", "age": 3, "weight": 5.2, "adopted": True, "vaccinated": True},
    {"name": "Luna", "species": "Dog", "age": 1, "weight": 6.2, "adopted": False, "vaccinated": True},
    {"name": "Rocky", "species": "Dog", "age": 2, "weight": 28.5, "adopted": True, "vaccinated": True},
    {"name": "Bella", "species": "Cat", "age": 5, "weight": 5.1, "adopted": False, "vaccinated": False},
    {"name": "Max", "species": "Dog", "age": 7, "weight": 22.3, "adopted": False, "vaccinated": True},
    {"name": "Nala", "species": "Cat", "age": 4, "weight": 4.8, "adopted": False, "vaccinated": False}
]

# 1. Basic For Loop: Iterating through the 'animals' list
print("--- 1. Listing All Shelter Animals ---")
for animal in animals:
    print("Name:", animal["name"], "| Species:", animal["species"])
print()

# 2. For Loop with Conditions: Filtering and printing only the Dogs
print("--- 2. Filtering Dogs Only ---")
for animal in animals:
    if animal["species"] == "Dog":
        print(animal["name"], "is a dog.")
print()

# 3. For Loop with Counting: Counting how many animals are adopted
print("--- 3. Counting Adopted Animals ---")
adopted_count = 0
for animal in animals:
    if animal["adopted"]:
        adopted_count += 1

print("Total adopted animals:", adopted_count)
print()

# 4. While Loop Example: Tracking feeding rounds
print("--- 4. While Loop Example (Feeding Schedule Tracker) ---")
feeding_rounds = 3
while feeding_rounds > 0:
    print("Feeding round left:", feeding_rounds)
    feeding_rounds -= 1
    
print("All feeding rounds completed!")