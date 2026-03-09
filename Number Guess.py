import random
number = random.randint(1, 100)
guess = None # Start with no guess
limit = 5
#for(i=0 : i <= 5 : i):
while guess != number:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    #elif guess > limit:
       # print("Ooops! You've failed! Try again next time")
        #break
    else:
        print("Hurreeey! You guesssed it correctly")

        