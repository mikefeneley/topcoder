class CCipher:
	def decode(self, cipherText, shift):
		decode_txt = ""
		for char in cipherText:
			new = chr(ord(char) - shift)
			
			if(new < 'A'):
				new = chr(ord(new) + ord('Z') - ord('A') + 1)

			decode_txt = decode_txt + new
		return decode_txt

