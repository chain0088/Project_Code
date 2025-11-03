import pygame
pygame.init()

# เซตติ้งตัวแปล
screen_W, screen_H= 800, 600
pygame.display.set_caption("เชนนี่ชายน์")
screen = pygame.display.set_mode((screen_W, screen_H))
# Color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
green = (0, 255, 128)
blue= (0, 0, 255)
pur = (229,204,255)
screen.fill(pur)

# ทำปุ่ม PLAY


# Topic Caption ตั้งค่าข้อความและฟอนต์
# arial 54ugcrbdbernadetteotf
sys_font1 =  pygame.font.SysFont("54ugcrbdbernadetteotf",60)
Game_caption = sys_font1.render("ChainyShine",True,white)
sys_font2 = pygame.font.SysFont("arail",46)
shall = sys_font2.render("Shall we go to space together??",True,white)


# รูปพื้นหลังหน้าหลักเกม //2Novยังทำให้imgไม่บังรูปทรงและแคปชันไม่ได้
wall= pygame.image.load("picture/safariWall.jpg")
wall= pygame.transform.scale(wall,(800,600))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(wall,(0,0))
    screen.blit(Game_caption,(210,80))
    screen.blit(shall, (167,170))
    pygame.draw.rect(screen,green, (295,246,195,60))
    pygame.draw.rect(screen, red,(295,329,195,60))
    pygame.display.update()
pygame.quit()