# Game : guess number : [lower_bound, upper_bound max_attempt
import random as _rd

class Game:
    def __init__(self, lower_bound, upper_bound, max_attempt):
        self.lower_bound    = lower_bound 
        self.upper_bound    = upper_bound
        self.max_attempt    = max_attempt
        self.secret_number  = _rd.randint(lower_bound, upper_bound)
        self.attempt_left   = max_attempt 
        self.msg("Init Game")

    def result(self):
        self.msg(f"Game result {self.secret_number}")

    def msg(self, msg):
        print('==',msg,"==")

    def guess(self, player_guess):
        if player_guess < self.secret_number:
            return "Too low"
        elif player_guess > self.secret_number:
            return "Too high"
        else:
            return "Congratulations! You guessed the number."

    def chek_guess(self, player_guess):
        rslt = self.guess(player_guess)
        self.msg(rslt)
        if rslt == "Congratulations! You guessed the number.":
            self.msg(rslt)
            return True
        return False


    def play(self):
        self.msg("Welcome GUESS NUMBER")
        self.msg(f"Guess between [{self.lower_bound} , {self.upper_bound}]. You have {self.max_attempt} attempts.")
    
        while self.attempt_left > 0:
            self.msg(f"Attempt left: {self.attempt_left}")
            player_guess = int(input("Enter your guess: "))
            if self.chek_guess(player_guess):
                break
            self.attempt_left -= 1
        if self.attempt_left == 0:
            self.msg("You've run out of attempts. The secret number was: {}".format(self.secret_number))