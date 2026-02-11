import pygame
import sys
import os

pygame.init()
pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background image")

# ALWAYS points to the folder of this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load images using BASE_DIR
background_image = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "Antarctica.png")).convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "penguin.png")).convert_alpha(),
    (120, 200)
)

penguin_rect = penguin_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
)

font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, pygame.Color("black"))
text_rect = text.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)
)

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
