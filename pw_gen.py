import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to this simple Password Generator")

let = int(input("How many letters do you want in your password?\n"))
sym = int(input("How many symbols do you want?\n"))
num = int(input("And how many numbers would you like?\n"))
dif = (input(
    "And now let's choose the complexity (low, high):\n"
)).lower()

if dif == "low":
    password = ""
    for _ in range(1, let + 1):
        random_char = random.choice(letters)
        password += random_char

    for _ in range(1, sym + 1):
        random_sym = random.choice(symbols)
        password += random_sym

    for _ in range(1, num + 1):
        random_num = random.choice(numbers)
        password += random_num
    print(f"Your password is - ' {password} '")

elif dif == "high":
    final_password = []
    for c in range(1, let + 1):
        random_char = random.choice(letters)
        final_password += random_char

    for _ in range(1, sym + 1):
        random_sym = random.choice(symbols)
        final_password += random_sym

    for _ in range(1, num + 1):
        random_num = random.choice(numbers)
        final_password += random_num
    random.shuffle(final_password)
    password = ""
    for i in final_password:
        password += i
    print(f"Your password is - ' {password} '")
else:
    print("Invalid input")
