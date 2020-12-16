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


    # maj l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermer fenetre')

