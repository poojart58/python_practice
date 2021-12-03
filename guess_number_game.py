# This code is a game in which user gives a number as an input and guess where the string(0) can be. every time the position of the string changes
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("pick a number : ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess]=='0':
        print("correct it is !!!")
    else:
        print("Wrong Guess!!!")
        print(mylist)

mylist = [' ','0','  ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list,guess)

