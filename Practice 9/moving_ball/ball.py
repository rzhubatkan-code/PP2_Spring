import pygame 

class Ball:
    def __init__(self, x , y, radius, color, screen_width, screen_height):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.screen_height=screen_height
        self.screen_width=screen_width
        self.step=20

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x , self.y), self.radius)


    def move(self, direction):
        if direction == "UP":
            if self.y-self.radius-self.step >= 0:
                self.y -= self.step
        elif direction == "DOWN":
            if self.y +self.radius + self.step <= self.screen_height:
                self.y += self.step
        elif direction == "LEFT":
            if self.x - self.radius - self.step >= 0:
                self.x -= self.step
        elif direction == "RIGHT":
            if self.x +self.radius + self.step <= self.screen_width:
                self.x += self.step