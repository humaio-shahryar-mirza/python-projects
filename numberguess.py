import random
lower_range = 1
higher_range = 10
max_attempts_of_range = 10

secret_number = random.randint(lower_range, higher_range)

def get_guess():
    while True:
        try:
            guess = int(input(f"guess a number between {lower_range} and {higher_range} "))
            if lower_range <= guess <= higher_range:
                return guess
            else:
                print("invalid input, please pick a number from the specified range")
        except ValueError:
            print("invalid input, please enter an integer")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correc... kawaii chaann >_<!"
    elif guess < secret_number:
        return "too low.."
    else:
        return "too hai."
    
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts_of_range:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
         
        if result == "correc... kawaii chaann >_<!":
            print(f"sogoto..! you guessed the secret number {secret_number} in {attempts} attempts!")
            won = True
            break
        else:
            print(f"{result}. badboy")

    if not won:
        print(f"sorry, u bad asl (ran out of attempts), but the secret number was {secret_number}")

if __name__ == "__main__":
    print("arigato gozaimasu, welcome to the number guessing gem.")
    play_game()

































