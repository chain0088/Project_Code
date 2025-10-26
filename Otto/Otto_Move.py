import pygame

#ประกาศใช้งาน pygame
pygame.init()

#หัวข้อเกม
pygame.display.set_caption("Vasco")

#ตั้งค่าสี 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#ตั้งค่าขนาดหน้าจอ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#ความเร็วตัวละคร
speed = 5
FPS = 60
Map_speed = 5
obstacle = [screen_width - 100, screen_width + 100, screen_width + 300]

clock = pygame.time.Clock()


#แสดงหน้าจอเกม
screen.fill(WHITE) #เติมสีพื้นหลัง



#โหลดภาพ
pygame.image.load("image/Char.png") #โหลดภาพตัวละคร
Char = pygame.image.load("image/Char.png") #เก็บภาพตัวละครในตัวแปร
Char = pygame.transform.scale(Char, (120, 130)) #ปรับขนาดภาพตัวละคร

Char_rect = Char.get_rect()  # รับขนาดภาพตัวละคร
Char_rect.centerx = screen_width // 2  # กึ่งกลางแนวนอนของหน้าจอ
Char_rect.centery = screen_height // 2  # กึ่งกลางแนวตั้งของหน้าจอ

Map = pygame.image.load("image/Map.jpg") #โหลดภาพพื้นหลัง
Map = pygame.transform.scale(Map, (800, 600)) #ปรับขนาดภาพพื้นหลัง

Map_rect = Map.get_rect()  # รับขนาดภาพพื้นหลัง
Map_rect.centerx = screen_width // 2  # กึ่งกลางแนวนอนของหน้าจอ
Map_rect.centery = screen_height // 2  # กึ่งกลางแนวตั้งของหน้าจอ    



running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    screen.blit(Map, Map_rect)  
    screen.blit(Char, Char_rect) #วางภาพตัวละครบนหน้าจอ
    pygame.display.update() #อัพเดทหน้าจอ

    
    for event in pygame.event.get():#ตรวจอีเวนด์
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed() # ตรวจสอบปุ่มที่ถูกกด
    if keys[pygame.K_w]: # ปุ่ม W
        Char_rect.y -= speed
    if keys[pygame.K_s]: # ปุ่ม S
        Char_rect.y += speed
    if keys[pygame.K_a]: # ปุ่ม A
        Char_rect.x -= speed
    if keys[pygame.K_d]: # ปุ่ม D
        Char_rect.x += speed
    
pygame.quit() #ออกจาก pygame