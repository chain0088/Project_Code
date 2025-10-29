import pygame


test = pygame.image.load("picture/test.png")
test = pygame.transform.scale(test,(50,50))
test_rect = test.get_rect()

test2 = pygame.image.load("picture/test copy.png")
test2 = pygame.transform.scale(test2,(100,100))
test_rect2 = test2.get_rect()

pixel = pygame.image.load("picture/pixel.jpg")
pixel = pygame.transform.scale(pixel,(1200,1000))
pixel_rect = pixel.get_rect()

test_rect.center = (400,300)
test_rect2.center = (200,150)
pixel_rect.center = (400,300)