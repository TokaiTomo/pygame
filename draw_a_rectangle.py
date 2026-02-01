import pygame
pygame.init()
screen=pygame.display.set_mode((105,105))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,125),pygame.Rect(25,25,55,55),5)
    pygame.display.flip()
