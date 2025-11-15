import pygame
import object_data as ojd
import time_score as ts

def sum_score():
    ojd.screen.fill((0,0,0))
    font = pygame.font.SysFont("arial",80)
    font_2 = pygame.font.SysFont("arial",60)

    text = font.render("Result", True, (255,255,255))
    sum_time_text = font_2.render(f"Time {(int(ojd.sum_time))//60}:{(int(ojd.sum_time))%60}", True, (255,255,255))
    sum_score = font_2.render(f"Score {int(ojd.sum_score)}", True, (255,255,255))
    restart = font.render("Restart", True, (255,255,255))

    ojd.screen.blit(text,(310,50))
    ojd.screen.blit(sum_time_text,(310,200))
    ojd.screen.blit(sum_score,(320,300))
    ojd.screen.blit(restart,(300,450))
