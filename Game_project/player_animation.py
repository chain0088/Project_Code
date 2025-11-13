import pygame
import movement as m
import object_data as ojd

fram_anima = 0

def player_anima(key):

    if not any(key) or (not key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_s] and not key[pygame.K_d]):
        ojd.screen.blit(ojd.test,ojd.test_rect)

    if key[pygame.K_w]:
        p_anima_up = []
        p_anima_up.append(pygame.image.load("Hero/Top/T1.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T2.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T3.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T4.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T5.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T6.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T7.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T8.png"))
        p_anima_up.append(pygame.image.load("Hero/Top/T9.png"))
        ojd.screen.blit(p_anima_up[int(ojd.fram_animation)],ojd.test_rect)
        ojd.fram_animation += 0.1

    elif key[pygame.K_a]:
        p_anima_left = []
        p_anima_left.append(pygame.image.load("Hero/Left/L1.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L2.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L3.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L4.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L5.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L6.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L7.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L8.png"))
        p_anima_left.append(pygame.image.load("Hero/Left/L9.png"))
        ojd.screen.blit(p_anima_left[int(ojd.fram_animation)],ojd.test_rect)
        ojd.fram_animation += 0.1

    elif key[pygame.K_s]:
        p_anima_down = []
        p_anima_down.append(pygame.image.load("Hero/Down/D1.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D2.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D3.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D4.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D5.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D6.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D7.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D8.png"))
        p_anima_down.append(pygame.image.load("Hero/Down/D9.png"))
        ojd.screen.blit(p_anima_down[int(ojd.fram_animation)],ojd.test_rect)
        ojd.fram_animation += 0.1

    elif key[pygame.K_d]:
        p_anima_right = []
        p_anima_right.append(pygame.image.load("Hero/Right/R1.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R2.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R3.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R4.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R5.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R6.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R7.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R8.png"))
        p_anima_right.append(pygame.image.load("Hero/Right/R9.png"))
        ojd.screen.blit(p_anima_right[int(ojd.fram_animation)],ojd.test_rect)
        ojd.fram_animation += 0.1

    if ojd.fram_animation >= 2 :
        ojd.fram_animation = 0

