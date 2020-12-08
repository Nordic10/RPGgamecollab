import pygame
import star_creator
import sky_creator

pygame.init()


#camera = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
camera = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The 10th Realm")
pygame.display.set_icon(pygame.image.load("thor.png"))

timer = pygame.time.Clock()

x = 50
y = 50
width = 40
height = 60
vel = 5
counter = 0

def drawer(image, x, y):
    camera.blit(image, (x,y))

run = True
while run:
    # pygame.time.delay(10)
    # counter += 1
    # if counter % 70 == 0:
    #     #print(timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # star_creator.star_creating()
    # sky_creator.moon_creator()
    keys = pygame.key.get_pressed()

    timer.tick

    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel

    camera.fill((0,0,0))
    pygame.draw.rect(camera, (255, 0, 0), (x, y, width, height))

    pygame.display.update()

    if counter % 20 == 0:
        print(timer.get_fps)



pygame.quit()