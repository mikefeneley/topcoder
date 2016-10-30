class FormatAmt:
	def amount(self, dollars, cents):
		bill = ""
		if(dollars < 1):
			bill += "0"
		else:
			dollars = str(dollars)
			i = 0
			while i < len(dollars) / 3:
				bill = ',' + dollars[len(dollars) - (i + 1) * 3: len(dollars) - i * 3] + bill
				i += 1
			bill = dollars[0: len(dollars) - i * 3] + bill
			if(bill[0] == ','):
				bill = bill[1:len(bill) +1]

		bill = '$' + bill + '.'

		if(cents == 0):
			bill = bill + '00'
		elif(cents < 10):
			bill = bill + '0' + str(cents)
		else:
			bill = bill + str(cents)

		return bill
