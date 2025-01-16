# print("Tell me your age:")
# age = input()
# print(age)
# 15

# #Write a simple code that swap the value in 2 different variables.

# # Cara Satu
# # Define two variables
# a = 5
# b = 10

# # Print original values
# print("Before swapping:")
# print("a =", a)
# print("b =", b)

# # Swap the values
# a, b = b, a

# # Print swapped values
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# Define two variables
a = 5
b = 10

# Print original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values using a temporary variable
sementara = a
a = b
b = sementara

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


# Formatting Output
# Ask the user for their age
age = int(input("Please enter your age: "))

# Calculate age in 50 years
future_age = age + 50

# Display the result with 3-digit formatting
print(f"In 50 years, you will be: {future_age:03d} years old.")

# EXERCISE HANGMAN 1
# Step 1: Create a secret word
secret_word = "python"

# Step 2: Ask user to give a letter
letter = input("Please enter a single letter: ")

# Step 3: Make sure the input is valid (a single letter)
if len(letter) != 1 or not letter.isalpha():
    print("Invalid input! Please enter exactly one letter.")
else:
    # Step 4: Check if the letter is in the secret word (case-insensitive)
    if letter.lower() in secret_word.lower():
        print(f"Yes, the letter '{letter}' is in the secret word!")
    else:
        print(f"No, the letter '{letter}' is not in the secret word.")
