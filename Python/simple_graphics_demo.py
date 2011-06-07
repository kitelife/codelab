import pygame

pygame.init()

#Define the colors we will use in RGB format
black = [0,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
red = [255,0,0]

pi = 3.141592653

#Set the height and width of the screen
size = [400,500]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

#Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

while done == False:
	clock.tick(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(white)
	pygame.draw.line(screen,green,[0,0],[100,100],5)

	y_offset = 0
	while y_offset < 100:
		pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
		y_offset = y_offset+10
	
	font = pygame.font.Font(None,25)

	text = font.render("My text",True,black)

	screen.blit(text,[250,250])

	pygame.draw.rect(screen,black,[20,20,250,100],2)

	pygame.draw.ellipse(screen,black,[20,20,250,100],2)


	pygame.draw.arc(screen,black,[20,220,250,200],0,pi/2,2)
	pygame.draw.arc(screen,green,[20,220,250,200],pi/2,pi,2)
	pygame.draw.arc(screen,blue,[20,220,250,200],pi,3*pi/2,2)
	pygame.draw.arc(screen,red,[20,220,250,200],3*pi/2,2*pi,2)

	pygame.draw.polygon(screen,black,[[100,100],[0,200],[200,200]],5)

	pygame.display.flip()

pygame.quit()
