import random
import os

SCORE_FILE = "score.txt"

def get_best_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return int(f.read())
    return 0

def save_best_score(score):
    with open(SCORE_FILE, "w") as f:
        f.write(str(score))

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Guess the Number Game (1 - 100)")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("❌ Enter only numbers!")
            continue

        attempts += 1

        if guess > number:
            print("⬇ Too High!")
        elif guess < number:
            print("⬆ Too Low!")
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempts.")
            break

    score = max(0, 100 - (attempts * 5))
    print(f"⭐ Your Score: {score}")

    best = get_best_score()
    if score > best:
        save_best_score(score)
        print("🏆 New Best Score Saved!")
    else:
        print(f"🥇 Best Score: {best}")

while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! 👋")
        break
