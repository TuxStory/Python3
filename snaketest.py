import pygame
import random
from math import sin, cos
 
W, H = 500, 500
#Rayon d'un segment du snake
RADIUS = 5
# Pour l'interpolation lineaire entre les segments su snake
RATIO = 2
# Nombre de ms entre 2 frames
TICKS_INTERVAL = 20
# Increment de l'angle
INC_ANGLE = .1
 
SNAKE_SPEED, SNAKE_ANGLE = 3, 0
 
class Node:
    def __init__(self,x , y):
         self.x, self.y = x, y
         
class Snake:
    def __init__(self, x, y):
        self.speed, self.angle = SNAKE_SPEED, SNAKE_ANGLE
        self.nodes = [Node(x, y) for _ in range(5)]
        self.head = self.nodes[0]
        self.alive = True
         
    def update(self):       
        # On bouge le corps
        for i in range(len(self.nodes) - 1, 0, -1):
            self.nodes[i].x += (self.nodes[i - 1].x - self.nodes[i].x) / RATIO
            self.nodes[i].y += (self.nodes[i - 1].y - self.nodes[i].y) / RATIO
        # On bouge la tete
        self.head.x += cos(self.angle) * self.speed
        self.head.y -= sin(self.angle) * self.speed
        # Dans les limites ?
        if not (0 <= self.head.x < W and 0 <= self.head.y < H):
            snake.alive = False
             
        # Collision entre la tete et un segments ?
        xh = self.head.x + cos(self.angle) * RADIUS
        yh = self.head.y - sin(self.angle) * RADIUS
        for i, rct in enumerate(self.getNodesRect()):
            if i:
                if pygame.Rect(rct).collidepoint(xh, yh):
                    self.snake.alive = False #
                    break
     
    def grow(self):
        x, y = self.nodes[-1].x, self.nodes[-1].y
        self.nodes.extend([Node(x, y) for _ in range(5)])
         
    def getNodesRect(self):
         return [(nd.x - RADIUS, nd.y - RADIUS, RADIUS * 2, RADIUS * 2) \
                                                        for nd in self.nodes]
    def eat(self, rctApple):
        return pygame.Rect(self.head.x - RADIUS, self.head.y - RADIUS, RADIUS * 2, RADIUS * 2).colliderect(rctApple)
     
    def display(self):
        screen = pygame.display.get_surface()
        for nd in self.nodes:
            x, y = nd.x, nd.y
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), RADIUS)
             
 
class Apple:
    def __init__(self):
        self.x = random.randrange(10, W - 10)
        self.y = random.randrange(10, H - 10)
        self.rect = (self.x - RADIUS, self.y - RADIUS, RADIUS * 2, RADIUS * 2)
        self.active = False
     
    def wait(self, nds):
        for nd in nds:
            if pygame.Rect(self.rect).colliderect(nd):
                return
        self.active = True
        return
     
    def display(self):
        screen = pygame.display.get_surface()
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), RADIUS)
         
         
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        self.snake = Snake(W / 2, H / 2)
        self.apple = Apple()
        self.score = 0
        self.done = False
         
    def timeLeft(self):
        now = pygame.time.get_ticks()
        if self.nxtTime <= now:
            return 0
        else:
            return self.nxtTime - now;
     
    def run(self):
        self.nxtTime = pygame.time.get_ticks()
        while self.snake.alive and not self.done:
            self.updateEvents()
            self.update()
            self.display()
            pygame.time.delay(self.timeLeft())
            pygame.display.flip()
            self.nxtTime += TICKS_INTERVAL
 
     
    def updateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        self.snake.angle += INC_ANGLE * (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT])
     
    def update(self):
        self.snake.update()
        if not self.apple.active:
            self.apple.wait(self.snake.getNodesRect())
        if self.snake.eat(self.apple.rect):
            self.apple = Apple()
            self.snake.grow()
            self.score += 1
     
    def display(self):
        self.screen.fill(0)
        self.snake.display()
        self.apple.display()
         
game = Game()
game.run()
