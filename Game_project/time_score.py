import pygame
import time
import object_data as ojd

#ตัวจับเวลา และตัวนับคะแนน

def timer_score():
    ojd.pass_time = time.time() - ojd.start_time            #ตัวคำนวณเวลาที่จะใช้แสดงภายในเกม
    font = pygame.font.SysFont("arial",30)          
    time_text = font.render(f"Time {(int(ojd.pass_time))//60}:{(int(ojd.pass_time))%60}", True, (255,255,255)) #แสดงเวลาออกทางหน้าจอ
    score = font.render(f"Score {int(ojd.count)}", True, (255,255,255))
    ojd.screen.blit(time_text,(10,10))
    ojd.screen.blit(score,(10,40))

