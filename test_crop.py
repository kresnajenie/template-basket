pygame.init()
	width = 2000
	height = 2000
	canvas = pygame.display.set_mode((width, height))
	
	scale(Surface, (width, height), DestSurface = None)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		

		pygame.display.flip()
	# save ke file
	pygame.image.save(canvas, "test.png")
	# send to rabbitMQ
	#por.kirim_gambar("subs.png","subs.png")
	sys.exit(0)
	