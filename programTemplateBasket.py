import pygame
import constant as c
import sys
from math import floor
import time
import utility as u
#import excel as ex

def getTeam(nama_file):

	team = {}

	with open(nama_file, "r") as ins:
	    for line in ins:
	    	pemain = {}
	        s = line.split(",")
	        if s[0].upper().strip() == "LOGO":
	        	team['logo'] = s[1].replace("\n","")
	        else:
	        	pass
	return team

def drawBoxTransparent(canvas, top,left, width,height, alpha, color):

	#print top, left
	s = pygame.Surface((width,height))  # the size of your rect
	s.set_alpha(alpha)                # alpha level
	s.fill(color)           # this fills the entire surface
	canvas.blit(s, (left,top))


def getMenuUtama(team_home,team_away,skor_home,skor_away):
	#variabel
	x = 0
	y = 0

	width_cabang = 1627
	height_cabang = 226

	left_cabang = 203
	top_cabang = 197

	width_title = 1459
	height_title = 148

	left_title = 269
	top_title = 442

	width_score = 514
	height_score = 484

	left_score_home = 230
	top_score_home = 1349

	left_score_away = 1286
	top_score_away = 1349

	width_team = 667
	height_team = 193

	left_team_away = 1208
	top_team_away = 1752

	left_team_home = 155
	top_team_home = 1752

	left_final = 848
	top_fial = 1502


	hijau = (0,255,126)
	putih = (255,255,255)
	hitam = (0,0,0)
	merah = (255,26,26)
	kuning = (255,255,0)


	#data = ex.getData()
	team = u.getTeam()

	nama_cabang = c.CABANG
	team_home = team_home
	team_away = team_away
	score_home = skor_home
	score_away = skor_away
	title = "| " + str(team_home).upper() + " VS " + str(team_away).upper() + " |"
	#por = c.por_FILENAME
	background_img = c.BACK_FILENAME
	final = pygame.image.load("final.png")
	background = pygame.image.load(background_img)


	# gambar di canvas
	pygame.init()
	width = 2000
	height = 2000
	canvas = pygame.display.set_mode((width, height))
	score_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_POINTS_INT_SIZE)
	team_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_TEAM_STR_SIZE)
	title_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_TITLE_STR_SIZE)
	cabang_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_CABANG_STR_SIZE)


	done = False

#while not done:

	print_score_home = score_font.render(score_home, 1, putih)
	print_score_away = score_font.render(score_away, 1, putih)
	print_nama_cabang_shadow = cabang_font.render(nama_cabang, 1, hitam)
	print_nama_cabang = cabang_font.render(nama_cabang, 1, putih)
	print_title_shadow = title_font.render(title, 1, hitam)
	print_title = title_font.render(title, 1, putih)
	print_team_home = team_font.render(team_home, 1, putih)
	print_team_away = team_font.render(team_away, 1 , putih)

	x_cabang = left_cabang + ((width_cabang - print_nama_cabang.get_width())/2)
	y_cabang = top_cabang + ((height_cabang - print_nama_cabang.get_height())/2)

	x_title = left_title + ((width_title - print_title.get_width())/2)
	y_title = top_title + ((height_title - print_title.get_height())/2)

	x_score_home = left_score_home + ((width_score - print_score_home.get_width())/2)
	y_score_home = top_score_home + ((height_score - print_score_home.get_height())/2)

	x_score_away = left_score_away + ((width_score - print_score_away.get_width())/2)
	y_score_away = top_score_away + ((height_score - print_score_away.get_height())/2)

	x_team_home = left_team_home + ((width_team - print_team_home.get_width())/2)
	y_team_home = top_team_home + ((height_team - print_team_home.get_height())/2)

	x_team_away = left_team_away + ((width_team - print_team_away.get_width())/2)
	y_team_away = top_team_away + ((height_team - print_team_away.get_height())/2)
	#width_pemain = print_nama_cabang.get_width()
	#height_pemain = print_nama_cabang.get_height()
	#left_pemain = width - width_pemain - 120
	#top_pemain = 150

	canvas.blit(background, (0,0))
	#drawBoxTransparent(canvas,50,50,logo_por.get_width(),logo_por.get_height(),128,putih)
	#canvas.blit(logo_por, (50,50))
	canvas.blit(print_nama_cabang_shadow, (x_cabang + 3,y_cabang + 3))
	canvas.blit(print_nama_cabang, (x_cabang,y_cabang))
	canvas.blit(print_title_shadow, (x_title + 3,y_title + 3))
	canvas.blit(print_title, (x_title,y_title))
	canvas.blit(print_score_home, (x_score_home,y_score_home))
	canvas.blit(print_score_away, (x_score_away,y_score_away))
	canvas.blit(final, (left_final, top_fial))
	canvas.blit(print_team_home, (x_team_home, y_team_home))
	canvas.blit(print_team_away, (x_team_away, y_team_away))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		

		pygame.display.flip()

	file_name = nama_cabang.title() + "_" + team_home.title() + " vs " + team_away.title() + "_" + (time.strftime("%d-%m-%Y")) + ".png"
	print file_name
	# save ke file
	pygame.image.save(canvas, "../foto_result/"+ c.CABANG"/"+file_name)
	# send to rabbitMQ
	#por.kirim_gambar("subs.png","subs.png")
	#sys.exit(0)
	return