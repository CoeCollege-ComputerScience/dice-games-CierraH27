import random

# Pig Game
def pig_game():
    print("Welcome to Pig!")
    player_scores = [0, 0]
    current_player = 0

    while max(player_scores) < 100:
        turn_total = 0
        print(f"\nPlayer {current_player + 1}'s turn!")
        while True:
            roll = random.randint(1, 6)
            print(f"Rolled: {roll}")
            if roll == 1:
                print("Rolled a 1! Turn over, no points added.")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}")
                choice = input("Roll again? (y/n): ").lower()
                if choice != 'y':
                    break
        player_scores[current_player] += turn_total
        print(f"Player {current_player + 1}'s total score: {player_scores[current_player]}")
        current_player = 1 - current_player

    winner = player_scores.index(max(player_scores)) + 1
    print(f"\nPlayer {winner} wins with {max(player_scores)} points!")

# Beat That!
def beat_that():
    print("Welcome to Beat That!")
    player_scores = [0, 0]

    while max(player_scores) < 100:
        for player in range(2):
            print(f"\nPlayer {player + 1}'s turn!")
            roll1, roll2 = random.randint(1, 6), random.randint(1, 6)
            roll = int(f"{max(roll1, roll2)}{min(roll1, roll2)}")
            print(f"Rolled: {roll1} and {roll2} -> {roll}")
            player_scores[player] += roll
            print(f"Player {player + 1}'s score: {player_scores[player]}")

    winner = player_scores.index(max(player_scores)) + 1
    print(f"\nPlayer {winner} wins with {max(player_scores)} points!")

# Roll the Bones
def roll_the_bones():
    print("Welcome to Roll the Bones!")
    total_points = 0
    turns = 0

    while True:
        guess = int(input("Enter your guess (5-30): "))
        if guess < 5 or guess > 30:
            print("Invalid guess. Try again.")
            continue

        rolls = [random.randint(1, 6) for _ in range(5)]
        total = sum(rolls)
        print(f"Rolled: {rolls} -> Total: {total}")

        if guess == total:
            points = 50
        elif guess < total:
            points = guess - 5
        else:
            points = 5 - guess

        total_points += points
        turns += 1
        print(f"Points this turn: {points}")
        print(f"Total points: {total_points}")
        print(f"Average points per turn: {total_points / turns:.2f}")

        if input("Play again? (y/n): ").lower() != 'y':
            break

# Prediction
def prediction():
    print("Welcome to Prediction!")
    players = [1, 2, 3]
    while len(players) > 1:
        for player in players[:]:
            print(f"\nPlayer {player}'s turn!")
            prediction = random.randint(1, 6)
            print(f"Prediction: {prediction}")
            rolls = [random.randint(1, 6) for _ in range(10)]
            print(f"Rolled: {rolls}")

            if rolls.count(prediction) < 2:
                print(f"Player {player} is out!")
                players.remove(player)

    print(f"\nPlayer {players[0]} wins!")

# Main Menu
def main():
    while True:
        print("\nChoose a game:")
        print("1. Pig")
        print("2. Beat That!")
        print("3. Roll the Bones")
        print("4. Prediction")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            pig_game()
        elif choice == '2':
            beat_that()
        elif choice == '3':
            roll_the_bones()
        elif choice == '4':
            prediction()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()