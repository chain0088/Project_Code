import pygame
import math
import random

# เริ่มต้น pygame
pygame.init()

# ตั้งค่าหน้าจอ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Chase Game")

# สี
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# กำหนด player และ monster
player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)
monster = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 40, 40)

# ความเร็ว
player_speed = 5
monster_speed = 2

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # FPS

    # ตรวจจับเหตุการณ์
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # การควบคุมผู้เล่น
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # มอนสเตอร์วิ่งเข้าหาผู้เล่น
    dx = player.x - monster.x
    dy = player.y - monster.y
    distance = math.hypot(dx, dy)  # หาระยะทาง

    if distance >= 40:
        dx, dy = dx / distance, dy / distance  # ทำให้เป็นทิศทางหน่วย (normalize)
        monster.x += dx * monster_speed
        monster.y += dy * monster_speed

    # ล้างหน้าจอและวาดใหม่
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, monster)

    pygame.display.flip()

pygame.quit()

