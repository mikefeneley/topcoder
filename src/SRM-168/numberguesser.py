class NumberGuesser:
	def guess(self, leftOver):
		nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
		length = len(num)
		for number in nums:
   			for position in range(length + 1):
				test = num[0:position] + number + num[position:length]
				if(self.check(int(test))):
					return number		
            		
	def check(self, num):
		for digits in range(1, 9999):
			if(digits < 10):
				digits = '000' + str(digits) 
			elif(digits < 100):
				digits = '00' + str(digits)
			elif(digits < 1000):
				digits = '0' + str(digits)
			else:
				digits = str(digits)
		  first = [] 
      second =[] 
        
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(0, 4):
                    for l in range(0, 4):
                        if i != j and i != k and i != l and j != k and j != l and k != l: 
                            first.append(int(digits[i] + digits[j] + digits[k] + digits[l]))
                            second.append(int(digits[i] + digits[j] + digits[k] + digits[l]))
            
        for comb1 in first:
            for comb2 in second:
                val = abs(comb1 - comb2)
                if(val == num):
                    return True
		return False
