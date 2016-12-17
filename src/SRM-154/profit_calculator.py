class ProfitCalculator:
    
    def percent(self, items):
        i = 0

        total_cost = 0
        total_profit = 0

        for item in items:
            item_split = item.split(" ")
            cost = item_split[0]
            profit = item_split[1]

            total_cost += float(cost)
            total_profit += float(profit)
        print(total_profit, total_cost) 
        margin = int((total_cost - total_profit)/total_cost * 100)
        return margin