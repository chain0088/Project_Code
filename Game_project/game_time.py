import pygame
import time

#ตัวจับเวลา

screen = pygame.display.set_mode((800, 600))
start_time = time.time()
pass_time = 0

def timer():
    pass_time = time.time() - start_time            #ตัวคำนวณเวลาที่จะใช้แสดงภายในเกม
    font = pygame.font.SysFont("arial",30)          
    time_text = font.render(f"{(round(pass_time))//60}:{(round(pass_time))%60}", True,(255,255,255)) #แสดงเวลาออกทางหน้าจอ
    screen.blit(time_text,(10,10))
