# coding:utf-8

import time
import pygame

timme = input("The time > ")

def start(ti):
    print("The timer's starting(Use Ctrl-C to stop).")
    start_time = time.perf_counter()
    try:

     while True:
        next_time = time.perf_counter()

        if int(next_time) - int(start_time)  == int(ti):
            print("Finish!")
            print("Ctrl-C to Quit")


            pygame.mixer.init()
            music = pygame.mixer.Sound("sound.mp3")
            
            music.play(-1)

    except KeyboardInterrupt:
       print("Already exited.")
    
start(timme)
