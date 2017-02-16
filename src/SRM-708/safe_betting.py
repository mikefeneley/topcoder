
class SafeBetting:

    def minRounds(self, a, b, c):
        minimum = a
        earnings = b
        bets = 0
        while True:
            if earnings >= c:
                return bets
            bet_amount = earnings - a
            earnings += bet_amount
            bets += 1
