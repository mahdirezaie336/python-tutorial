import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Testing PyGame!')
red = (255, 0, 0)
blue = (0, 0, 255)

turn = True
while True:
    pygame.event.pump()

    if turn:
        screen.fill(red)
    else:
        screen.fill(blue)

    turn = not turn
    pygame.display.update()
    pygame.time.delay(200)
