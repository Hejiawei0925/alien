class Settings(object):
	
	def __init__(self):

		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.plane_speed_factor = 3	

	def initialize_dynamic_settings(self):
		self.plane_speed_factor = 3	
		
