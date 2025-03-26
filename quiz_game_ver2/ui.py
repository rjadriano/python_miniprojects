from functools import partial
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Score Label
        self.score_label = Label(text="Score : 0",fg="white",font=(FONT_NAME,10,'normal'),bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        # Question Canvas
        self.canvas = Canvas(width=300,height=300,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            150,
            width=280,
            text="Question",
            font=(FONT_NAME, 20, "italic")
        )
        self.canvas.grid(column=0,columnspan=2,row=1,pady=30)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img,highlightthickness=0,command=partial(self.clicked_answer,"True"))
        self.true_btn.grid(column=0,row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img,highlightthickness=0,command=partial(self.clicked_answer,"False"))
        self.false_btn.grid(column=1,row=2)

        self.get_next_question()
        self.window.mainloop()

    def clicked_answer(self,answer):
        self.give_feedback(self.quiz.check_answer(answer))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You Scored : {self.quiz.score}/{len(self.quiz.question_list)}")
            # Deactivate Button
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def give_feedback(self,is_right):
        color = "green" if is_right else "red"

        self.canvas.config(bg=color)
        self.score_label["text"] = f"Score: {self.quiz.score}"
        self.window.after(1000,self.get_next_question)
