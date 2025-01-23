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
    letterIndex = random.randint(0, len(letters) - 1)
    final_password_easy += letters[letterIndex]

for num in range(1, nr_symbols + 1):
    symbolIndex = random.randint(0, len(symbols) - 1)
    final_password_easy += symbols[symbolIndex]

for num in range(1, nr_numbers + 1):
    numberIndex = random.randint(0, len(numbers) - 1)
    final_password_easy += numbers[numberIndex]

print("Your easy password is: " + final_password_easy)


character = 0
charsRemaining = nr_letters
numsRemaining = nr_numbers
symbolsRemaining = nr_symbols


total_chars = charsRemaining + numsRemaining + symbolsRemaining

for i in range(0, total_chars + 1):

    condition = False
    while condition == False:
        charType = random.randint(0, 2)
        if charType == 0 and charsRemaining > 0:
            charIndex = random.randint(0, len(letters) - 1)
            charToAdd = letters[charIndex]
            final_password_hard += charToAdd
            condition = True
        elif charType == 1 and symbolsRemaining > 0:
            charIndex = random.randint(0, len(symbols) - 1)
            charToAdd = symbols[charIndex]
            final_password_hard += charToAdd
            condition = True
        elif charType == 2 and numsRemaining > 0:
            charIndex = random.randint(0, len(symbols) - 1)
            charToAdd =numbers[charIndex]
            final_password_hard += charToAdd
            condition = True
        else:
            condition = False

print("Your hard password is: " + final_password_hard)