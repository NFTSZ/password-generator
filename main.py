import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*_'
num_pass = int(input('Number of passwords: '))
len_pass = int(input('Lenght of password: '))

for pss in range(num_pass):
    password = ''
    for n in range(len_pass):
        password += random.choice(chars)
    print(password)