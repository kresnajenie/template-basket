import pygame
import constant as c
import sys
from math import floor
import time

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

def getMenuUtama(team_home, team_away, file_foto):
	#variabel
	x = 0
	y = 0
	x_kotak = 448
	y_kotak = 448

	x_skor = 320
	y_skor = 384

	left_skor_home = 508
	top_skor_home = 1444

	left_skor_away = 1200
	top_skor_away = 1444

	left_home = 76
	top_home = 1444

	left_away = 1496
	top_away = 1444

	x_final = 376
	y_final = 296

	left_final = 820
	top_final = 1488

	hijau = (0,255,126)
	putih = (255,255,255)
	hitam = (0,0,0)
	merah = (255,26,26)
	kuning = (255,255,0)

	
	nama_pemain = raw_input("Nama Pemain ").upper()	
	points = raw_input("Points MVP berapa? ").lower().strip()
	assists = raw_input("Assists MVP berapa? ").lower().strip()
	rebounds = raw_input("Rebounds MVP berapa? ").lower().strip()
	steals = raw_input("Steals MVP berapa? ").lower().strip()
	blocks = raw_input("Blocks MVP berapa? ").lower().strip()
	score_home = raw_input("Score Home? ").lower().strip()
	score_away = raw_input("Score Away? ").lower().strip()


	foto = pygame.image.load(file_foto)
	final = pygame.image.load("final.png")

	if team_home == "kanisius":
		logo_home = pygame.image.load("cc.png")
	elif team_home == "smabel":
		logo_home = pygame.image.load("smabel.png")
	elif team_home == "smpn74":
		logo_home = pygame.image.load("smpn74.png")
	elif team_home == "smpn216":
		logo_home = pygame.image.load("smpn216.png")
	elif team_home == "p7":
		logo_home = pygame.image.load("p7.png")
	if team_home == "ipeka":
		logo_home = pygame.image.load("ipeka.png")


	if team_away == "kanisius":
		logo_away = pygame.image.load("cc.png")
	elif team_away == "smabel":
		logo_away = pygame.image.load("smabel.png")
	elif team_away == "smpn74":
		logo_away = pygame.image.load("smpn74.png")
	elif team_away == "smpn216":
		logo_away = pygame.image.load("smpn216.png")
	elif team_away == "p7":
		logo_away = pygame.image.load("p7.png")
	if team_away == "ipeka":
		logo_away = pygame.image.load("ipeka.png")


	# gambar di canvas
	pygame.init()
	width = 2000
	height = 2000
	canvas = pygame.display.set_mode((width, height))
	score_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_SCORE_SIZE)
	pemain_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_PEMAIN_SIZE)
	points_int_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_POINTS_INT_SIZE)
	points_str_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_POINTS_STR_SIZE)
	astreb_int_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_ASTREB_INT_SIZE)
	astreb_str_font = pygame.font.Font(c.FONT_FILENAME, c.FONT_ASTREB_STR_SIZE)

	#kotak = pygame.Rect(0, 0, width, height)
	#arrow_up = pygame.image.load("arrow.png")
	#arrow_down = pygame.image.load("arrows.png")
	# total score dictionary

	

	x_tulisan = 288
	y_tulisan = 120
	y_tulisan_margin = 260

	x_angka = 84
	y_angka = 80
	y_angka_margin = 260

	done = False

