
import random

print("welcome to rock paper scissors! \n Choose between \n 1 - rock \n 2 - paper \n 3 - scissors")


while True:
    
    choice=int(input("Enter the number assigned to the choices above: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please : "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"

    elif choice == 3:
        choice_name = "scissors"

    print("Your choice is " + choice_name)
    print("now the computers turn")

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    elif comp_choice == 3:
        comp_choice_name = "Scissors"
    

    print("Computer choice is: ", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 2):
        result = "Scissors"

    if result == "DRAW":
        print(" Tie ")
    elif result == choice_name:
        print(" User wins")
    else:
        print(" computer wins")

    print("do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == "n":
        break
print("thx for playing")
