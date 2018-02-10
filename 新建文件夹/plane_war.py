import sys 
import pygame
from settings import Settings
import functions as f 
from plane import Plane 

def run():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width,
		settings.screen_height))
	pygame.display.set_caption("打飞机")

	plane = Plane(settings,screen)
	while True:
		f.check_events(settings,screen,plane)

		plane.update()
		f.update_screen(settings,screen,plane)

run()

