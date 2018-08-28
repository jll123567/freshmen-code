import random


def roll(sides=6):
    num_rolled=random.randint(1,sides)
    return num_rolled

def dice():
    sides=6
    rolling=True
    while rolling:
        roll_again=input('Are you ready to roll? ENTER=roll Q=Quit. ')
        if roll_again.lower() !='q':
            num_rolled=roll(sides)
            print('You rolled a', num_rolled)
        else:
            rolling=False

    print ('Thanks for playing')


print ('pick a game!')
print('type guess() to play guess the number, type dice() to play the dice game')


def is_valid_num(s):
    if s.isdigit() and 1 <=int(s) <=100:
        return True
    else:
        return False


def guess():
    number=random.randint(1,100)
    guessed_number=False
    guess=input('guess a number between 1 and 100')
    num_guesses=0
    while not guessed_number:
        if not is_valid_num(guess):
            guess=input('BETWEEN 1 and 100 silly')
            continue
        else:
            num_guesses +=1
            guess=int(guess)

        if guess<number:
            guess=input('too low,guess again: ')
        elif guess > number:
            guess=input('too high,guess again: ')
        else:
            print('you got it in' ,num_guesses,"guesss")
            guessed_number=True

    print('good for you')
