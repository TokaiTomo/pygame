import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
screen.fill((255,255,255))
done=False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    

    pygame.draw.rect(screen,(0,125,255),pygame.Rect(295,215,50,50),5)
    pygame.display.flip()
    font = pygame.font.Font(None, 36)
    text = font.render("Elements", True, pygame.Color("black"))
    text_rect = text.get_rect(
        center=(640 // 2, 480 // 2 + 110)
    )
    screen.blit(text, text_rect)
pygame.display.update()
