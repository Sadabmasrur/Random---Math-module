import random

options=["Rock","Scissors","Paper"]

playing=True
score=0

while playing:
    comp_choice=random.choice(options)
    
    user_choice=input("Please choose Rock, Scissors or Paper(Ensure the spelling is correct...): ")
    
    print("Your chose:",user_choice)
    print("Computer chose:",comp_choice)
    
    if score<5:
        if user_choice==comp_choice:
            print("It is a tie!")
            print(f"Score: {score}\n\n")
            
     
    
        elif user_choice=="Rock" and comp_choice=="Scissors":
            print("Rock smashes Scissors.You win!!!")
            score=score+1
            print(f"Score: {score}\n\n")        
            
            
        elif user_choice=="Paper" and comp_choice=="Rock":
            print("Paper covers Rock.You win!!!")
            score=score+1
            print(f"Score: {score}\n\n")        
                
        
        elif user_choice=="Scissors" and comp_choice=="Paper":
            print("Scissors cuts Paper.You win!!!")
            score=score+1
            print(f"Score: {score}\n\n")        
                   
                   
        else:
            print("You lose, Computer wins this turn")
            print(f"Score: {score}\n\n")    
            
            
    else:
        print(f"Player wins!!!!!!!!!!! Score: {score}")     
        
        playing=False  