import pygame
import time

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

clock =pygame.time.Clock()
start_time = time.time()
pass_time = 0

def timer(pass_time):
    font = pygame.font.SysFont("arial",30)
    time_text = font.render(f"{(round(pass_time))//60}:{(round(pass_time))%60}", True,(0,0,0))
    screen.blit(time_text,(10,10))

run = True
while run:
    clock.tick(60)
    pass_time = time.time() - start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    screen.fill((255,255,255))
    timer(pass_time)
    pygame.display.update()

pygame.quit()
