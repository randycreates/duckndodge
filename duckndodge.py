from re import X

import pygame
import random

# Starts game system and creates window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Define player size & position
player = pygame.Rect(375, 250, 50, 50)

# Define bottles
bottle = pygame.Rect(350, 0, 10, 10)
bottle2 = pygame.Rect(375, 600, 10, 10)

# Fix frame rate with clock
clock = pygame.time.Clock()

running = True
lost = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # Draws white screen
    screen.fill("white")

    # Asigning movement for left & right arrow
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x = player.x - 5
    if keys[pygame.K_RIGHT] and player.right < 800:
        player.x = player.x + 5
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # Bottle falling from top of screen
    bx = random.randint(2, 7)
    bottle.y = bottle.y + bx
    if bottle.y > 600:
        bottle.y = 0
        bottle.x = random.randint(0, 790)

    # Bottle coming from bottom of screen
    by = random.randint(2, 7)
    bottle2.y = bottle2.y - by
    if bottle2.y < 0:
        bottle2.y = 600
        bottle2.x = random.randint(0, 790)

    if player.colliderect(bottle) or player.colliderect(bottle2):
        print("Game over")
        lost = True
        running = False
    
    # Draws player in blue on screen
    pygame.draw.rect(screen, "blue", player)
    
    # Draws falling bottles
    pygame.draw.rect(screen, "red", bottle)
    pygame.draw.rect(screen, "red", bottle2)
    pygame.display.flip()
    clock.tick(60)

# Game over message when lost
if lost:
	screen.fill("white")
	font = pygame.font.Font(None, 48)
	text_surface = font.render(
	    "Bottle to the face! Your're going to the hospital.", 
	    True, "black")
	sad = font.render(":(", True, "black")

	text_rect = text_surface.get_rect(center=(400, 300))
	sad_rect = sad.get_rect(center=(400, 350))

	screen.blit(text_surface, text_rect)
	screen.blit(sad, sad_rect)
	pygame.display.flip()

	waiting = True
	while waiting:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            waiting = False
else:
    pygame.quit()