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

        dive = float(next_time) - float(start_time)
        print('\r', round(dive, 3), end='', flush=True)

        if int(dive)  == int(ti):
            break

     print("\nFinish!")
     print("Press Ctrl-C to Quit")


     while True:
        pygame.mixer.init()
        music = pygame.mixer.Sound("sound.mp3")
            
        music.play(-1)

    except KeyboardInterrupt:
       print("Already exited.")
    
start(timme)
