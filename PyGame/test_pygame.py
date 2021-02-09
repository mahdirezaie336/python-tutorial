import pygame
img = pygame.image.load('draw.png')

white = (255, 255, 255)
screen = pygame.display.set_mode((640, 480))
screen.fill((white))

x, y = 0, 0

while True:
    screen.fill((white))
    screen.blit(img,(x, y))
    x, y = x + 1, y + 1
    pygame.display.update()
    pygame.time.delay(10)
    pygame.event.pump()