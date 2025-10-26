import pygame
import random
import object_data as ojd


enemy_speed = 3
back_ground = 1

def move():
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        ojd.test_rect2.y += enemy_speed
        ojd.pixel_rect.y += back_ground 
    if key[pygame.K_a]:
        ojd.test_rect2.x += enemy_speed
        ojd.pixel_rect.x += back_ground
    if key[pygame.K_s]:
        ojd.test_rect2.y -= enemy_speed
        ojd.pixel_rect.y -= back_ground
    if key[pygame.K_d]:
        ojd.test_rect2.x -= enemy_speed
        ojd.pixel_rect.x -= back_ground

def move_object1():
    ojd.test_rect2.x = random.randint(0,700)
    ojd.test_rect2.y = random.randint(0,500)