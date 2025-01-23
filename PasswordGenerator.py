import random

final_password_easy = ""
final_password_hard = ""

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#easy way

for num in range(1, nr_letters + 1):
    final_password_easy += random.choice(letters)

for num in range(1, nr_symbols + 1):
     final_password_easy += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    final_password_easy += random.choice(numbers)

print("Your easy password is: " + final_password_easy)


#slightly harder way

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)  # put list of nums, symbols, letters in random order2
final_password_hard = ""
for char in password_list:
    final_password_hard += char

print("Your hard password is: " + final_password_hard)
