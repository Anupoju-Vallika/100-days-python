import random
print("🎮 Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]
# User input
user = input("Choose rock, paper, or scissors: ").lower()
# Computer random choice
computer = random.choice(choices)
print(f"Computer chose: {computer}")
# Game logic
if user not in choices:
    print("❌ Invalid choice! Please choose rock, paper, or scissors.")
elif user == computer:
    print("🤝 It's a draw!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("✅ You win!")
else:
    print("💥 You lose!")
