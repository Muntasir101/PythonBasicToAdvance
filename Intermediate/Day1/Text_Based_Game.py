import random


def play_game(user_choice):
    """
    Play a text-based game (e.g., rock-paper-scissors) against the computer.

    Parameters:
    - user_choice (str): User's choice (rock, paper, or scissors)

    Returns:
    str: Result of the game (win, lose, or tie).
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"


# Example usage:
user_input = input("Enter your choice (rock, paper, scissors): ").lower()
result = play_game(user_input)
print(result)
