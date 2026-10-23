import random

print("Welcome to Rock Paper Scissor")

user_choice = input("Choose 1 for rock , choose 2 for paper , choose 3 for scissor :")
computer_choice = random.randint(1,3)

if user_choice == 1 and computer_choice == 3:
    print("You win")

elif computer_choice  == 1 and user_choice == 3:
    print("You lose")
elif user_choice < computer_choice:
    print("Computer wins")
elif user_choice == computer_choice:
    print("draw")
elif user_choice > computer_choice:
    print("you win")
else:
    print("You typed an invlid number you lost")
