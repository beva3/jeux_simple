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
    
    def msg(self, msg):
        print('==',msg,"==")

    def guess(self, player_guess):
        if player_guess < self.secret_number:
            return "Too low"
        elif player_guess > self.secret_number:
            return "Too high"
        else:
            return "Congratulations! You guessed the number."
