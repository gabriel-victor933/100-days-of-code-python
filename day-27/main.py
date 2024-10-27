from tkinter import *

CONVERTION_RATE = 1.60934

def convert():
    try: 
        invalidInput['text'] = ''
        miles = float(input.get())
        kilometers = CONVERTION_RATE*miles
        answer['text'] = kilometers
    except ValueError:
        invalidInput['text'] = 'Entry must be a valid number!'

    

window = Tk()
window.title("My first GUI program")
window.minsize(width=360,height=120)
window.config(padx=20,pady=20)


input = Entry()
input.grid(row=0,column=1)

labelInput = Label(text='Miles')
labelInput.grid(row=0,column=2)

labelAnswer = Label(text='is equal to')
labelAnswer.grid(row=1,column=0)

answer = Label(text='0')
answer.grid(row=1,column=1)

labelKm = Label(text='Km')
labelKm.grid(row=1,column=2)

button = Button(text='Calculate',command=convert)
button.grid(row=2,column=1)

invalidInput = Label(text='')
invalidInput.grid(row=3,column=1)

window.mainloop()