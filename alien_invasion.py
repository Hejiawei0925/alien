import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()	#设置屏幕大小 背景色 飞船速度
	#创建一个窗口 然后把上一行的属性传给屏幕
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	#窗口的名字
	pygame.display.set_caption("外星人入侵")
	#创建play纽扣
	play_button = Button(ai_settings,screen,'Play')
	#统计信息的实例
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一艘飞船实例
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建外星人
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,
			ship,aliens,bullets)	
		
		if stats.game_active: 
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)

run_game()