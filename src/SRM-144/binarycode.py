class BinaryCode:
	def decode(self, message):
		zero_string = self.decode_message(message, 0)
		one_string = self.decode_message(message, 1)

		return(zero_string, one_string)

	def decode_message(self, message, init):

		decode_string = ""
		p0 = init
		q = message[0]
		p1 = int(q) - p0
		decode_string = decode_string + str(p0) + str(p1)

		print(decode_string)

		i = 0
		for i in range(1, len(message) - 1):
			p = int(message[i]) - p0 - p1
			decode_string = decode_string + str(p)
			p0 = p1
			p1 = p


		for character in decode_string:
			if(character != '1' and character != '0'):
				decode_string = "NONE"

		return decode_string