class MostProfitable:
    def bestItem(self, costs, prices, sales, items):
		

        cost = costs[0]
        price = prices[0]
        sale = sales[0]
        max_profit = (price - cost) * sales
        index = 0

        for i in range(0, len(costs) - 1):
            cost = costs[i]
            price = prices[i]
            sale = sales[i]

            profit = (price - cost) * sales

            if(profit > max_profit):
                index = 1
        return items[index]