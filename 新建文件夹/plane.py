import pygame
from pygame.sprite import Sprite 


class Plane(Sprite):
	def __init__(self,settings,screen):
		super(Plane,self).__init__()

		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('images/plane.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
								#xxx.rect.size[0],[1] 分别是矩形的宽度和高度
		self.rect.centery = self.screen_rect.size[1] - (self.rect.size[1] / 2)

		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)


		self.moving_right = False
		self.moving_left = False
		self.moving_down = False
		self.moving_up = False


	def blitme(self):
		self.screen.blit(self.image,self.rect)	#两个参数 图像和它的矩形

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.settings.plane_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.settings.plane_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.settings.plane_speed_factor 
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.settings.plane_speed_factor 				

		self.rect.centerx = self.centerx
		self.rect.centery = self.centery