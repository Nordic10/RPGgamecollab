import pygame
import math

pygame.init()

camera = pygame.display.set_mode((800, 600))

head = [[50, 32], pygame.transform.scale2x(pygame.image.load("images/basecharacter/head.png"))]
body = [[50, 50], pygame.transform.scale2x(pygame.image.load("images/basecharacter/body.png"))]
leg1 = [[153, 87], 0, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallthigh.png")), [53, 100], 0, pygame.transform.scale2x(pygame.image.load("images/basecharacter/shin.png"))]
leg2 = [[53, 87], 0, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallthigh.png")), [53, 100], 0, pygame.transform.scale2x(pygame.image.load("images/basecharacter/shin.png"))]
arm1 = [[41, 48], 315, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallbicep.png")), [54, 70], 270, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallforearm.png"))]
arm2 = [[41, 48], 315, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallbicep.png")), [54, 70], 270, pygame.transform.scale2x(pygame.image.load("images/basecharacter/smallforearm.png"))]

walkcount = 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    camera.fill((255, 255, 255))

    camera.blit(pygame.transform.rotate(arm2[2], arm2[1]), tuple(arm2[0]))
    camera.blit(pygame.transform.rotate(arm2[5], arm2[4]), tuple(arm2[3]))
    camera.blit(pygame.transform.rotate(leg2[2], leg2[1]), tuple(leg2[0]))
    camera.blit(pygame.transform.rotate(leg2[5], leg2[4]), tuple(leg2[3]))
    camera.blit(head[1], tuple(head[0]))
    camera.blit(pygame.transform.rotate(leg1[2], leg1[1]), tuple(leg1[0]))
    camera.blit(pygame.transform.rotate(leg1[5], leg1[4]), tuple(leg1[3]))
    camera.blit(body[1], tuple(body[0]))
    camera.blit(pygame.transform.rotate(arm1[2], arm1[1]), tuple(arm1[0]))
    camera.blit(pygame.transform.rotate(arm1[5], arm1[4]), tuple(arm1[3]))
    camera.
    #camera.blit(pygame.image.load("thor.png"), (50, 50))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        walkcount += 1
        oldleg1position = leg1[0]
        leg1[1] += 1
        print(leg1)
        leg1[0] = oldleg1position
        print(leg1)
        oldleg2position = leg2[0]
        leg2[1] += 1
        leg2[0] = oldleg2position

    if keys[pygame.K_a]:
        walkcount += 1
        leg1[1] -= 1
        leg2[1] -= 1


    pygame.display.update()

pygame.quit()
