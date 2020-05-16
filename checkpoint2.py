import random
import string
import sys,os
import getpass


domains = [ 'hotmail.com' , 'gmail.com' , 'fiap.com.br']
letters = string.ascii_lowercase



def get_one_random_domain(domains):
    return random.choice(domains)

def get_one_random_name(letters):
    return ''.join(random.choice(letters) for i in range(7))

def generate_random_emails():
    return get_one_random_name(letters) + '@' + get_one_random_domain(domains) 



def main():

    mydict = {}
    checkAgain = 'Y'
    index = 0


    while  checkAgain.upper() == 'Y' :

        while len(mydict) < 31: 

            mydict['mail' + str(index)] =  generate_random_emails().upper()
            index = index + 1

        searchForMail = input('Check if your email password has been disclosed: ')

        if searchForMail.upper() in mydict.values():
            print('Change your password right now!')
        
        else:
            print('You are safe, for now...')

        

        checkAgain = input('Would you like to check an mail? (Y / N) ' )




getpass.getuser()


if __name__ == "__main__":

    arrayChoose = (1,2)

    print('\n')
    print ('=================================================')
    print ('       Check if your email has been leaked        ')
    print ('=================================================')
    print ('\n                                               ')
    print ('       _,.                   ')
    print ('     ,` -.)                  ')
    print ('    ( _/-\\-._               ')
    print ('   /,|`--._,-^|            , ')
    print ('   \_| |`-._/||          , | ')
    print ('     |  `-, / |         /  / ')
    print ('     |     || |        /  /  ')
    print ('      `r-._||/   __   /  /   ')
    print ('  __,-<_     )`-/  `./  /    ')
    print ('  \   `---    \   / /  /     ')
    print ('     |           |./  /      ')
    print ('     /           //  /       ')
    print (' \_/  \         |/  /        ')
    print ('  |    |   _,^- /  /         ')
    print ('  |    , ``  (\/  /_         ')
    print ('   \,.->._    \X-=/^         ')
    print ('   (  /   `-._//^`           ')
    print ('    `Y-.____(__}             ')
    print ('     |     {__)              ') 
    print ('                             ')
    print('\n')

    print('Hi',  getpass.getuser().capitalize() + ',please, select one of the options below...' + '\n')
    print('Press 1 if you wanna check if your email account has been leaked')
    print('press 2 to exit program')
    choose = input('')

    
    if int(choose) not in arrayChoose:

        print('Option not found, bye!')

    elif int(choose) == 2:

        print('See you later')
        input('Press ENTER to exit...')
        
        os._exit(0)

    else:

        main()
        