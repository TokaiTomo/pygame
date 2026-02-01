import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((50,255,125))
c=(0,125,125)
pygame.draw.circle(window,c,(50,50),50)
pygame.draw.circle(window,c,(50,350),50)
pygame.draw.circle(window,c,(350,50),50,3)
pygame.draw.circle(window,c,(350,350),50,3)
pygame.display.update()
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.display.flip()
