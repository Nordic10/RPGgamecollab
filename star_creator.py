import test
import pygame
import random

stars = []

# new_camera = test.camera

class star:
    def __init__(self, xposition, yposition, size):
        self.xposition = xposition
        self.yposition = yposition
        self.size = size

def star_creating():
    if random.randint(40, 50) == 42 and len(stars) <= 100:
        stars.append(star(random.randint(-100, 1000), random.randint(-100, 1000), random.randint(1, 15)))
    marked_for_death = []
    for i in range(len(stars)):
        increase = random.randint(41, 43)
        if increase == 42 and stars[i].size < 15:
            stars[i].size += 1
        elif increase != 42:
            stars[i].size -= 1
            if stars[i].size == 0:
                marked_for_death.append(i)
    for i in marked_for_death:
        del(stars[i])
    for each in stars:
        if each.size == 0 or each.size == 16:
            print("will break")
        # test.drawer(pygame.image.load("images/stars/star1.png"), (100, 100))
        # new_camera.blit(pygame.image.load("images/stars/star1.png"), (100, 100))
        # test.camera.blit(pygame.transform.scale(pygame.image.load("images/stars/star" + str(each.size) + ".png"), (32, 32)), (each.xposition, each.yposition))

