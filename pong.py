import pygame
from pygame.locals import *

motion = 30
motionClock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pong')

background = (0, 0, 0)
ball = (255, 255, 255)
rectangle = (255, 255, 255)

screen.fill(background)
pygame.draw.rect(screen, rectangle, (1, 100, 10, 100))
pygame.draw.rect(screen, rectangle, (389, 100, 10, 100))
pygame.draw.circle(screen, ball, (250, 100, ), 10, 0)

while True:
	for i in pygame.event.get():
		if i.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()