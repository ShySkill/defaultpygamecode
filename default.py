import pygame
import math
import os


WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Default Game")

YELLOW = (255 , 255 , 0)
RED = (255 , 0 , 0)
COLORET = (255,255,255)

SKY_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.abspath('sky.jpg')),  (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(SKY_IMAGE, (0,0))
    pygame.display.update()


clock = pygame.time.Clock()
def main():
    clock.tick(FPS)
    run = True
    while run:
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    draw_window()
    main()

if __name__ == "__main__":
    main()
