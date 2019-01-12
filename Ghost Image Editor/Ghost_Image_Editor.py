# ============================================================
#
# Student Name (as it appears on cuLearn): Justin Tam 
# Student ID (9 digits in angle brackets): <101078802>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

import pygame
pygame.init()
#prompt for instructions
instruction = input ("Do you require instructions? (Enter Yes if you require otherwise it will continue)")
if instruction.upper() == "YES":
	print ("This program merges two images together. You will provide the filenames of two images. One image being a background image and the second image will be a ghost behind a green background. The program will place the ghost on top of the background at a given coordinate and give it a semi-translucent effect.")
	
#get filenames
background_img = pygame.image.load (input("Name of background file: "))
ghost = pygame.image.load (input ("Name of ghost file: "))

#get dimensions of images and display background
(width,height)= background_img.get_rect().size
frame = pygame.display.set_mode((width,height))
frame.blit (background_img, (0,0))
(ghost_width,ghost_height)= ghost.get_rect().size
pygame.display.update()
ghost_width = int(ghost_width)
ghost_height = int (ghost_height)

#get coordinates of where to place the ghost
while True:
	center_x = int(input ("What is the x-coordinate that you would like the ghost to center? "))
	center_y = int(input ("What is the y-coordinate that you would like the ghost to center? "))
	if center_x < 0 or center_x > width or center_y < 0 or center_y > height: #validation
		print ("Please try again")
	else :
		break

#process of pixels
for i in range (0,ghost_width):
	for j in range (0,ghost_height):
		#get rgb values of background and ghost
		(ghost_red,ghost_green,ghost_blue,a)= ghost.get_at((i,j))
		if (center_x+i-ghost_width/2)>=-1 and (center_y+j-ghost_height/2)>=-1 :
			(background_red,background_green,background_blue,a) = background_img.get_at ((int(center_x+i-ghost_width/2),int(center_y+j-ghost_height/2)))
			#if pixel is green make it same as background
			if (ghost_green == 255) and (ghost_red == 0) and (ghost_blue == 0):
				ghost.set_at ((i,j),(background_red,background_green,background_blue))
			else: #average values of background and ghost rgb values to make semi transparent effect
				ghost.set_at ((i,j),((background_red + ghost_red )/2,(background_blue + ghost_blue )/2,(background_green + ghost_green )/2))
#update display with ghost
frame.blit (ghost,(center_x-(ghost_width/2),center_y-(ghost_height/2)))
pygame.display.update()
#allow program to exit with x in corner
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()
