'''
Created on Mar 28, 2017

@author: Shurick
'''
import random

MAX_TRIES = 7

print(''' --- Welcome to Guess My Number ---

I'm thinking of a number between 1 and 100.
Try to guess my number in %d''' % MAX_TRIES, end = '')

if MAX_TRIES == 1:
    print('atempt...')
else:
    print('attempts...')
    
number = random.randint(1,100)
tries = 1
guess = int(input('Enter guess %d:' %tries))

while guess != number:
    if guess > number:
        print('Lower...')
    else:
        print('Higher...')
    tries = tries + 1
    if tries > MAX_TRIES:
        break
    guess - int(input('Enter guess %d: ' % tries))
    
    if tries <= MAX_TRIES:
        print('Congratulations! You correctly guessed the number %d and it took you only, %d' % (number,tries))
    else:
        print('\nSorry, you did not guess the number %d in %d' % (number, MAX_TRIES))
    if MAX_TRIES == 1:
        print('try.')
    else:
        print('tries')