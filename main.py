from tkinter import *
import time
import math
# --------------------CONSTANTS-----------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------TIME RESET--------------------------------------------#

def reset_timer():
    window.after_cancel(timer)
    click_label.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    Long_break_sec = LONG_BREAK_MIN*60
    if rep % 8 == 0:  # rep==1 or rep == 3 or rep==5 or rep==7
        title_label.config(text="Long Break", fg=RED)
        count_down(Long_break_sec)
    elif rep % 2 == 0 and rep != 8:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    # count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    print(count)
    minute_count = math.floor(count/60)
    second_count = count % 60
    if minute_count < 10:
        minute_count = f"0{minute_count}"
    if second_count == 0:
        second_count = f"0{second_count}"
        # second_count="00"
    elif second_count < 10:
        second_count = "0"+str(second_count)

    canvas.itemconfig(timer_text, text=f"{minute_count}:{second_count}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(rep/2)
        for _ in range(work_sessions):
            mark+="🐓"
        click_label.connfig(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

#to create a space for  a image in tkinter than overlap the image on it
#highlightthickness is used to eliminate the border highlight
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

click_label = Label(text="", bg=YELLOW, fg=GREEN)
click_label.grid(column=1, row=3)

window.mainloop()
