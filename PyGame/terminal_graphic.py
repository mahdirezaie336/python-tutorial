import pygame
import threading


game_continue = True


def loop_event_pump(*args):
    while game_continue:
        pygame.event.pump()


pygame.init()
pencil_size = 1
pencil_color = (0, 0, 0)
screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
pygame.display.update()

# game loop
t = threading.Thread(args=tuple(), target=loop_event_pump)
t.setDaemon(True)
t.start()
# Getting inputs
while True:
    inputs = input().split()
    if inputs[0] == 'change':
        if inputs[1] == 'color':
            r = int(inputs[2])
            g = int(inputs[3])
            b = int(inputs[4])
            pencil_color = (r, g, b)
        elif inputs[1] == 'size':
            pencil_size = int(inputs[2])
    elif inputs[0] == 'draw':
        if inputs[1] == 'circle':
            x = int(inputs[2])
            y = int(inputs[3])
            r = int(inputs[4])
            pygame.draw.circle(screen, pencil_color, (x, y), r, pencil_size)
        elif inputs[1] == 'line':
            x0 = int(inputs[2])
            y0 = int(inputs[3])
            x1 = int(inputs[4])
            y1 = int(inputs[5])
            pygame.draw.line(screen, pencil_color, (x0, y0), (x1, y1), pencil_size)
        elif inputs[1] == 'polygon':
            points = []
            for i in range(2, len(inputs), 2):
                x = int(inputs[i])
                y = int(inputs[i + 1])
                points.append((x, y))
            pygame.draw.polygon(screen, pencil_color, points, pencil_size)
    elif inputs[0] == 'end':
        pygame.image.save(screen, 'draw.png')
        break
    pygame.display.update()
game_continue = False
