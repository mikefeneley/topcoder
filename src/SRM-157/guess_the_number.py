class GuessTheNumber:

    def noGuesses(self, upper, answer):
        lower = 1
        guesses = 0

        while(1):
            guesses += 1
            x = (upper + lower)/2
            if(x < answer):
                lower = x + 1
            if(x > answer):
                upper = x - 1
            if(x == answer):
                return guesses
