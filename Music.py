import pygame

pygame.init()
pygame.display.set_caption("Game name")
screen = pygame.display.set_mode((800, 600))    

Music = pygame.mixer.music.load("Music/Theme1.mp3")
pygame.mixer.music.play(-1)
Music_volume = 0.1
pygame.mixer.music.set_volume(Music_volume)

pygame.time.delay(1000)
pygame.mixer.music.stop()

Music.play
run=True
while run:                                          
    for event in pygame.event.get():                
        if event.type == pygame.QUIT:
            run = False