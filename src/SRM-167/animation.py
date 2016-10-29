class Animation:
	def animate(self, speed, init):
		positions = []

		positions.append(init)

		next_pos = ""
		for character in init:
			next_pos += "."

		i = 0
		for thing in range(0, 45):
			last = positions[i]
			
			next_pos = ""
			for character in init:
				next_pos += "."

			j = 0
			while(j < len(last)):
				if last[j] == 'R':
					index = j + speed
					if(index < len(last)):
						next_pos = next_pos[0:index] + 'R' + next_pos[index + 1:len(init)]
				if last[j] == 'L':
					index = j - speed
					if(index >= 0):
						next_pos = next_pos[0:index] + 'L' + next_pos[index + 1:len(init)]
				j += 1
			
			positions.append(next_pos)
			i += 1
			if(not 'R' in next_pos and not 'L' in next_pos):
				k = 0
				for k in range(0, len(positions)):
					string = positions[k]
					string = string.replace('L', 'X')
					string =string.replace('R', 'X')
					positions[k] = string
				print(positions)
				return positions



if __name__== "__main__":
	animator = Animation()
	animator.animate(2, "LRLR.LRLR")