
# Assignment 1 - Part 4

# Assuming milo dictionary from Part 3 is already defined
milo = {
    "name": "Milo",
    "species": "Cat",
    "age": 3,
    "weight": 5.0,
    "adopted": True,
    "vaccinated": True
}

# 1. Simple If-Else Statement (Checking if Milo is an adult or baby)
print("--- 1. Age Condition Check ---")
if milo["age"] >= 2:
    print(milo["name"], "is an adult.")
else:
    print(milo["name"], "is a baby.")
print()

# 2. Elif (Else-If) Ladder (Categorizing weight into Small, Medium, or Large)
print("--- 2. Weight Category Check ---")
if milo["weight"] < 5.0:
    print(milo["name"], "is small.")
elif milo["weight"] <= 15.0:
    print(milo["name"], "is medium.")
else:
    print(milo["name"], "is large.")
print()

# 3. Inline If-Else / Ternary Operator (Checking adoption status)
print("--- 3. Adoption Status Check ---")
adoption_status = "Yes" if milo["adopted"] else "No"
print("Adopted:", adoption_status)

# 4. Inline If-Else for Vaccination Status
vaccination_status = "Yes" if milo["vaccinated"] else "No"
print("Vaccinated:", vaccination_status)