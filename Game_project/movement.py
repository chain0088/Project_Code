import pygame
import random
import object_data as ojd
import player_animation as pa

screen = pygame.display.set_mode((800, 600))

def move():                                        #การเคลื่อนที่
    key = pygame.key.get_pressed()                 #ตรวจจับการกดปุ่มบนคีบอร์ด
    enemy_speed = 3
    back_ground = 1

    if key[pygame.K_LSHIFT]:
        enemy_speed = 6
        back_ground = 2

    pa.player_anima(key)

    if key[pygame.K_w] and (ojd.pixel_rect.y < 0):
        ojd.test_rect2.y += enemy_speed
        ojd.pixel_rect.y += back_ground
    if key[pygame.K_a] and (ojd.pixel_rect.x < 0):
        ojd.test_rect2.x += enemy_speed
        ojd.pixel_rect.x += back_ground
    if key[pygame.K_s] and (ojd.pixel_rect.y > -800):
        ojd.test_rect2.y -= enemy_speed
        ojd.pixel_rect.y -= back_ground
    if key[pygame.K_d] and (ojd.pixel_rect.x > -800):
        ojd.test_rect2.x -= enemy_speed
        ojd.pixel_rect.x -= back_ground

def move_object1():                                 #ศัตรูสุ่มไปตำแหน่งต่างๆ
    ojd.test_rect2.x = random.randint(0,700)
    ojd.test_rect2.y = random.randint(0,500)