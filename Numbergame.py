import random

playing=True

number=random.randint(0,20)

print("I will guess a number from 0 to 20, you have to guess it one digit at a time")
print("The game ends when the number is guessed")

while playing:
    guess=int(input("Enter your guess: "))
    
    if number>guess:
        print("Your guess is LESSER than the number")
        
    elif number<guess:
        print("Your guess is HIGHER than the number")
        
    else:
        print("Your guess is correct...")
        print(f"The number was {number}")
        break    
            
        