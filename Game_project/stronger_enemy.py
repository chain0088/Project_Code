import pygame
import bullet as bul
import object_data as ojd
import time_score as gt

screen = pygame.display.set_mode((800, 600))
size = 10
def Str_enemy():
    if bul.count > 0 and bul.count <= 3:
        ojd.test2 = pygame.transform.scale(ojd.test2,(100-(size*bul.count),100-(size*bul.count)))
