
class BettingMoney:

    def moneyMade(self, amounts, centsPerDollar, finalResult):

        winnings = 0
        payout = 0
        for idx, money in enumerate(amounts):
            if(idx != finalResult):
                winnings += money
            else:
                payout = money * float(centsPerDollar[idx]) / 100
        winnings = winnings * 100
        payout = payout * 100
        net = winnings - payout
        return net
