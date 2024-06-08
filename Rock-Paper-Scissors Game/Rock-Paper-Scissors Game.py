import random
# winning conditions
def main():
    print("Winning conditions for the game are below:")
    print("\nRock vs Paper --- Paper Wins")
    print("Rock vs Scissors --- Rock Wins")
    print("Paper vs Scissors --- Scissors Wins")
    print("Rock vs Rock, Paper vs Paper, Scissors vs Scissors --- Play Again")

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue

        comp_choice_name = get_computer_choice()
        print(f"The user move is: {user_choice}")
        print(f"The computer move is: {comp_choice_name}")

        result = determine_winner(user_choice, comp_choice_name)
        print(result)
        play = play_again()
        if play == 'n':
            break
      
           
#Get user choice

def get_user_choice():
    print("\nEnter your choice from the below list:")
    print("1. Rock\n2. Paper\n3. Scissors")
    try:
        pick = int(input("Enter the number: "))
    except ValueError:
        print("Enter a valid number")
        return None

    if pick == 1:
        return 'Rock'
    elif pick == 2:
        return 'Paper'
    elif pick == 3:
        return 'Scissors'
    else:
        print("Enter a valid number")
        return None

#Get computer choice
def get_computer_choice():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        return 'Rock'
    elif com_choice == 2:
        return 'Paper'
    else:
        return 'Scissors'

#gives the winner
def determine_winner(user_choice, comp_choice_name):
    if user_choice == comp_choice_name:
        return "It's a draw! Play again."

    if (user_choice == 'Rock' and comp_choice_name == 'Paper') or \
       (user_choice == 'Paper' and comp_choice_name == 'Rock'):
        winner = 'Paper'
    elif (user_choice == 'Rock' and comp_choice_name == 'Scissors') or \
         (user_choice == 'Scissors' and comp_choice_name == 'Rock'):
        winner = 'Rock'
    elif (user_choice == 'Paper' and comp_choice_name == 'Scissors') or \
         (user_choice == 'Scissors' and comp_choice_name == 'Paper'):
        winner = 'Scissors'

    if winner == user_choice:
        return "User wins!"
    else:
        return "Computer wins!"

# Promt asking whether to continue playing or not
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ")
        if choice == 'n':
            return choice

if __name__ == "__main__":
    main()
