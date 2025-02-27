import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "\u2713"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_click():
    global reps
    reps = 0
    window.after_cancel(timer)

    timer_label.config(text="Timer", fg="#000000")
    check_label.config(text='')
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 1:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break",fg=PINK)
    elif reps % 2 == 0:
        count_down(WORK_MIN*60)
        timer_label.config(text="Work",fg=GREEN)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = f"0{math.floor(count / 60)}" if math.floor(count / 60) < 10 else math.floor(count / 60)
    count_sec = f"0{count % 60}" if count % 60 < 10 else count % 60

    time = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text,text=time)
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        if reps < 9:
            start_timer()
            if reps % 2 == 0:
                # Add Check Mark for every work
                check = ''
                for rep in range(reps):
                    check += CHECK_MARK
                check_label.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
# Tomato - Image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

# Tomato - Text
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

# Label
timer_label = Label(text="Timer",font=(FONT_NAME,45,'bold'),bg=YELLOW)
check_label = Label(font=(FONT_NAME,20),bg=YELLOW)

# Button
start_btn = Button(text="Start",command=start_timer)
reset_btn = Button(text="Reset",command=reset_click)

# Widget - Call
canvas.grid(column=1,row=1)
timer_label.grid(column=1,row=0)

start_btn.grid(column=0,row=2)
reset_btn.grid(column=2,row=2)

check_label.grid(column=1,row=3)

window.mainloop()
