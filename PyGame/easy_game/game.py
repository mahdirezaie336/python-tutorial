import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 320 * 2, 240 * 2
        self.speed = [1, 1]
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        # self.ball, self.ballrect = self.load_image("intro_ball.gif")
        self.ball, self.ballrect = self.load_image("sq.png")

    def load_image(self, image_name):
        pass

    def move_ball(self):
        ballrect = self.ballrect.move(self.speed)
        if ballrect.left < 0 or ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if ballrect.top < 0 or ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]
        self.ballrect = ballrect

    def draw(self):
        pass

    def handel_events(self):
        pass

