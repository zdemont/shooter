import pygame
from game import Game
pygame.init()


# generate window
pygame.display.set_caption('Comet fall Game')
screen = pygame.display.set_mode((1080, 720))

# import background window
background = pygame.image.load('assets/bg.jpg')

# load game
game = Game()


running = True

while running:

    # apply game background
    screen.blit(background, (0, -200))

    # apply player image
    screen.blit(game.player.image, game.player.rect)

    # check if player go to right or left
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # maj l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Close windows')

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

