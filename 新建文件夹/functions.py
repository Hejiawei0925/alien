import sys
import pygame 

def check_events(settings,screen,plane):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,settings,screen,plane)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,plane)	

		

def check_keydown_events(event,settings,screen,plane):
	print('777')
	###### event.key  不是event.type
	if event.key == pygame.K_RIGHT:
		plane.moving_right = True	
	elif event.key == pygame.K_LEFT:
		plane.moving_left = True
	elif event.key == pygame.K_DOWN:
		plane.moving_down = True
	elif event.key == pygame.K_UP:
		plane.moving_up = True


	elif event.type == pygame.K_q:
		sys.exit()	

def check_keyup_events(event,plane):	
	if event.key == pygame.K_RIGHT:
		plane.moving_right = False	
	elif event.key == pygame.K_LEFT:
		plane.moving_left = False
	elif event.key == pygame.K_DOWN:
		plane.moving_down = False
	elif event.key == pygame.K_UP:
		plane.moving_up = False





def update_screen(settings,screen,plane):
	 screen.fill(settings.bg_color)

	 plane.blitme()

	 pygame.display.flip()

