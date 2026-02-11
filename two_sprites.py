import pygame
screen_w=640
screen_h=480
sprite_w=30
sprite_h=30
x,y=30,30
clock=pygame.time.Clock()
screen=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Two Sprites')

done=False

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3
        x=min((max(0,x)), screen_w-sprite_w)
        y=min((max(0,y)), screen_h-sprite_h)
        
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (125, 0, 255), pygame.Rect(x, y, sprite_w, sprite_h))
        pygame.draw.rect(screen,(0,125,255),pygame.Rect(295,215,50,50),11)
        pygame.display.update()
        clock.tick(90)
