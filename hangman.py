class hangman:
	secret_word = ""
	guessed_letters = []
	life = 6

	@classmethod
	def secret_word_render(self):
		shown_word = ""

		for letter in self.secret_word:
			if letter in self.guessed_letters or letter == " ":
				shown_word += letter
			else:
				shown_word += "_"

		return shown_word

	@classmethod
	def guess_letter(self, letter):
		if len(letter) != 1:
			return 0

		if letter in self.guessed_letters:
			return 0
		elif letter in self.secret_word:
			self.guessed_letters.append(letter)
			return 0
		else:
			self.guessed_letters.append(letter)
			return -1

		print(self.guessed_letters)


	@classmethod
	def update_values(self, letter):
		self.life += self.guess_letter(letter)
		return self.check_win_condition()

	@classmethod
	def check_win_condition(self):	
	    letter_found = False

	    for letter in self.secret_word:
	        if letter in self.guessed_letters or letter == " ":
	            letter_found = True
	        else:
	            letter_found = False
	            return letter_found

	    return letter_found

	@classmethod
	def register_secret_word(self, word):
		self.secret_word = word

	@classmethod
	def get_secret_word(self):
		return self.secret_word