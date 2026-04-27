def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    if user == "stone" and computer == "scissor":
        return "You win!"
    elif user == "paper" and computer == "stone":
        return "You win!"
    elif user == "scissor" and computer == "paper":
        return "You win!"
    else:
        return "Computer wins!"