from random import randint
guess = ''
guess_value = {'heads':1, 'tails':0}
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = randint(0, 1)
    if toss == guess_value[guess]:
        print(toss)
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == guess_value[guess]:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')