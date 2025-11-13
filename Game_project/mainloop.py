import pygame
import movement as m
import object_data as ojd
import time_score as ts
import bullet as bul
import stronger_enemy as ste
import movemonster as mmr
# import Music as mc

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))

fps = 60
clock = pygame.time.Clock()

# mc.music()

run=True
while run:                                          #loop หลักของเกมทำให้เกมทำงานได้
    for event in pygame.event.get():                #ตรวจสอบอีเว้นต่างๆภายในเกม
        if event.type == pygame.QUIT:
            run = False

    if ojd.test_rect2.colliderect(ojd.test_rect):
        run = False

    screen.blit(ojd.pixel,ojd.pixel_rect)           #แสดงพื้นหลัง
    screen.blit(ojd.test2,ojd.test_rect2)           #แสดงศัตรูออกทางหน้าจอเกม(ยังไม่ได้ใส่รูปศัตรูจริง)
    bul.bullets.draw(screen)

    ts.timer_score()                                      #ตัวจับเวลา
    ste.Str_enemy()
    m.move()
    mmr.move_monter()                              #การเคลื่อนที่monsters

    ojd.bullet_delay_time += 1
    if ojd.bullet_delay_time % (60 - (ojd.count//2)) == 0:
        mouse_pos = pygame.mouse.get_pos()
        bullet = bul.Bullet(ojd.test_rect.centerx, ojd.test_rect.centery, mouse_pos)
        bul.bullets.add(bullet)

    bul.bullets.update()
    pygame.display.update()                         #อัพเดทหน้าจอเกมเมื่อเิกดเหตุการต่างๆ
    clock.tick(fps)                                 #กำหนดเฟรมเรทไม้ให้โค้ดทำงานเร็วเกินไป
pygame.quit()