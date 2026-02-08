import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,125),pygame.Rect(320,240,50,50),5)
    pygame.display.flip()