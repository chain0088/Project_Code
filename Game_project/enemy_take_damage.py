import pygame
import object_data as ojd
import movement as m
import bullet as bul

# count = 0
# damage = 20
# damage_time = 0
# max_hp = 100
# screen = pygame.display.set_mode((800, 600))

# def enemy_td():
#     global count                      #ใช้ global เพื่อประกาศให้สามารถใช้ค่าที่กำหนดได้ทั้งภายในและนอกฟังก์ชั่น
#     global damage
#     global damage_time
#     global max_hp

#     if count >= 5:
#         ojd.test2.fill(0)               #การทำให้ศัตรูหายไปเมื่อเลือดหมด
#         max_hp = 0                      #การทำให้หลอดเลือดศัตรูหายไปเมื่อตาย

#     if ojd.test_rect.colliderect(ojd.test_rect2) and (count < 5) and (damage_time <= 5):
#         pygame.draw.rect(screen, (255,0,0), (ojd.test_rect2.x,ojd.test_rect2.y,100,100))
#         damage_time += 1

#     if ojd.test_rect.colliderect(ojd.test_rect2) and (count < 5) and (damage_time > 5):
#         m.move_object1()
#         count += 1
#         damage_time = 0
        
#     pygame.draw.rect(screen, (125,125,125), (ojd.test_rect2.x,ojd.test_rect2.y+120,max_hp,20))
#     pygame.draw.rect(screen, (0,255,0), (ojd.test_rect2.x,ojd.test_rect2.y+120,max_hp-(damage*count),20))
