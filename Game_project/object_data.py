import pygame

#กำหนดวัตถุต่างๆภายในเกม

#ตัวละครผู้เล่น
player = pygame.image.load("Hero/Stand.png")
player_rect = player.get_rect()

#ตัวละครศัตรู
enemy = pygame.image.load("picture/Boss.gif")
enemy = pygame.transform.scale(enemy,(100,100))
enemy_rect = enemy.get_rect()

#ภาพพื้นหลัง
pixel = pygame.image.load("picture/pixel.jpg")
pixel = pygame.transform.scale(pixel,(1600,1400))
pixel_rect = pixel.get_rect()

#กำหนดตำแหน่งเริ่มต้น
player_rect.center = (400,300)
enemy_rect.center = (0,0)
pixel_rect.center = (400,300)

# ค่าตั้งต้นสำหรับการแสดงผล
screen = pygame.display.set_mode((800, 600))
mouse_x = 0
mouse_y = 0
start_game = 0
start_time = 0
pass_time = 0
summary = 0
save_time_score = 0
sum_time = 0
sum_score = 0
restart = 0

# enemy
down_size_enemy = 5
enemy_speed = 1
boss_hp = 1

# player
fram_animation = 0

#  bullet
count = 0
bullet_delay_time = 0