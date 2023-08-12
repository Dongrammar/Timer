from tkinter import *
import pygame as pg
import ttkbootstrap as ttk

# 定义按钮函数
def clicked():
    tip['text'] = "The timer's running!"
    tip['fg'] = 'red'

    time_input.pack_forget()   #隐藏输入框和开始按钮
    btn.pack_forget()
    
    return time_counter()

def time_counter():
    global nt
    nt += 1
    n_time['text'] = str(nt)
    if nt < int(user_time.get()):
        n_time.after(1000, time_counter)
    else:
        return ring()

# 定义显示按钮函数
def show_btn():
    time_input.pack()
    btn.pack()
    
    tip["fg"] = 'black'
    tip["text"] = "Please input \n your time\n(Unit:s) :"

    n_time['text'] = '0'
    global nt
    nt = 0

def ring():
    global ring_btn
    ring_btn = ttk.Button(window, text="Stop", command=stop_ring, style='default-outline')
    ring_btn.pack()
    
    pg.mixer.init()
    global music
    music = pg.mixer.Sound("sound.mp3")
    music.play(-1)

def stop_ring():
    music.stop()
    ring_btn.pack_forget()
    return show_btn()


window = ttk.Window(themename="lumen")
window.title("Timer")
window.geometry("300x230")
nt = 0


n_time = Label(window, text="0", font=("Jetbrains Mono", 20))
n_time.pack()
tip = Label(window, text="Please input \n your time\n(Unit:s) :", font=("Microsoft JhengHei", 15))
tip.pack()

user_time = StringVar()
time_input = Entry(window, width=20, textvariable=user_time)
time_input.pack()



btn_text = StringVar()
btn = ttk.Button(window, command=clicked, textvariable=btn_text, style="primary-ouline")
btn_text.set("Start")
btn.pack()


window.mainloop()