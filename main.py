# Password generator

import generator
from generator import gen_dig_sym

# title

again=1

while(again!=0):
    print('< < < password generator > > >'.upper())
    print('[1] generate a password'.title())
    print('[0] exit'.upper()+'\n')

    again=input('Your Choice ==> ')
    print()

    if(again=='0'):
        print('Thank you for using our application :D')
        break
    else:
        val=input('Enter the length of the password (min 6) ==> ')

        while(int(val)<6):
            print('please try again'.title())
            val=input('Enter the length of the password (min 6) ==> ')

        print()
        print('here is your randomly generated password ==>'.title()+gen_dig_sym(int(val)))
        print()
