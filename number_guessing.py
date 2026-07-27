import random
from typing import Tuple, List, Optional

DIFFICULTY_LEVELS = {
    "1": {"name": "Easy",       "max_num": 50,  "max_attempts": 10},
    "2": {"name": "Medium",     "max_num": 100, "max_attempts": 9},
    "3": {"name": "Hard",       "max_num": 200, "max_attempts": 8},
    "4": {"name": "Very Hard",  "max_num": 500, "max_attempts": 5},
}


def print_header() -> None:
    print("=" * 44)
    print("      🎯  Number Guessing Game  🎯")
    print("=" * 44)


def choose_difficulty() -> Tuple[int, int]:
    print("\nSelect difficulty level:")
    print("1. Easy       → 1 to 50   | 10 attempts")
    print("2. Medium     → 1 to 100  |  9 attempts")
    print("3. Hard       → 1 to 200  |  8 attempts")
    print("4. Very Hard  → 1 to 500  |  5 attempts")

    while True:
        choice = input("\nChoose (1-4): ").strip()
        level = DIFFICULTY_LEVELS.get(choice)
        if level is not None:
            print(f"\n→ Selected: {level['name']}")
            return level["max_num"], level["max_attempts"]
        print("--- Invalid choice. Please enter 1, 2, 3 or 4 ---")


def get_guess(max_num: int, guessed_numbers: List[int]) -> Optional[int]:
    """Gets a valid new guess. Returns None if user wants to quit."""
    while True:
        raw = input("Your guess (or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            return None

        if not raw:
            print("Please enter a number!")
            continue

        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number!")
            continue

        if guess < 1 or guess > max_num:
            print(f"Please enter a number between 1 and {max_num}")
            continue

        if guess in guessed_numbers:
            print("You already guessed this number! Try a different one.")
            continue

        return guess


def give_hint(guess: int, secret: int, max_num: int) -> None:
    diff = abs(secret - guess)

    if diff <= 2:
        if guess < secret:
            print("🔥 Very close! Go a bit higher")
        else:
            print("🔥 Very close! Come a bit lower")
    elif diff <= max_num // 10:
        if guess < secret:
            print("Go higher")
        else:
            print("Come lower")
    elif diff <= max_num // 4:
        if guess < secret:
            print("Go higher")
        else:
            print("Come lower")
    else:
        if guess < secret:
            print("Go much higher!")
        else:
            print("Come much lower!")


def calculate_score(attempts: int, max_attempts: int, max_num: int) -> int:
    """
    Score rewards fewer attempts and scales with difficulty.
    First try → ~100 × difficulty multiplier
    Last try  → ~10  × difficulty multiplier
    """
    efficiency = (max_attempts - attempts + 1) / max_attempts
    base = max(int(efficiency * 100), 10)
    difficulty_multiplier = max_num / 50
    return round(base * difficulty_multiplier)


def play_round(max_num: int, max_attempts: int) -> None:
    secret = random.randint(1, max_num)
    attempts = 0
    guessed_numbers: List[int] = []

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"Remaining attempts: {remaining}")

        if guessed_numbers:
            print(f"Previous guesses: {guessed_numbers}")

        guess = get_guess(max_num, guessed_numbers)

        if guess is None:
            print(f"\nYou gave up. The number was {secret}.")
            return

        guessed_numbers.append(guess)
        attempts += 1

        if guess == secret:
            score = calculate_score(attempts, max_attempts, max_num)
            print("\n" + "🎉" * 12)
            print(f"🎉  Congratulations! The number was {secret}")
            print(f"You found it in {attempts} attempt(s)!")
            print(f"Score: {score} 💫")
            print("🎉" * 12)
            return

        give_hint(guess, secret, max_num)
        print()

    print("\n💀 Sorry, you ran out of attempts.")
    print(f"The number was {secret}.")


def play_again() -> bool:
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def game() -> None:
    print_header()
    while True:
        max_num, max_attempts = choose_difficulty()
        play_round(max_num, max_attempts)
        if not play_again():
            print("\nThanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")