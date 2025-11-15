import pygame
import bullet as bul
import object_data as ojd

def Str_enemy():
    if ojd.count <= 10:
        ojd.enemy = pygame.transform.scale(ojd.enemy,(100-(ojd.down_size_enemy*ojd.count),100-(ojd.down_size_enemy*ojd.count)))
