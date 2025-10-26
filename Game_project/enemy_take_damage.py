import pygame
import object_data as ojd
import movement as m

count = 0
damage = 20
damage_time = 0
screen = pygame.display.set_mode((800, 600))

def enemy_td():
    global count
    global damage
    global damage_time
    if count >= 5:
        ojd.test2.fill(0)

    if ojd.test_rect.colliderect(ojd.test_rect2) and (count < 5) and (damage_time <= 10):
        pygame.draw.rect(screen, (255,0,0), (ojd.test_rect2.x,ojd.test_rect2.y,100,100))
        damage_time += 1

    if ojd.test_rect.colliderect(ojd.test_rect2) and (count < 5) and (damage_time >= 10):
        m.move_object1()
        count += 1
        damage_time = 0
    
    pygame.draw.rect(screen, (0,255,0), (ojd.test_rect2.x,ojd.test_rect2.y+120,100-(damage*count),20))