import random
guess = ''
while guess != 'heads' and guess != 'tails':
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.choice(['heads', 'tails'])
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')