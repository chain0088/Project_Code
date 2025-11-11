import pygame
import math
import object_data as ojd
import stronger_enemy as ste

def move_monter():
    dis_x_en = 400 - ojd.test_rect2.x
    dis_y_en = 300 - ojd.test_rect2.y
    distance = ((dis_x_en**2) + (dis_y_en**2))**(1/2)

    if distance >= 40:
        dis_x_en = dis_x_en / distance
        dis_y_en = dis_y_en / distance
        ojd.test_rect2.x += dis_x_en * ojd.enemy_speed
        ojd.test_rect2.y += dis_y_en * ojd.enemy_speed