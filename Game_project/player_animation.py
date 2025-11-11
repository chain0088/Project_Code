import pygame
import movement as m
import object_data as ojd
import player_animation as pa

screen = pygame.display.set_mode((800, 600))
fram_anima = 0

def player_anima(key):

    if not any(key) or (not key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_s] and not key[pygame.K_d]):
        screen.blit(ojd.test,ojd.test_rect)

    if key[pygame.K_w]:
        p_anima_up = []
        p_anima_up.append(pygame.image.load("Hero/Top/T4.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T8.png"))
        screen.blit(p_anima_up[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    elif key[pygame.K_a]:
        p_anima_left = []
        p_anima_left.append(pygame.image.load("Hero/Left/L2.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L6.png"))
        screen.blit(p_anima_left[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    elif key[pygame.K_s]:
        p_anima_down = []
        p_anima_down.append(pygame.image.load("Hero/Down/D4.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D8.png"))
        screen.blit(p_anima_down[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    elif key[pygame.K_d]:
        p_anima_right = []
        p_anima_right.append(pygame.image.load("Hero/Right/R2.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R6.png"))
        screen.blit(p_anima_right[int(fram_anima)],ojd.test_rect)
        pa.fram_anima += 0.1

    if pa.fram_anima >= 2 :
        pa.fram_anima = 0

