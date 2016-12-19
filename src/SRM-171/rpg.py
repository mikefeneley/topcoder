
class RPG:
    
    def dieRolls(self, dice):
        print(dice)
        minimum = self.calculate_min(dice) 
        maxi = self.calculate_max(dice) 
        average = self.calculate_avg(dice) 
        final = (minimum, maxi, average)
        return final

    def calculate_min(self, dice):
        minimum = 0
        for die in dice:
            div = die.split('d') 
            rolls = int(div[0])
            minimum += rolls
        return minimum

    def calculate_max(self, dice):
        total = 0
        for die in dice:
            div = die.split('d')
            rolls = int(div[0])
            max_val = int(div[1])
            total += (rolls * max_val)
        return total
    
    def calculate_avg(self, dice):
        avg = 0

        for die in dice:
            div = die.split('d')
            rolls = float(div[0])
            val = float(div[1])
            average = rolls *(1 + val) / 2
            avg += average
        return int(avg)
