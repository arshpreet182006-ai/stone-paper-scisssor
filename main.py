from computer import get_computer_choice
from result import check_winner

def play_game():
    user_choice = input("Enter stone, paper or scissor: ").lower()

    if user_choice not in ["stone", "paper", "scissor"]:
        print("Invalid choice!")
        return

    computer_choice = get_computer_choice()

    print("Computer chose:", computer_choice)

    result = check_winner(user_choice, computer_choice)
    print(result)

play_game()
