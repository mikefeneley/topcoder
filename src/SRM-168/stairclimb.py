class StairClimb:
	def stridesTaken(self, flights, stairsPerStride):
		total_strides = 0
		for flight in flights:
			leftover = flight % stairsPerStride
			strides = flight / stairsPerStride
			if(leftover > 0):
				strides += 1
			total_strides += 2			
			total_strides += strides 
		
		total_strides -= 2 #Remove top level change
		return total_strides
