import time
import pygame
from alive_progress import alive_bar

ti = int(input("The time > "))

try:

    with alive_bar(ti) as bar:
        for item in range(ti):  # 遍历任务

            time.sleep(1)
            bar()
    print("Finish! Time is at youself!")
    while True:
        pygame.mixer.init()
        sound = pygame.mixer.Sound("sound.mp3")
        sound.play(-1)

except KeyboardInterrupt:
    print("Bye!")
