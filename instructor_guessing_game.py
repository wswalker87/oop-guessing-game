import random
# let's do a game where you guess a number
# give feedback on it the number is high, low, or corrent. 
# create a method that returns true if the last guess was correct and false if not. 
# bonus not in the directions: Keep a running count of games played and games won.
class GuessingGame:

    # initialize and give a range of numbers to work with
    def __init__(self, winning_number):
        self.winning_number = winning_number
        self.last_game_won = False

    # compare the user's guess to the random number
    def guess(self, user_guess):
        if user_guess < self.winning_number:
            print("Too Low")
            return False
        elif user_guess > self.winning_number:
            print("Too High")
            return False
        else:
            print(f"Correct!")
            self.last_game_won = True

    def solved(self):
        return self.last_game_won

current_game = GuessingGame(10)
# Define an instance method GuessingGame#solved which returns True if the most recent user_guess was correct and False otherwise.
user_guess = 0
while current_game.solved() == False:
    user_guess = int(input(f"Guess a number. "))
    guess_check = current_game.guess(user_guess)
    if current_game.last_game_won:
        print("Congrats. You won")
        break
