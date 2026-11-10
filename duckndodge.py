"""Duck n Doge - a single-player dodge game set in a night club.
Move left and right to avoid thrown bottles. Survive 45 seconds to win."""

# pylint: disable=no-member

import random

import pygame

# Starts game system and creates window
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Define player position & size
player = pygame.Rect(300, 300, 15, 15)

# Define random number of bottles in wave
bottles = []


def new_batch():
    """Clear the curent bottles and builds new wave with random count"""
    bottles.clear()
    num_of_bottles = random.randint(1, 12)

    for i in range(num_of_bottles):
        bottles.append([pygame.Rect(random.randint(0, 590), 0, 10, 10), 1])
        bottles.append([pygame.Rect(random.randint(0, 590), 600, 10, 10), -1])


new_batch()

# Fix frame rate with clock
clock = pygame.time.Clock()

# Club lighting
colors = ["black", "white"]
color_index = 0
frame_count = 0


# Reset game play for new round after loss
def reset_game():
    """Reset player and bottle positions for a new round."""
    player.x = 300
    player.y = 300
    for b, direction in bottles:
        if direction == 1:
            b.y = 0
        else:
            b.y = 600
        b.x = random.randint(0, 590)


# Timmer records time when game begins
start_time = pygame.time.get_ticks()

# Creating the timer font
timer_font = pygame.font.Font(None, 25)

# Game state
state = "title"

# Main game loop - handles events, updates states, draws the current screen
while True:
    # Handle quit and key press events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        # State transistions on key press
        if event.type == pygame.KEYDOWN:
            if state == "title":
                state = "directions"
            elif state == "directions":
                state = "playing"
                start_time = pygame.time.get_ticks()
            elif state == "game_over":
                if event.key == pygame.K_y:
                    reset_game()
                    state = "playing"
                    start_time = pygame.time.get_ticks()
            elif state == "win":
                if event.key == pygame.K_y:
                    reset_game()
                    start_time = pygame.time.get_ticks()
                    state = "playing"

    # Active gameplay
    if state == "playing":
        elapsed = (pygame.time.get_ticks() - start_time) / 1000

        if elapsed >= 45:
            state = "win"
            continue

        # Draws colored screen
        frame_count += 1
        if frame_count % 30 == 0:  # Every 30 frames (half a second at 60fps)
            color_index = (color_index + 1) % len(colors)
        screen.fill(colors[color_index])

        # Asigning movement for left & right arrow
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x = player.x - 5
        if keys[pygame.K_RIGHT] and player.right < 600:
            player.x = player.x + 5
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit

        # Falling bottles
        speed = random.randint(2, 9)
        for b, direction in bottles:
            b.y += speed * direction

        # Reset falling bottle count
        all_off = all(b.y > 600 or b.y < 0 for b, d in bottles)
        if all_off:
            new_batch()

        # End the game if the player touches a bottle
        for b, direction in bottles:
            if player.colliderect(b):
                state = "game_over"

        # Draws player in blue on screen
        pygame.draw.rect(screen, "blue", player)

        # Draws falling bottles
        for b, direction in bottles:
            pygame.draw.rect(screen, "red", b)

        # Calculates time left in game play
        time_left = max(0, 45 - int(elapsed))
        # Renders countdown timer in top-left corner
        timer_text = timer_font.render(f"{time_left} 's", True, "crimson")
        screen.blit(timer_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Title screen - shown first, key advances to directions
    elif state == "title":
        screen.fill("black")
        font1 = pygame.font.Font(None, 50)
        title = font1.render("Welcome to Club Velocity!", True, "fuchsia")
        font2 = pygame.font.Font(None, 30)
        warning = font2.render(
            "Warning: this game features a flashing screen", True, "white"
        )
        start = font2.render("Press any key to continue", True, "white")

        title_rect = title.get_rect(center=(300, 250))
        warn_rect = warning.get_rect(center=(300, 325))
        start_rect = start.get_rect(center=(300, 390))

        screen.blit(title, title_rect)
        screen.blit(warning, warn_rect)
        screen.blit(start, start_rect)
        pygame.display.flip()

    # Directions screen - explains game play, key advances to game start
    elif state == "directions":
        screen.fill("black")
        font1 = pygame.font.Font(None, 42)
        d1 = font1.render("A fight has broken out in the club", True, "red")
        d2 = font1.render("& bottles are flying!!", True, "red")
        font2 = pygame.font.Font(None, 32)
        d3 = font2.render("Use the right & left arrow keys to", True, "white")
        d4 = font2.render(
            "avoid being hit for 45 seconds to win.", True, "white"
            )
        font3 = pygame.font.Font(None, 30)
        d5 = font3.render("Press any key to start & be ready!", True, "white")

        d1_rect = d1.get_rect(center=(300, 225))
        d2_rect = d2.get_rect(center=(300, 255))
        d3_rect = d3.get_rect(center=(300, 325))
        d4_rect = d4.get_rect(center=(300, 355))
        d5_rect = d5.get_rect(center=(300, 425))

        screen.blit(d1, d1_rect)
        screen.blit(d2, d2_rect)
        screen.blit(d3, d3_rect)
        screen.blit(d4, d4_rect)
        screen.blit(d5, d5_rect)
        pygame.display.flip()

    # Game over screen - player hit, instructions to restart
    elif state == "game_over":
        screen.fill("white")
        font1 = pygame.font.Font(None, 42)
        oh_no = font1.render("OH NO!", True, "red")
        l1 = font1.render("You took a bottle to the face.", True, "black")
        l2 = font1.render(":- (", True, "crimson")
        l2_ro = pygame.transform.rotate(l2, 270)
        font2 = pygame.font.Font(None, 38)
        l3 = font2.render("You're going to the hospital", True, "black")
        l4 = font2.render("...but you have no insurance.", True, "black")
        font2 = pygame.font.Font(None, 32)
        play_again = font2.render("Play again? press y", True, "black")

        oh_rect = oh_no.get_rect(center=(300, 150))
        l1_rect = l1.get_rect(center=(300, 210))
        l2_rect = l2_ro.get_rect(center=(300, 260))
        l3_rect = l3.get_rect(center=(300, 310))
        l4_rect = l4.get_rect(center=(300, 350))
        playa_rect = play_again.get_rect(center=(300, 425))

        screen.blit(oh_no, oh_rect)
        screen.blit(l1, l1_rect)
        screen.blit(l2_ro, l2_rect)
        screen.blit(l3, l3_rect)
        screen.blit(l4, l4_rect)
        screen.blit(play_again, playa_rect)
        pygame.display.flip()

    # Win screen - player survied 60 seconds, instrutions to restart
    elif state == "win":
        screen.fill("black")
        font1 = pygame.font.Font(None, 48)
        win1 = font1.render(
            "I see you've done this before...", True, "limegreen"
        )
        win2 = font1.render("Nice Job", True, "limegreen")
        font2 = pygame.font.Font(None, 30)
        start = font2.render("To play again, press y", True, "white")

        win1_rect = win1.get_rect(center=(300, 250))
        win2_rect = win2.get_rect(center=(300, 300))
        start_rect = start.get_rect(center=(300, 390))

        screen.blit(win1, win1_rect)
        screen.blit(win2, win2_rect)
        screen.blit(start, start_rect)
        pygame.display.flip()
