from tkinter import *

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self):
        #Windo
        self.window = Tk()
        self.window.title("Quizzler", )
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        #Score Label
        self.score_label = Label(text="score: ", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        #Canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        #True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, padx=20, pady=20)
        self.true_button.grid(row=2, column=0)
        #False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
