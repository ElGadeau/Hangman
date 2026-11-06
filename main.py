from tkinter import *
from tkinter import ttk

from hangman import hangman

def submit_letter(letter):
	did_win = hangman.update_values(letter)
	if did_win:
		end_message.config(text="YOU WON!")
		word.config(text="The word was: " + hangman.get_secret_word())
		show_end()
	elif hangman.life <= 0:
		end_message.config(text="YOU LOST!")
		word.config(text="The word was: " + hangman.get_secret_word())
		show_end()
	else:
		update_labels()

def update_labels():
	secret_word.config(text=hangman.secret_word_render())
	guessed_letters.config(text=hangman.guessed_letters)
	life.config(text=hangman.life)
	entry.delete(0, END)

def show_word_entry():
	secret_word.grid_remove()
	entry.grid_remove()
	guessed_letters.grid_remove()
	life.grid_remove()
	end_message.grid_remove()
	word.grid_remove()

	secret_word_entry.grid()

def show_game():
	secret_word_entry.grid_remove()
	end_message.grid_remove()
	word.grid_remove()

	secret_word.grid()
	entry.grid()
	guessed_letters.grid()
	life.grid()

	update_labels()

def show_end():
	secret_word.grid_remove()
	entry.grid_remove()
	guessed_letters.grid_remove()
	life.grid_remove()
	secret_word_entry.grid_remove()

	end_message.grid()
	word.grid()

def submit_secret_word(word):
	hangman.register_secret_word(word)
	show_game()

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

secret_word = ttk.Label(frm, text=hangman.secret_word_render())
guessed_letters = ttk.Label(frm, text=hangman.guessed_letters)
life = ttk.Label(frm, text=hangman.life)
end_message = ttk.Label(frm)
word = ttk.Label(frm)

button = ttk.Button(frm, text="Quit!", command=root.destroy)

secret_word_entry = ttk.Entry(frm)
entry = ttk.Entry(frm)
secret_word_entry.bind("<Return>", lambda e: submit_secret_word(secret_word_entry.get()))
entry.bind("<Return>", lambda e: submit_letter(entry.get()))


secret_word.grid(column=0, row=0)
secret_word_entry.grid(column=0, row=0)
end_message.grid(column=0, row=0)
word.grid(column=0, row=1)
button.grid(column=1, row=2)
entry.grid(column=1, row=0)
guessed_letters.grid(column=1, row=1)
life.grid(column=0, row=1)

show_word_entry()

root.mainloop()