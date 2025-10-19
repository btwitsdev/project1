import random 
'''
1 for ston
2 for paper
3 for sesior
'''
def game():
    choises = ("stone" , "paper" , "sesior")
    while True:
        user = input("Enter your choise (stone/paper/sesior or quit to stop : ").lower()

        if user == "quit":
            print("\nThanks for Playing!")
            break


        if user not in choises:
            print("\nInvalid state" , "Try Again")
            continue

        

        computer = random.choice(choises)
        print(f"computer choise\t:    {computer}")

        if user==computer:
            print("Its Draw!")
        elif (user == "stone" and computer == "sesior") or\
             (user == "paper" and computer == "stone") or\
                    (user == "sesior" and computer == "paper"):
                    print("You Win!!!")
        else :
            print("You Loss!!!")


game()