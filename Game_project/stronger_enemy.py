import pygame
import bullet as bul
import object_data as ojd

def Str_enemy():
    if ojd.count <= 10:
        ojd.test2 = pygame.transform.scale(ojd.test2,(100-(ojd.down_size_enemy*ojd.count),100-(ojd.down_size_enemy*ojd.count)))
