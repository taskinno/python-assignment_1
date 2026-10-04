
# Assignment 1 - Part 2

# 1. Creating four parallel lists for names, species, ages, and weights
names = ["Milo", "Luna", "Rocky", "Bella", "Max"]
species = ["Cat", "Dog", "Dog", "Cat", "Dog"]
ages = [3, 1, 2, 5, 7]
weights = [5.0, 6.2, 28.5, 5.1, 21.8]

# 2. Using indexing to display the name of the first animal
print("First animal in the shelter:", names[0])
print()

# 3. Using indexing to display Rocky's age
print("Rocky's age:", ages[2], "years")
print()

# 4. Using negative indexing to display the name and weight of the last animal
print("Last animal name:", names[-1])
print("Last animal weight:", weights[-1], "kg")
print()

# 5. Using the len() function to determine and display the number of animals
print("Number of animals in the shelter:", len(names))
print()

# 6. Using appropriate functions to determine extremes
print("Age of the youngest animal:", min(ages), "years")
print("Age of the oldest animal:", max(ages), "years")
print("Weight of the lightest animal:", min(weights), "kg")
print("Weight of the heaviest animal:", max(weights), "kg")
print()

# 7. Calculating and displaying the average age using sum() and len()
average_age = sum(ages) / len(ages)
print("Average age of the animals:", average_age, "years")
print()

# 8. Correcting Max's weight to 22.3 kg (Max is at index 4)
weights[4] = 22.3
print("Max's corrected weight:", weights[4], "kg")
print()

# 9. Adding a new animal (Nala) using append()
names.append("Nala")
species.append("Cat")
ages.append(4)
weights.append(4.8)

# 10. Displaying the updated number of animals in the shelter
print("Updated number of animals in the shelter:", len(names))