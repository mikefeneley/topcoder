class MineField:
	def getMineField(self, mineLocations):
		board = [
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0'],
				['0', '0', '0', '0', '0', '0', '0', '0', '0']
				]

		locations = mineLocations.split(')')
		locations = locations[0:len(locations) - 1]
		
		for location in locations:
			x = int(location[1])
			y = int(location[3])
			board[x][y] = 'M' 		

		for i in range(0, 9):
			for j in range(0, 9):
				if(board[i][j] == '0'):
					total_mines = 0
					
					for k in range (-1, 2):
						for l in range(-1, 2):
							x_index = k + i
							y_index = l + j

							if(x_index < 9 and x_index >= 0 and y_index >= 0 and y_index < 9):
								if(board[x_index][y_index] == 'M'):
									total_mines += 1

					if(total_mines > 0):
						board[i][j] = str(total_mines)

		final_board = set()				
		strings = []

		for i in range(0, 9):
			string = ""
			for j in range(0, 9):
				string = string + board[i][j]
			strings.append(string)
		final_board = (this)
		return final_board
