import random

pass1 = (['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l' 'ç',
        'z' 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', '0'])

password = ""

for x in range(6):
    password = password + random.choices(pass1)[0]

print('Sua nova senha:',password)
