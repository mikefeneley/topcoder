class DivisorDigits:
	def howMany(self, number):
		total = 0
		holder = str(number)
		number = int(number)
		for character in holder:
			value = int(character)

			if(value == 0):
				pass
			elif((number % value) == 0):
				total += 1
		return total