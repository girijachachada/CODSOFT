import random
import string
def passwordgenerator(length):
    c = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    password = ''.join(random.choice(c) for i in range(length))
    return password

def main():
    print()
    print('This is the password generator!!')
    print()
    plength=int(input('Enter length of your password : '))
    print()
    try:
        if plength<=0:
            print('Password length should be greater than 0')
        password=passwordgenerator(plength)
        print(f'Password generated : {password}')
    except ValueError:
        print('Invalid Input')
main()