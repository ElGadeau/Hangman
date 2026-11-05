from tkinter import *
from tkinter import ttk

from hangman import hangman

def submit_letter(letter):
	hangman.update_values(letter)
	update_lables()

def update_lables():
	secret_word.config(text=hangman.secret_word_render())
	guessed_letters.config(text=hangman.guessed_letters)
	life.config(text=hangman.life)

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

secret_word = ttk.Label(frm, text=hangman.secret_word_render())
guessed_letters = ttk.Label(frm, text=hangman.guessed_letters)
life = ttk.Label(frm, text=hangman.life)

button = ttk.Button(frm, text="Quit!", command=root.destroy)

entry = ttk.Entry(frm)
entry.bind("<Return>", lambda e: submit_letter(entry.get()))

secret_word.grid(column=0, row=0)
button.grid(column=1, row=2)
entry.grid(column=1, row=0)
guessed_letters.grid(column=1, row=1)
life.grid(column=0, row=1)

root.mainloop()

