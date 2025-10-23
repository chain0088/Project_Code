import pygame
import time


pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

test = pygame.image.load("test.png")
test = pygame.transform.scale(test,(50,50))
test_rect = test.get_rect()
bullet = pygame.image.load("bullet.png")
bullet_rect = bullet.get_rect()

fps = 60
clock = pygame.time.Clock()
start_time = time.time()
pass_time = 0
speed = 3

run=True
while run:
    pass_time = time.time() - start_time
    font = pygame.font.SysFont("comicsans",30)
    time_text = font.render(f"Time: {round(pass_time)}", 1, (255,0,0))
    screen.blit(time_text,(750,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and (test_rect.y > 0):
        test_rect.y -= speed
    if key[pygame.K_a] and (test_rect.x > 0):
        test_rect.x -= speed
    if key[pygame.K_s] and (test_rect.y < 550):
        test_rect.y += speed
    if key[pygame.K_d] and (test_rect.x < 750):
        test_rect.x += speed
    screen.fill((255,255,255))
    screen.blit(test,test_rect)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()