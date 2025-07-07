pet = input("Enter pet type (dog/cat/bird/hamster): ")
age = int(input("Enter your pet's age in human years: "))

pet_age=0
if pet=="dog" or pet =="cat":
    if age <3:
        pet_age=age*12
    else:
        pet_age=24+(age-2)*4
elif pet=="bird":
    pet_age=age*9
elif pet=="hamster":
    pet_age=age*25

print(pet_age)

print(f'''
=== PET AGE CONVERSION ===
Pet Type: {pet}
Human Age: {age} years
Pet Age: {pet_age} pet years

Fun Fact: Your {pet} is like a {pet_age}-year-old human!

''')