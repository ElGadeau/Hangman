class hangman:
	secret_word = "hello"
	guessed_letters = []
	life = 6

	@classmethod
	def secret_word_render(self):
		shown_word = ""

		for letter in self.secret_word:
			if letter in self.guessed_letters:
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