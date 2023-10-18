import random


def get_user_choice():
    while True:
        user_choice = input(
            "Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == "rock" and computer_choice == "scissors")
          or (user_choice == "scissors" and computer_choice == "paper")
          or (user_choice == "paper" and computer_choice == "rock")):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score - You: {user_score} Computer: {computer_score}")

        play_again = input("Play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

        round_number += 1

    print("Thanks for playing!")


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
