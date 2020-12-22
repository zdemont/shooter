import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def update(self, screen):
          # apply player image
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        # get player projectile
        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        # check if player go to right or left
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
