import pygame
import movement as m
import object_data as ojd
import time_score as ts
import bullet as bul
import stronger_enemy as ste
import movemonster as mmr
import Start as s

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

fps = 60
clock = pygame.time.Clock()

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
            elif (295 <= mouse_x <= 490) and (330 <= mouse_y <= 390):
                run = False

    if ojd.start_game == 0:
        s.menu()
    else:
        if ojd.test_rect2.colliderect(ojd.test_rect):
            run = False

        screen.blit(ojd.pixel,ojd.pixel_rect)           #แสดงพื้นหลัง
        screen.blit(ojd.test2,ojd.test_rect2)           #แสดงศัตรูออกทางหน้าจอเกม(ยังไม่ได้ใส่รูปศัตรูจริง)

        ts.timer_score()                                      #ตัวจับเวลา
        ste.Str_enemy()
        bul.bullets.draw(screen)
        m.move()
        mmr.move_monter()                              #การเคลื่อนที่monstersssssss

        ojd.bullet_delay_time += 1
        if ojd.bullet_delay_time % (60 - (ojd.count//2)) == 0:
            mouse_pos = pygame.mouse.get_pos()
            bullet = bul.Bullet(ojd.test_rect.centerx, ojd.test_rect.centery, mouse_pos)
            bul.bullets.add(bullet)

        bul.bullets.update()
    pygame.display.update()                         #อัพเดทหน้าจอเกมเมื่อเิกดเหตุการต่างๆ
    clock.tick(fps)                                 #กำหนดเฟรมเรทไม้ให้โค้ดทำงานเร็วเกินไป
pygame.quit()