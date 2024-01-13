import random

# Input the desired number of characters for each category
uppercase_letters = int(input("How many uppercase letters: "))
lowercase_letters = int(input("How many lowercase letters: "))
numbers = int(input("How many numbers: "))
special_characters = int(input("How many special characters: "))

# Define character sets
lowercase_set = 'abcdefghijklmnopqrstuvwxyz'
uppercase_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers_set = '0123456789'
special_set = '!@#%^&*()+=/[]?'

# Initialize an empty list to store all possible characters
all_characters = []

# Add characters from each category to the list
all_characters.extend(random.sample(lowercase_set, lowercase_letters))
all_characters.extend(random.sample(uppercase_set, uppercase_letters))
all_characters.extend(random.sample(numbers_set, numbers))
all_characters.extend(random.sample(special_set, special_characters))

# Shuffle the characters to randomize the order
random.shuffle(all_characters)

# Generate the final password by joining the characters
password = ''.join(all_characters)

print("Generated Password:", password)
