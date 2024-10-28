from tkinter import *
import pandas 
import random

BG_COLOR = '#B1DDC6'
FONT_NAME = 'Ariel'

TIMER_REF = None
SELECTED_INDEX = 0

def pick_word():
    global TIMER_REF
    global SELECTED_INDEX
    if TIMER_REF is not None:
        window.after_cancel(TIMER_REF)

    SELECTED_INDEX = random.randint(0,len(words)-1)

    canva.itemconfig(canvas_image, image=card_front)
    canva.itemconfig(language_text, text="French", fill='black')
    canva.itemconfig(word_text, text=f"{words[SELECTED_INDEX]['French']}", fill='black')

    TIMER_REF = window.after(3000,show_answer)
  
def show_answer():
    canva.itemconfig(canvas_image, image=card_back)
    canva.itemconfig(language_text, text="English", fill='white')
    canva.itemconfig(word_text, text=f"{words[SELECTED_INDEX]['English']}", fill='white')

def got_right():
    words.pop(SELECTED_INDEX)

    new_dataframe = pandas.DataFrame(words)

    new_dataframe.to_csv('day-31/words_to_learn.csv',index=False)

    pick_word()

data = pandas.read_csv('day-31/data/french_words.csv')

words = data.to_dict(orient='records')

window = Tk()
window.title('Flashy')
window.config(padx=50,pady=50, bg=BG_COLOR)

# Images
card_front = PhotoImage(file='day-31/images/card_front.png')
card_back = PhotoImage(file='day-31/images/card_back.png')
right = PhotoImage(file='day-31/images/right.png')
wrong = PhotoImage(file='day-31/images/wrong.png')

canva = Canvas()

canva = Canvas(width=800, height=526,highlightthickness=0, bg=BG_COLOR)
canvas_image = canva.create_image(400,263,image=card_front)
language_text = canva.create_text(400,150, text='french', fill='black',font=(FONT_NAME,40,'italic'))
word_text = canva.create_text(400,263, text='', fill='black',font=(FONT_NAME,60,'bold'))
canva.grid(row=0,column=0,columnspan=2)

button_right = Button(image=right,highlightthickness=0, command=got_right)
button_right.grid(row=1,column=0)
button_wrong = Button(image=wrong,highlightthickness=0, command=pick_word)
button_wrong.grid(row=1,column=1)

pick_word()

window.mainloop()