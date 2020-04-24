import random
import string
import sys

domains = [ 'hotmail.com' , 'gmail.com' , 'fiap.com.br']
letters = string.ascii_lowercase



def get_one_random_domain(domains):
    return random.choice(domains)

def get_one_random_name(letters):
    return ''.join(random.choice(letters) for i in range(7))

def generate_random_emails():
    return get_one_random_name(letters) + '@' + get_one_random_domain(domains) 



def main():

    arrayMail = []
    checkAgain = 'Y'


    while  checkAgain.upper() == 'Y' :

        while len(arrayMail) < 31: 

            arrayMail.append(generate_random_emails())

        searchForMail = input('Check if your email password has been disclosed: ')

        if searchForMail in arrayMail:
            print('Change your password right now!')
        
        else:
            print('You are safe, for now...')

        arrayMail = []

        checkAgain = input('Would you like to check an mail? (Y / N)' )







if __name__ == "__main__":
    main()