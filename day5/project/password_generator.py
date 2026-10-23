import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

specials = ['!','@','#','$','%','^','&','*','+']

print("Welcome to python password generator")
nr_letters = int(input("How many letters would you like in password : "))
nr_num = int(input("How many numbers would you like in password : "))
nr_special = int(input("How many special characters would you like in password : "))

password = []

for i in range(0,nr_letters):
    password.append(random.choice(letters))

for j in range(0,nr_num):
    password.append(random.choice(numbers))

for k in range(0,nr_special):
    password.append(random.choice(specials))

random.shuffle(password)
print(len(password))
print(password)

password1 = ""

for char in password:
    password1+= char

print(password1)

