from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
timer = None
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dic = original_data.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")

current_card = {}

#words_to_learn = data_dic.to_csv("words_to_lear.csv", index=False)

def generate_word():
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(data_dic)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_text, text=current_card["French"], fill="black")
        canvas.itemconfig(canvas_image, image=card_img)
        flip_timer= window.after(3000, flip_card)

def flip_card():
       canvas.itemconfig(card_title, text="English", fill="white")
       canvas.itemconfig(card_text, text=current_card["English"], fill="white")
       canvas.itemconfig(canvas_image, image=flip_img)


def is_known():

    data_dic.remove(current_card)
    generate_word()
    data2 = pandas.DataFrame(data_dic)
    data2.to_csv("words_to_learn.csv", index=False)
    # f = pandas.DataFrame(known_words)
    # f.to_csv("words_to_learn.csv", index=False)





#------------------------ UI SET UP----------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
flip_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

my_image_x = PhotoImage(file="images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0, command=generate_word)
button_x.grid(column=0, row=1)

my_image_r = PhotoImage(file="images/right.png")
button_r = Button(image=my_image_r, highlightthickness=0, command=is_known)
button_r.grid(column=1, row=1)

generate_word()

#flip_card()
window.mainloop()
