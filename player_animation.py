import pygame
import movement as m
import object_data as ojd
import player_animation as pa

screen = pygame.display.set_mode((800, 600))
fram_anima = 0

def player_anima(key):

    if key[pygame.K_d]:
        p_anima = []
        p_anima.append(pygame.image.load("Hero/Right/R1.png"))
        p_anima.append(pygame.image.load("Hero/Right/R2.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R3.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R4.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R5.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R6.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R7.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R8.png"))
       # p_anima.append(pygame.image.load("Hero/Right/R9.png"))
        screen.blit(p_anima[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    if key[pygame.K_a]:
        p_anima = []
        p_anima.append(pygame.image.load("Hero/Left/L1.png"))
        p_anima.append(pygame.image.load("Hero/Left/L2.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L3.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L4.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L5.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L6.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L7.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L8.png"))
        # p_anima.append(pygame.image.load("Hero/Left/L9.png"))
        screen.blit(p_anima[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    if key[pygame.K_w]:
        p_anima = []
        p_anima.append(pygame.image.load("Hero/Top/T1.png"))
        p_anima.append(pygame.image.load("Hero/Top/T2.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T3.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T4.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T5.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T6.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T7.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T8.png"))
        #p_anima.append(pygame.image.load("Hero/Top/T9.png"))
        screen.blit(p_anima[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    if key[pygame.K_s]:
        p_anima = []
        p_anima.append(pygame.image.load("Hero/Down/D1.png"))
        p_anima.append(pygame.image.load("Hero/Down/D2.png"))
        screen.blit(p_anima[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    if pa.fram_anima >= 2 :
        pa.fram_anima = 0

