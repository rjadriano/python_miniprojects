import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
timer = None
word_key = 0
data = {}
# -------------------------------- DATA -------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    french_words = data["French"].to_dict()
    english_words = data["English"].to_dict()
# ---------------------------- BUTTON FUNCTIONS -----------------------
def right_clicked():
    # Update Word list
    french_words.pop(word_key)
    english_words.pop(word_key)

    words_data = {
        "French" : french_words,
        "English" : english_words
    }
    # Save Word List
    words_to_learn_data = pandas.DataFrame(words_data)
    words_to_learn_data.to_csv("data/words_to_learn.csv")

    next_card()

def next_card():
    global word_key,flip_timer
    window.after_cancel(flip_timer)
    word_key = random.choice(list(french_words.keys()))

    # To French
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_lang,text="French",fill="black")
    canvas.itemconfig(card_word,text=french_words[word_key],fill="black")
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    """Change Card every three seconds"""
    global word_key
    # To English
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_lang,text="English",fill="white")
    canvas.itemconfig(card_word,text=english_words[word_key],fill="white")

# ----------------------------- UI SETUP ------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

# Card Image
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=front_image)

# Card Text
card_lang = canvas.create_text(400,150,font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,font=("Ariel",60,"bold"))

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_btn = Button(image=right_img,highlightthickness=0,command=right_clicked)
wrong_btn = Button(image=wrong_img,highlightthickness=0,command=next_card)

# Widget Call
canvas.grid(column=0,row=0,columnspan=2)

wrong_btn.grid(column=0,row=1)
right_btn.grid(column=1,row=1)

next_card()

window.mainloop()
