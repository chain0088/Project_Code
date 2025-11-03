import pygame
import math
import object_data as ojd
import movement as m
import bullet as bul

count = 0
damage = 20
damage_time = 0
max_hp = 100
bullet_delay_time = 0
screen = pygame.display.set_mode((800, 600))
bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, target_pos):
        super().__init__()
        self.image = pygame.image.load("picture/b.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.bullet_speed = 10

        dis_x, dis_y = target_pos[0] - player_x, target_pos[1] - player_y
        distance = math.hypot(dis_x, dis_y)
        self.bullet_speed = ((dis_x / distance) * self.bullet_speed, (dis_y / distance) * self.bullet_speed)

    def update(self):
        self.rect.x += self.bullet_speed[0]
        self.rect.y += self.bullet_speed[1]

        if bul.count < 5:
            if ojd.test2.get_rect(center = (ojd.test_rect2.x+50,ojd.test_rect2.y+50)).colliderect(self.rect):
                self.kill()
                pygame.draw.rect(screen, (255,0,0), (ojd.test_rect2.x,ojd.test_rect2.y,100-(20*bul.count),100-(20*bul.count)))
                bul.count += 1
                m.move_object1()

        elif bul.count >= 5:
            ojd.test2.fill(0)
            bul.max_hp = 0

        if not screen.get_rect().colliderect(self.rect):
            self.kill()
