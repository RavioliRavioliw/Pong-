import pygame as pyg
import sys
from pygame.locals import *
import buton

pyg.init()


win_reso_width = 900
win_reso_height = 600

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
light_green =(211, 255, 185)
gray = (128, 128, 128)
score_1 = 0

screen = pyg.display.set_mode((win_reso_width, win_reso_height))
pyg.display.set_caption("pog game")
clock = pyg.time.Clock()
#-------------
mains = pyg.image.load("img/main_menu.png").convert_alpha()
start = pyg.image.load("img/start_button.png").convert_alpha()
#-------------

start_btn = buton.Button(300, 500, start, 0.5)

background = pyg.Surface(screen.get_size())
background = background.convert()
background.fill((light_green))





#drawing borders
def borders():
	pyg.draw.line(screen, black, (0,0), (win_reso_width, 0), 20)
	pyg.draw.line(screen, black, (win_reso_width, 0), (win_reso_width, win_reso_height), 20)
	pyg.draw.line(screen, black, (win_reso_width, win_reso_height), (0, win_reso_height), 20)
	pyg.draw.line(screen, black, (0, win_reso_height), (0,0), 20)
	pyg.draw.line(screen, gray, (win_reso_width//2 + 10, 10), (win_reso_width//2 +10, win_reso_height -10),  1)





#-------------------------------------------------------------
player_1 = pyg.Rect(10, 10, 8, 100)
player_2 = pyg.Rect( win_reso_width -17, 10, 8, 100)
balll = pyg.Rect(win_reso_width//2 -15, win_reso_height //2 -15, 20, 20)
#--------------------------
fonts = pyg.font.Font("freesansbold.ttf", 32)
fonts2 = pyg.font.Font("freesansbold.ttf", 20)

score_1 = 0
score_2 = 0

#----------------------------------------

def main():

	screen.blit(background, (0, 0))

	while True:

		screen.blit(mains, (0, 0))
		if start_btn.draw(screen):
			play(score_1, score_2)
			break



		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()


		clock.tick(60)
		pyg.display.update()
	return






def play(score_1, score_2):
	screen.blit(background, (0, 0))
	borders()
	
	speed_y = 0
	speed_y_2 = 0

	balll_speed_x = 4
	balll_speed_y = 4


	ball_start = False

	go_menu = False


	while True:
		screen.blit(background, (0, 0))
		borders()
		text = fonts.render(f'{score_1}', False, gray)
		text2 = fonts.render(f'{score_2}', False, gray)
		#---------------------------------------------------
		p1win = fonts.render("the player 1 has won", False, gray)
		p2win = fonts.render("the player 2 has won", False, gray)
		#---------------------------------------------------
		space = fonts.render("Press Space to start", False, gray)
		rest = fonts.render("Press 'R' to restart the game", False, gray)
		pla_1_c = fonts2.render("player one controls: E and D", False, gray)
		pla_2_c = fonts2.render("player two controls: up arrow and down arrow", False, gray)


		if ball_start != True and score_1 == 0 and score_2 == 0:
			screen.blit(space, (win_reso_width// 2 - 150, win_reso_height // 2))
			screen.blit(pla_1_c, (20, 500))
			screen.blit(pla_2_c, (420, 500))




		if score_2 == 10:
			ball_start = False
			screen.blit(p1win, (win_reso_width// 2 - 150, win_reso_height // 2))
			screen.blit(rest, (win_reso_width// 2 - 130, win_reso_height // 2 + 100))

		if score_1 == 10:
			ball_start = False
			screen.blit(p2win, (win_reso_width// 2 - 150, win_reso_height // 2))
			screen.blit(rest, (win_reso_width// 2 - 130, win_reso_height // 2 + 100))

		if ball_start == False and go_menu == True:
			main()
			break




		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()

			#player move
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					speed_y += 4
				if event.key == K_UP:
					speed_y += -4
				if event.key == K_d:
					speed_y_2 += 4
				if event.key == K_e:
					speed_y_2 += -4
				if event.key == K_SPACE:
					ball_start = True
				if event.key == K_r:
					go_menu = True
					
					
			elif event.type == KEYUP:
				if event.key == K_DOWN or event.key == K_UP:
					speed_y = 0
				if event.key == K_e or event.key == K_d:
					speed_y_2 = 0
		


		#----------------------------------------------------------------------------------------------------

		if ball_start:
			balll.x += balll_speed_x
			balll.y += balll_speed_y
		else:
			balll.x = win_reso_width//2 -15
			balll.y = win_reso_height //2 -15
		#------------------------------------------------------------------
		#if player_1.y 
		#---

		pyg.draw.rect(screen, (117, 8, 129), player_1)
		pyg.draw.rect(screen, (117, 8, 129), player_2)
		pyg.draw.ellipse(screen, (127, 127, 127), balll)
		screen.blit(text, (win_reso_width//2 + 20, 20))
		screen.blit(text2, (win_reso_width//2 -16, 20))
		
		
		#collide efects
		if balll.colliderect(player_2):
			balll_speed_x *= -1

		if balll.colliderect(player_1):
			balll_speed_x *= -1

		#-----------------------------
		if score_1 == 5 or score_2 == 5:
			balll_speed_x += 1
			balll_speed_y += 1




		#----------------
		# player_2 properties
		player_2.y += speed_y
		if player_2.y <= 10:
			player_2.y = 10
		if player_2.bottom >= win_reso_height -9:
			player_2.bottom = win_reso_height -9
		# player_1 properties

		player_1.y += speed_y_2
		if player_1.y <= 10:
			player_1.y = 10
		if player_1.bottom >= win_reso_height -9:
			player_1.bottom = win_reso_height -9

		#---------------
		
		#ball properties
		if balll.y <= 0:
			balll.y = 0
		if balll.bottom >= win_reso_height -9 or balll.top <= 10:
			balll_speed_y *= -1
		if balll.right >= win_reso_width -9:
			balll_speed_x *= -1
			score_2 += 1
		if balll.left <= 10:
			balll_speed_x *= -1
			score_1 += 1

		#----------------

		clock.tick(60)
		pyg.display.update()
	return


if __name__ == '__main__':
	main()

