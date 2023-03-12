import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password =[]
for letter in range(nr_letters):
  choice = random.choice(letters)
  password += choice

for symbol in range(nr_symbols):
  choice = random.choice(symbols)
  password += choice
 
for number in range(nr_numbers):
  choice = random.choice(numbers)
  password += choice

length_of_password = nr_letters + nr_numbers + nr_symbols

password_shuffle = ""
for char in range(length_of_password):
  choice = random.choice(password)
  password_shuffle += choice
print(f"Your password ganerated is : {password_shuffle}")
