import pygame
import os
import requests

def read_file(filename):
	with open(filename) as f:
	    lines = f.readlines()

	return lines

def getData():
	
	lParameter = read_file("template.txt")
	data = {}

	for parameter in lParameter:
		param = parameter.split('=')
		key_data = param[0].strip()
		value_data = param[1].strip().lower().replace("\n","")
		if key_data == 'nama_cabang':
			value_data = value_data.upper()

	#	data[param[0].strip()] = param[1].strip().replace("\n","")
		data[key_data] = value_data

	return data

def getTeam():
	
	lParameter = read_file("team.txt")
	team = {}

	for parameter in lParameter:
		param = parameter.split(',')
		key_data = param[0].strip()
		value_data = param[1].strip().lower().replace("\n","")
	
		team[key_data] = value_data

	return team

def crop_img(image,posisi):

	d = posisi

	gambar = pygame.image.load(os.path.join("../Raw_Foto",image))

	left = 0
	top = 0
	background = pygame.Surface((0, 0))

	h_gambar = gambar.get_height()
	w_gambar = gambar.get_width()
	
	print w_gambar,h_gambar
	if w_gambar > h_gambar :
		h = h_gambar
		w = h
		print "landscape"
		print w,h
		background = pygame.Surface((w, h))
		#gambar = pygame.transform.rotate(gambar,90)
		if d.strip().lower() == 'left':
			top = 0
			left = 0
		if d.strip().lower() == 'right':
			top = 0
			left = w_gambar - w
		if d.strip().lower() == 'center':
			top = 0
			left = (w_gambar - w)/2


	else:
		w = w_gambar
		h = w
		print "portrait"
		print w,h
		#gambar = pygame.transform.rotate(gambar,90)
		background = pygame.Surface((w, h))
		if d.strip().lower() == 'left':
			top = 0
			left = 0
		if d.strip().lower() == 'right':
			top = 0
			left = w_gambar - w
		if d.strip().lower() == 'center':
			top = 0
			left = (w_gambar - w)/2

	background.blit(gambar, (0, 0), (left, top, w, h))

	scaled = pygame.transform.scale(background,(2000,2000))

	return scaled

