import pygame

def music():
    pygame.mixer.init()
    pygame.mixer.music.load("Music/Theme1.mp3")
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)