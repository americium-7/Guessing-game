import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    
    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

number_guessing_game()