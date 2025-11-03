import pygame
import bullet as bul
import object_data as ojd

size = 10
def Str_enemy():
    if bul.count > 0:
        ojd.test2 =  pygame.transform.scale(ojd.test2,(100-(size*bul.count),100-(size*bul.count)))