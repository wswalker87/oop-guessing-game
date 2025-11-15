import random
# let's do a game where you guess a number
# give feedback on it the number is high, low, or corrent. 
# create a method that returns true if the last guess was correct and false if not. 
# bonus not in the directions: Keep a running count of games played and games won.
class GuessingGame:

    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num
        self.computer_guess = self.get_random_number()
        self.score = 0

    def get_random_number(self):
        random_number = (random.randint(self.start_num, self.end_num))
        # print(f"Random number chosen by the computer is {random_number}")
        return random_number

    def user_input(self):
        while True:
            user_guess = int(input(f"Guess a number between {self.start_num} and {self.end_num} "))
            # print(f"The user guessed {user_guess}.")
            if self.end_num >= user_guess >= self.start_num:
                return user_guess
            else:
                print(f"The chosen number is outside the limit. Choose a number between {self.start_num} and {self.end_num}")

    def game_test(self, user_guess):
        if user_guess < self.computer_guess:
            print("Too Low")
            return False
        elif user_guess > self.computer_guess:
            print("Too High")
            return False
        else:
            
            print(f"Correct! The current score is {self.score}")
            self.score += 1
            return True


    def main_game(self):
        solved = False

        while not solved:
            user_guess = self.user_input()

            solved = self.game_test(user_guess)

current_game = GuessingGame(1,50)

current_game.main_game()
