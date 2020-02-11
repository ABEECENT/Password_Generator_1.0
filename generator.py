import random
import string

def letter_menu():
    print('[1] Only Upper Case Letters')
    print('[2] only lower case letters'.title())
    print('[3] mixed upper and lower case letters'.title()+'\n')

    opt=input('Your Choice ==> ')

    return int(opt)

def gen_dig_sym(l=6):
    letter=input('Would you like it to contain letters? (Y/N) ==> ')
    print()

    while letter not in ['y','Y','n','N']:
        print('please try again'.title())
        letter=input('Would you like it to contain letters? (Y/N) ==> ')
        print()

    if(letter in ['y','Y']):
        letter_spec=letter_menu()
        print()

        while letter_spec not in [1,2,3]:
            print('please try again'.title())
            letter_spec=letter_menu()
            print()

    digit=input('Would you like it to contain digits (0-9)? (Y/N) ==>')
    print()

    while digit not in ['y','Y','n','N']:
        print('please try again'.title())
        digit=input('Would you like it to contain digits (0-9)? (Y/N) ==> ')
        print()

    special=input('Would you like it to contain special characters (. , ? !)? (Y/N) ==>')
    print()

    while special not in ['y','Y','n','N']:
        print('please try again'.title())
        special=input('Would you like it to contain special characters (. , ? !)? (Y/N) ==> ')
        print()

    password_store=''

    if(letter=='y' or letter=='Y'):
        if(letter_spec==1):
            password_store+=string.ascii_uppercase

        elif(letter_spec==2):
            password_store+=string.ascii_lowercase

        else:
            password_store+=string.ascii_letters

    if(digit=='y' or digit=='Y'):
        password_store+=string.digits

    if(special=='y' or special=='Y'):
        password_store+=string.punctuation

    return ''.join(random.choice(password_store) for i in range(l))
