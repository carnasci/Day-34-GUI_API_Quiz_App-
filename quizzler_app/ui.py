from tkinter import *

THEME_COLOR = "#375362"
TRUE_IMAGE = PhotoImage(file="images/true.png")
FALSE_IMAGE = PhotoImage(file="images/false.png")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text="score: ")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.true_button = Button(image=TRUE_IMAGE)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=FALSE_IMAGE)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
