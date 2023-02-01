import random
n = random.randrange(9,90)
guess = int(input("Enter the first guess:"))
while n!= guess:
    if guess < n:
        print("Too low!")
        guess = int(input("Enter the next guess"))
    elif guess > n:
         print("Too high!")
         guess = int(input("Enter the next guess"))
    else:
         break
print("You guessed it right!!")         
    
