from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = '✔'
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    icon['text'] = ''
    window.after_cancel(timer)
    title['text'] = 'Timer'
    title['fg'] = GREEN
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title['text'] = 'Break'
        title['fg'] = RED
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        title['text'] = 'Break'
        title['fg'] = PINK
    elif reps % 2 != 0:
        count_down(WORK_MIN*60)
        title['text'] = 'Work'
        title['fg'] = GREEN

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    seconds = count%60
    minutes = math.floor(count/60)

    if seconds < 10:
        seconds = "0" + str(seconds)

    if minutes < 10:
        minutes = "0" + str(minutes)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else: 
        start_timer()
        work_sections = math.floor(reps/2)
        icon['text'] = checkmark*work_sections


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=70,bg=YELLOW)


def saysomething(*args):
    print(args)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='day-28/tomato.png')
canvas.create_image(101,112,image=tomato_img)
timer_text = canvas.create_text(101,130, text='0', fill='white',font=(FONT_NAME,32,'bold'))
canvas.grid(row=1,column=1)

title = Label(text='Timer',fg=GREEN,font=(FONT_NAME,48,'normal'),bg=YELLOW)
title.grid(row=0,column=1)

startButton = Button(text='Start', highlightthickness=0,command=start_timer)
startButton.grid(row=2,column=0)

ResetButton = Button(text='Reset', highlightthickness=0, command=reset_timer)
ResetButton.grid(row=2,column=2)

icon = Label(fg=GREEN,font=(FONT_NAME,24,'normal'), bg=YELLOW)
icon.grid(row=3,column=1)

window.mainloop()

