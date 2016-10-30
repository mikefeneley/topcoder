class Bonuses:
	def getDivision(self, points):
		total = 0
		for point in points:
			total += point

		fractions = []

		for point in points:
			fractions.append(int(100 * point / total))


		leftover = 100 - sum(fractions)
		print(leftover)
		
		max_value = max(fractions)
		max_index = fractions.index(max_value)
		print(fractions)

		print(max_value, max_index)

		while(leftover > 0):
			leftover -= 1
			fractions[max_index] += 1

			if(leftover > 0):
				max_val = 0
				index = 0
				i = 0
				for idx, value in enumerate(fractions):
					if((value == max_value and idx > max_index)):
						max_value = value
						max_index = index
						break
					else:
						if(value > max_val and value < max_value):
							max_val = value
							index = idx
				max_value = max_val			
				max_index = index
		return fractions