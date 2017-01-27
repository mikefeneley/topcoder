
class TestTaking:

    def findMax(self, questions, guessed, actual):
        large = 0
        false = questions - actual
        false_guesses = questions - guessed
        false_correct = min(false, false_guesses)
        true_correct = min(guessed, actual)
        total_correct = false_correct + true_correct
        return total_correct
