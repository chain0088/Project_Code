import pygame
import random
import object_data as ojd
import player_animation as pa

def move():                                        #การเคลื่อนที่
    key = pygame.key.get_pressed()                 #ตรวจจับการกดปุ่มบนคีบอร์ด
    En_S_when_player_move = 3
    BG_S_when_player_move = 1

    if key[pygame.K_LSHIFT]:
        En_S_when_player_move = 6
        BG_S_when_player_move = 2

    pa.player_anima(key)

    if key[pygame.K_w] and (ojd.pixel_rect.y < 0):
        ojd.enemy_rect.y += En_S_when_player_move
        ojd.pixel_rect.y += BG_S_when_player_move

    if key[pygame.K_a] and (ojd.pixel_rect.x < 0):
        ojd.enemy_rect.x += En_S_when_player_move
        ojd.pixel_rect.x += BG_S_when_player_move

    if key[pygame.K_s] and (ojd.pixel_rect.y > -800):
        ojd.enemy_rect.y -= En_S_when_player_move
        ojd.pixel_rect.y -= BG_S_when_player_move

    if key[pygame.K_d] and (ojd.pixel_rect.x > -800):
        ojd.enemy_rect.x -= En_S_when_player_move
        ojd.pixel_rect.x -= BG_S_when_player_move

def enemy_spawn():                                 #ศัตรูสุ่มไปตำแหน่งต่างๆ
    if ojd.count%2 == 0:
        ojd.enemy_rect.x = random.randint(-150,0)
        ojd.enemy_rect.y = random.randint(-150,0)
    else:
        ojd.enemy_rect.x = random.randint(800,900)
        ojd.enemy_rect.y = random.randint(600,700)