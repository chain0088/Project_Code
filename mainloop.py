import pygame
import movement as m
import object_data as ojd
import game_time as gt
import bullet as bul
import stronger_enemy as ste
import Music as Mu

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))
fps = 60
clock = pygame.time.Clock()



def music():
    pygame.mixer.init()
    pygame.mixer.music.load("Music/Theme1.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

music()

run=True
while run:                                          #loop หลักของเกมทำให้เกมทำงานได้
    for event in pygame.event.get():                #ตรวจสอบอีเว้นต่างๆภายในเกม
        if event.type == pygame.QUIT:
            run = False


    screen.blit(ojd.pixel,ojd.pixel_rect)           #แสดงพื้นหลัง
    screen.blit(ojd.test2,ojd.test_rect2)           #แสดงศัตรูออกทางหน้าจอเกม(ยังไม่ได้ใส่รูปศัตรูจริง)
    ste.Str_enemy()
    # pygame.draw.rect(screen, (125,125,125), (ojd.test_rect2.x,ojd.test_rect2.y+120,bul.max_hp,20))
    # pygame.draw.rect(screen, (0,255,0), (ojd.test_rect2.x,ojd.test_rect2.y+120,bul.max_hp-(bul.damage*bul.count),20))
    bul.bullets.draw(screen)


    m.move()

    bul.bullet_delay_time += 1
    if bul.bullet_delay_time % 30 == 0:
        mouse_pos = pygame.mouse.get_pos()
        bullet = bul.Bullet(ojd.test_rect.centerx, ojd.test_rect.centery, mouse_pos)
        bul.bullets.add(bullet)

    gt.timer()                                      #ตัวจับเวลา

    bul.bullets.update()
    pygame.display.update()                         #อัพเดทหน้าจอเกมเมื่อเิกดเหตุการต่างๆ
    clock.tick(fps)                                 #กำหนดเฟรมเรทไม้ให้โค้ดทำงานเร็วเกินไป
pygame.quit()