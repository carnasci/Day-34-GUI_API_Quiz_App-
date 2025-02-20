from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        #QuizBrain
        self.quiz = quiz_brain
        #Windo
        self.window = Tk()
        self.window.title("Quizzler", )
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        #Score Label
        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        #Canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        #True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, padx=20, pady=20, command=self.answer_is_true)
        self.true_button.grid(row=2, column=0)
        #False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, padx=20, pady=20, command=self.answer_is_false)
        self.false_button.grid(row=2, column=1)
        #Render the quiz question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """fetches next question from quizbrain and displays it onto the canvas"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_is_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_is_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
