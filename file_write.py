import random

def game():
    print("You are playing the game:")
    score = random.randint(1, 100)

    # Fetch the high score
    try:
        with open("hiscore.txt") as f:
            hiscore_data = f.read()
            hiscore = int(hiscore_data) if hiscore_data else 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")
    print(f"High score: {hiscore}")

    if score > hiscore:
        print("New high score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

# Run the game
game()
