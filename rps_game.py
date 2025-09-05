import random

print("🎮 Welcome to Rock-Paper-Scissors!")
name = input("Enter your name: ")

def check_winner(player, computer):
    match (player, computer):
        case (p, c) if p == c:
            return "Draw"
        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return "You win!"
        case _:
            return "Computer wins!"

def rps_game():
    choices = ("rock", "paper", "scissors")
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("❌ Invalid choice! Please type rock, paper, or scissors.")
        return
    
    print(f"Computer chose: {computer_choice}")
    print(check_winner(player_choice, computer_choice))

while True:
    game_state = input(f"\n{name}, do you want to play the game? (y/n): ").lower()
    if game_state != "y":
        print("👋 Thank you for playing!")
        break
    rps_game()
