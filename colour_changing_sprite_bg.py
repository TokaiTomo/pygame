import pygame
import random
pygame.init()
sprite_c_event=pygame.USEREVENT+1
bg_c_event=pygame.USEREVENT+2
B=pygame.Color('blue')
LB=pygame.Color('lightblue')
DB=pygame.Color('darkblue')
Y=pygame.Color('yellow')
M=pygame.Color('magenta')
O=pygame.Color('orange')
W=pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width): 
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]= -self.velocity[0]
            boundary_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]= -self.velocity[1]
            boundary_hit=True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_c_event))
            pygame.event.post(pygame.event.Event(bg_c_event))
    def change_color(self):
        self.image.fill(random.choice([W,M,O,Y]))
def change_background_colour():
    global bg_color
    bg_color=random.choice([B,DB,LB])
all_sprites_list=pygame.sprite.Group()
sp1 = Sprite(W, 20, 30)
# Randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Boundary Sprite")
# Set the initial background color
bg_color = B
# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()


while not exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
    elif event.type == sprite_c_event:
      sp1.change_color()
    elif event.type == bg_c_event:
      change_background_colour()

  all_sprites_list.update()
  screen.fill(bg_color)
  all_sprites_list.draw(screen)
  pygame.display.flip()
  clock.tick(2000)
pygame.quit()