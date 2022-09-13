import pygame,sys

pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
displaySurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#import image
spaceShip = pygame.image.load('./Assets/astro/ship.png').convert_alpha()

#set title and icon
pygame.display.set_caption("Astro Shooter")
pygame.display.set_icon(spaceShip)

#import text
gameFont = pygame.font.Font("./Assets/astro/subatomic.ttf",50)
text_surf = gameFont.render('Space Astro', True ,'white')

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    displaySurface.fill((0,5,35))
    displaySurface.blit(spaceShip,(300,500))
    displaySurface.blit(text_surf,(500,200))

    pygame.display.update()