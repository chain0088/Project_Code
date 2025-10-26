import pygame
import movement as m
import object_data as ojd
import enemy_take_damage as etd
import game_time as gt

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

fps = 60
clock = pygame.time.Clock()

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    m.move()

    screen.blit(ojd.pixel,ojd.pixel_rect)
    screen.blit(ojd.test2,ojd.test_rect2)
    screen.blit(ojd.test,ojd.test_rect)

    etd.enemy_td()
    gt.timer()
    
    pygame.display.update()
    clock.tick(fps)
pygame.quit()