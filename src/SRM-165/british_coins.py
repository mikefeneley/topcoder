
class BritishCoins:

    def coins(self, pence):
    
        pence_per_pound = 12 * 20
        pence_per_shilling = 12

        pounds = pence / pence_per_pound
        shilling = (pence - (pounds * pence_per_pound)) / pence_per_shilling
        pen = pence - (pounds * pence_per_pound) - (shilling * pence_per_shilling)

        return (pounds, shilling, pen)
