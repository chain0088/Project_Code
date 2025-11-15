import pygame
import object_data as ojd
import movement as m
import bullet as bul

bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, target_pos):
        super().__init__()
        self.image = pygame.image.load("picture/ammo.webp")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.bullet_speed = 10

        dis_x = target_pos[0] - player_x
        dis_y = target_pos[1] - player_y
        distance = ((dis_x**2) + (dis_y**2))**(1/2)
        self.bullet_speed_x = (dis_x / distance) * self.bullet_speed
        self.bullet_speed_y = (dis_y / distance) * self.bullet_speed

    def update(self):
        self.rect.x += self.bullet_speed_x
        self.rect.y += self.bullet_speed_y

        if (ojd.count < 10) and ojd.enemy.get_rect(center = (ojd.enemy_rect.x+50, ojd.enemy_rect.y+50)).colliderect(self.rect):
            self.kill()
            pygame.draw.rect(ojd.screen, (255,0,0), (ojd.enemy_rect.x, ojd.enemy_rect.y, 100-(ojd.down_size_enemy*ojd.count), 100-(ojd.down_size_enemy*ojd.count)))
            ojd.count += 1
            ojd.enemy_speed += 0.1
            m.enemy_spawn()

        if (ojd.count >= 10) and ojd.enemy.get_rect(center = (ojd.enemy_rect.x+50, ojd.enemy_rect.y+50)).colliderect(self.rect):
            self.kill()
            pygame.draw.rect(ojd.screen, (255,0,0), (ojd.enemy_rect.x, ojd.enemy_rect.y, 50, 50))
            ojd.boss_hp -= 1

        if ojd.boss_hp == 0:
            ojd.count += 1
            ojd.enemy_speed += 0.05
            ojd.boss_hp = ojd.count//5
            m.enemy_spawn()

        if not ojd.screen.get_rect().colliderect(self.rect):
            self.kill()