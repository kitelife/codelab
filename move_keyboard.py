import pygame

black  = [0,0,0]
white = [255,255,255]
blue = [50,50,255]
dkgreen = [0,100,0]
green = [0,255,0]
red = [255,0,0]
purple = [0xBF,0x0F,0xB5]
brown = [0x55,0x33,0x00]

def draw_background(screen):
	screen.fill(white)

def draw_item(screen,x,y):
	pygame.draw.rect(screen,green,[0+x,0+y,30,10],0)
	pygame.draw.circle(screen,black,[15+x,15+y],7,0)
	
pygame.init()


screen = pygame.display.set_mode((640,480))

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

clock = pygame.time.Clock()

done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -3
			if event.key == pygame.K_RIGHT:
				x_speed = 3
			if event.key == pygame.K_UP:
				y_speed = -3
			if event.key == pygame.K_DOWN:
				y_speed = 3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed

	draw_background(screen)

	draw_item(screen,x_coord,y_coord)

	pygame.display.flip()
	clock.tick(20)

pygame.quit()