#while not done:

	print_points_int = points_int_font.render(points, 1, putih)
	print_points_str = points_str_font.render("PTS", 1, putih)
	print_assists_int = astreb_int_font.render(assists, 1, putih)
	print_assists_str = astreb_str_font.render("AST", 1, putih)
	print_rebounds_int = astreb_int_font.render(rebounds, 1, putih)
	print_rebounds_str = astreb_str_font.render("REB", 1, putih)
	print_steals_int = astreb_int_font.render(steals, 1, putih)
	print_steals_str = astreb_str_font.render("STL", 1, putih)
	print_blocks_int = astreb_int_font.render(blocks, 1, putih)
	print_blocks_str = astreb_str_font.render("BLK", 1, putih)
	print_score_home = score_font.render(score_home, 1, putih)
	print_score_away = score_font.render(score_away, 1, putih)
	print_nama_pemain = pemain_font.render(nama_pemain, 1, putih)

	x_logo_home = left_home + ((x_kotak - logo_home.get_width())/2)
	y_logo_home = top_home + ((y_kotak - logo_home.get_height())/2)

	x_logo_away = left_away + ((x_kotak - logo_away.get_width())/2)
	y_logo_away = top_away + ((y_kotak - logo_away.get_height())/2)

	x_skor_home = left_skor_home + ((x_skor - print_score_home.get_width())/2)
	y_skor_home = top_skor_home + ((y_skor - print_score_home.get_height())/2)

	x_skor_away = left_skor_away + ((x_skor - print_score_away.get_width())/2)
	y_skor_away = top_skor_away + ((y_skor - print_score_away.get_height())/2)

	x_final_last = left_final + ((x_final - final.get_width())/2)
	y_final_last = top_final + ((y_final - final.get_height())/2)

	width_pemain = print_nama_pemain.get_width()
	height_pemain = print_nama_pemain.get_height()
	left_pemain = width - width_pemain
	top_pemain = 200

	canvas.blit(foto, (0,0))
	canvas.blit(logo_home, (x_logo_home,y_logo_home))
	canvas.blit(logo_away, (x_logo_away,y_logo_away))
	canvas.blit(final, (x_final_last,y_final_last))
	canvas.blit(print_nama_pemain, (left_pemain,top_pemain))

	canvas.blit(print_score_home, (x_skor_home, y_skor_home))
	canvas.blit(print_score_away, (x_skor_away, y_skor_away))

	if points == "0":
		pass
	else:
		canvas.blit(print_points_int, (x_angka, y_angka))
		canvas.blit(print_points_str, (x_tulisan, y_tulisan))
		y_angka = y_angka + y_angka_margin
		y_tulisan = y_tulisan + y_tulisan_margin
		x_angka = x_angka + 20
		#print points

	if assists == "0":
		pass
	else:
		canvas.blit(print_assists_int, (x_angka, y_angka))
		canvas.blit(print_assists_str, (x_tulisan, y_tulisan))
		y_angka = y_angka + y_angka_margin
		y_tulisan = y_tulisan + y_tulisan_margin

	if rebounds == "0":
		pass
	else:
		canvas.blit(print_rebounds_int, (x_angka, y_angka))
		canvas.blit(print_rebounds_str, (x_tulisan, y_tulisan))
		y_angka = y_angka + y_angka_margin
		y_tulisan = y_tulisan + y_tulisan_margin

	if steals == "0":
		pass
	else:
		canvas.blit(print_steals_int, (x_angka, y_angka))
		canvas.blit(print_steals_str, (x_tulisan, y_tulisan))
		y_angka = y_angka + y_angka_margin
		y_tulisan = y_tulisan + y_tulisan_margin

	if blocks == "0":
		pass
	else:
		canvas.blit(print_blocks_int, (x_angka, y_angka))
		canvas.blit(print_blocks_str, (x_tulisan, y_tulisan))
		y_angka = y_angka + y_angka_margin
		y_tulisan = y_tulisan + y_tulisan_margin

	x_tulisan = 288
	y_tulisan = 120
	y_tulisan_margin = 140

	x_angka = 84
	y_angka = 80
	y_angka_margin = 60

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		

		pygame.display.flip()

	file_name = nama_pemain.title() + "_" + team_home.title() + " vs " + team_away.title() + "_" + (time.strftime("%d-%m-%Y")) + ".png"
	print file_name
	# save ke file
	pygame.image.save(canvas, file_name)
	# send to rabbitMQ
	#por.kirim_gambar("subs.png","subs.png")
	sys.exit(0)
	return