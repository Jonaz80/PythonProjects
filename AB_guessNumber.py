# Guess a number game
import random



print('I am thinking of a number between 1 and 20')
target = random.randint(1, 20)
tries = 5
success = None


for i in range(tries, 0, -1):
    print('You have '+ str(i) +' guesses left')
    guess = input('Take a guess: ')
    try:
        guess = int(guess)
        print
        if guess < target:
            print('Too low!')
        elif guess >target:
            print('Too HIGH!')
        elif guess == target:
            print('SPOT ON :)')
            success = 1
            break
    except:
        print('invalid entry, wasted guess :(')


if success:
    print('Well done, you guessed it in ' + str(tries - i + 1) + ' guesses.')
else:
    print('The number I was thinking of was: ' + str(target) + '.  Better luck next time!')


