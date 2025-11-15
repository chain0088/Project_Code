import pygame
import object_data as ojd


def menu():
    # Color
    white = (255, 255, 255)
    red = (255,0,0)
    green = (0, 255, 128)

    # Topic Caption ตั้งค่าข้อความและฟอนต์
    # arial 54ugcrbdbernadetteotf
    sys_font1 =  pygame.font.SysFont("54ugcrbdbernadetteotf",60)
    sys_font2 = pygame.font.SysFont("54ugcrbdbernadetteotf",50)
    Game_caption = sys_font1.render("Game Name", True, white)
    start = sys_font2.render("Start", True, white)
    quit = sys_font2.render("Quit", True, white)

    # รูปพื้นหลังหน้าหลักเกม //2Novยังทำให้imgไม่บังรูปทรงและแคปชันไม่ได้
    wall= pygame.image.load("picture/open_menu.jpg")
    wall= pygame.transform.scale(wall,(800,600))

    ojd.screen.blit(wall, (0,0))
    ojd.screen.blit(Game_caption, (265,80))
    pygame.draw.rect(ojd.screen, green, (295,250,195,60))
    pygame.draw.rect(ojd.screen, red,(295,330,195,60))
    ojd.screen.blit(start, (350,265))
    ojd.screen.blit(quit, (350,345))
