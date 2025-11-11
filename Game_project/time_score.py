import pygame
import time
import bullet as bul
import object_data as ojd

#ตัวจับเวลา และตัวนับคะแนน


start_time = time.time()

def timer_score():
    pass_time = time.time() - start_time            #ตัวคำนวณเวลาที่จะใช้แสดงภายในเกม
    font = pygame.font.SysFont("arial",30)          
    time_text = font.render(f"Time {(int(pass_time))//60}:{(int(pass_time))%60}", True, (255,255,255)) #แสดงเวลาออกทางหน้าจอ
    ojd.screen.blit(time_text,(10,10))
    score = font.render(f"Score {int(ojd.count)}", True, (255,255,255))
    ojd.screen.blit(score,(10,40))
