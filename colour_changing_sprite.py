import pygame
def main():
    pygame.init()
    screen_w,screen_h=500,500
    screen=pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption('COLOUR CHANGING SPRITE ⚽️')
    colors = {'red':pygame.Color('red'),
              'blue':pygame.Color('blue'),
              'green':pygame.Color('green'),
              'yellow':pygame.Color('yellow'),
              'white':pygame.Color('white')}
    current_color=colors['white']
    x,y=30,30
    sprite_w,sprite_h=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: x-=3
        if pressed[pygame.K_DOWN]: x+=3
        x=min((max(0,x)), screen_w-screen_h)
        y=min((max(0,y)), screen_w-screen_h)
        if x==0: current_color=colors['blue']
        elif x == screen_w-screen_w: current_color=colors['yellow']
        elif y==0: current_color=colors['red']
        elif x == screen_h-screen_h: current_color=colors['green']
        else:
            current_color=colors['white']
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,
                         (x,y,sprite_w,sprite_h))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=='__main__':
    main()