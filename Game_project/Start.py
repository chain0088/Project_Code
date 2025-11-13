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

# Topic Caption ตั้งค่าข้อความและฟอนต์
# arial 54ugcrbdbernadetteotf
sys_font1 =  pygame.font.SysFont("54ugcrbdbernadetteotf",60)
Game_caption = sys_font1.render("Game Name",True,white)
sys_font2 = pygame.font.SysFont("arail",50)
shall = sys_font2.render("Shall we go to space together??",True,white)
start = sys_font2.render("Start",True,white)
quit = sys_font2.render("Quit",True,white)


# รูปพื้นหลังหน้าหลักเกม //2Novยังทำให้imgไม่บังรูปทรงและแคปชันไม่ได้
wall= pygame.image.load("picture/safariWall.jpg")
wall= pygame.transform.scale(wall,(800,600))

start_game = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            if (295 <= mouse_x <= 490) and (250 <= mouse_y <= 310):
                start_game = 1
            elif (295 <= mouse_x <= 490) and (330 <= mouse_y <= 390):
                run = False

    if start_game == 1:
        screen.fill((0,255,0))

    else:
        screen.blit(wall,(0,0))
        screen.blit(Game_caption,(265,80))
        screen.blit(shall, (140,170))
        pygame.draw.rect(screen,green, (295,250,195,60))
        pygame.draw.rect(screen, red,(295,330,195,60))
        screen.blit(start, (350,265))
        screen.blit(quit, (350,345))
    pygame.display.update()
pygame.quit()