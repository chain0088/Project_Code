import pygame

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))    

Music = pygame.mixer.music.load("Music/Theme1.mp3")
pygame.mixer.music.play(-1)

run=True
while run:                                          #loop หลักของเกมทำให้เกมทำงานได้
    for event in pygame.event.get():                #ตรวจสอบอีเว้นต่างๆภายในเกม
        if event.type == pygame.QUIT:
            run = False