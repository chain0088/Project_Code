import pygame
import bullet as bul
import object_data as ojd

def Str_enemy():
    if ojd.count <= 50:
        ojd.test2 = pygame.transform.scale(ojd.test2,(100-(ojd.size*ojd.count),100-(ojd.size*ojd.count)))
