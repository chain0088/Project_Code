import pygame
import time
import movement as m
import object_data as ojd
import time_score as ts
import bullet as bul
import stronger_enemy as ste
import movemonster as mmr
import Start as s
import sum_score as ssc
import restart as R
import Music as M

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

fps = 60
clock = pygame.time.Clock()

M.music()

run=True
while run:                                          #loop หลักของเกมทำให้เกมทำงานได้
    for event in pygame.event.get():                #ตรวจสอบอีเว้นต่างๆภายในเกม
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            if (295 <= mouse_x <= 490) and (250 <= mouse_y <= 310):
                ojd.start_game = 1
                ojd.start_time = time.time()
            elif (295 <= mouse_x <= 490) and (330 <= mouse_y <= 390):
                run = False

    if ojd.start_game == 0:
        s.menu()
    else:
        if ojd.enemy_rect.colliderect(ojd.player_rect):
            ojd.start_game = 2
            ojd.summary = 1

        screen.blit(ojd.pixel,ojd.pixel_rect)           #แสดงพื้นหลัง
        screen.blit(ojd.enemy,ojd.enemy_rect)           #แสดงศัตรูออกทางหน้าจอเกม(ยังไม่ได้ใส่รูปศัตรูจริง)
        bul.bullets.draw(screen)                        #แสดงกระสุนออกทางหน้าจอ

        ts.timer_score()                                      #ตัวจับเวลา
        ste.Str_enemy()                                #ทำให้ศัตรูตัวเล็กลง
        m.move()                                       #การเคลื่อนไหวของผู้เล่น
        mmr.move_monter()                              #การเคลื่อนที่monsters

        ojd.bullet_delay_time += 1
        if ojd.bullet_delay_time % (60 - (ojd.count//2)) == 0:
            mouse_pos = pygame.mouse.get_pos()
            bullet = bul.Bullet(ojd.player_rect.centerx, ojd.player_rect.centery, mouse_pos)
            bul.bullets.add(bullet)
        bul.bullets.update()

    if ojd.summary == 1:
        if ojd.save_time_score == 0:
            ojd.sum_time = ojd.pass_time
            ojd.sum_score = ojd.count
            ojd.save_time_score = 1
            ojd.restart = 1
        ssc.sum_score()

    if ojd.restart == 1:
        if (300 <= mouse_x <= 500) and (450 <= mouse_y <= 530):
            R.restart()

    pygame.display.update()                         #อัพเดทหน้าจอเกมเมื่อเิกดเหตุการต่างๆ
    clock.tick(fps)                                 #กำหนดเฟรมเรทไม้ให้โค้ดทำงานเร็วเกินไป
pygame.quit()