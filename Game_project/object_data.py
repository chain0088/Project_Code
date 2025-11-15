import pygame

#กำหนดวัตถุต่างๆภายในเกม

#ตัวละครผู้เล่น
test = pygame.image.load("Hero/Stand.png")
test_rect = test.get_rect()

#ตัวละครศัตรู
test2 = pygame.image.load("picture/Boss.gif")
test2 = pygame.transform.scale(test2,(100,100))
test_rect2 = test2.get_rect()

#ภาพพื้นหลัง
pixel = pygame.image.load("picture/pixel.jpg")
pixel = pygame.transform.scale(pixel,(1600,1400))
pixel_rect = pixel.get_rect()

#กำหนดตำแหน่งเริ่มต้น
test_rect.center = (400,300)
test_rect2.center = (0,0)
pixel_rect.center = (400,300)


screen = pygame.display.set_mode((800, 600))

# enemy
down_size_enemy = 5
enemy_speed = 1
boss_hp = 1

# player
fram_animation = 0

#  bullet
count = 0
bullet_delay_time = 0