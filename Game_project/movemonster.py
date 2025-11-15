import pygame
import math
import object_data as ojd

def move_monter():
    dis_x_en = 400 - ojd.enemy_rect.x
    dis_y_en = 300 - ojd.enemy_rect.y
    distance = ((dis_x_en**2) + (dis_y_en**2))**(1/2)

    if distance >= 40:
        dis_x_en = dis_x_en / distance
        dis_y_en = dis_y_en / distance
        ojd.enemy_rect.x += dis_x_en * ojd.enemy_speed
        ojd.enemy_rect.y += dis_y_en * ojd.enemy_speed