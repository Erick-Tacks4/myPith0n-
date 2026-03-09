import random, sys


correct = random.randint(1 , 100)

for guess_taken in range(1 , 6):
    guess = int(input('Enter your guess number between 1 and 100: '))

    if guess < correct:
        print('Too Low. Guess a higher value')

    elif guess > correct:
        print('Your guess is too big. Guess a lower number number than this')

    #else:
        #continue

    elif guess_taken == 4:
        print('You have ', guess_taken , 'guesses remaining')
        

    else:
        break 

if guess == correct:
    print('Hurray!!!. You are the Bazzuu!!.. You guessed it correctly in just ', guess_taken , ' attempts')

else:
    print()
    print('You have exhausted all your ', guess_taken, ' chances. Try again next time. The correct guess was: ', correct)

input('>>>')

sys.exit()