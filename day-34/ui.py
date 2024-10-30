from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = 'Arial'
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.scoreLabel = Label(text="Score: 0",bg=THEME_COLOR,fg='white', font=(FONT_NAME,16,'normal'))
        self.scoreLabel.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, width=280,text='teste', fill=THEME_COLOR, font=(FONT_NAME,20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        right = PhotoImage(file='day-34/images/true.png')
        wrong = PhotoImage(file='day-34/images/false.png')

        self.button_right = Button(image=right,highlightthickness=0, command=self.click_right)
        self.button_right.grid(row=3,column=0)
        self.button_wrong = Button(image=wrong,highlightthickness=0, command=self.click_wrong)
        self.button_wrong.grid(row=3,column=1)

        self.get_next_question()
        ##
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz!')
            self.button_right.config(state=DISABLED)
            self.button_wrong.config(state=DISABLED)

    def click_right(self):
        answer = self.quiz.check_answer('True')
        self.give_feedback(answer)
        

    def click_wrong(self):
        answer = self.quiz.check_answer('False')
        self.give_feedback(answer)

    def give_feedback(self,is_right):
        if is_right:
            bg = 'green'
        else:
            bg = 'red'
        self.canvas.config(bg=bg)
        self.scoreLabel['text'] = f"score: {self.quiz.score}"
        self.window.after(2000,self.get_next_question)