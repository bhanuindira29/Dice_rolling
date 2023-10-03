import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
DICE_SIZE = 200
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

def draw_dice(value):
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (100, 100, DICE_SIZE, DICE_SIZE), 2)
    
    if value == 1:
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 10)
    elif value == 2:
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, 3 * HEIGHT // 4), 10)
    elif value == 3:
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, 3 * HEIGHT // 4), 10)
    elif value == 4:
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, 3 * HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, 3 * HEIGHT // 4), 10)
    elif value == 5:
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, 3 * HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, 3 * HEIGHT // 4), 10)
    elif value == 6:
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 2), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 2), 10)
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, 3 * HEIGHT // 4), 10)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, 3 * HEIGHT // 4), 10)
    
    pygame.display.flip()

def roll_die():
    return random.randint(1, 6)

# Main loop
rolling = False
value = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not rolling:
            rolling = True
            value = roll_die()
    
    if rolling:
        draw_dice(random.randint(1, 6))
        pygame.time.delay(100)  # Delay for a short time to make it look like rolling
        rolling = False
        draw_dice(value)
    
    pygame.display.update()