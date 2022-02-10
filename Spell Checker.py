import tkinter as tk
from textblob import TextBlob

window = tk.Tk()
window.title("Spell Checker")
window.geometry("700x400")
window.config(background="#dae6f6")

def check_spelling():
    word = entry.get()
    text = TextBlob(word)
    right = str(text.correct())
    labels = tk.Label(window, text="Correct Spelling : ", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    labels.place(x=180, y=250)
    spell.config(text=right)

label = tk.Label(window, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
label.pack(pady=(50, 0))

entry = tk.Entry(window, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
entry.pack(pady=10)
entry.focus()

button = tk.Button(window, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

spell = tk.Label(window, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=400, y=250)

window.mainloop()
