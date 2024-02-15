import pygame
import sys

# Constants
GRID_SIZE = 15
DOT_RADIUS = 5
LINE_WIDTH = 5
SCREEN_SIZE = 2 * DOT_RADIUS * GRID_SIZE + LINE_WIDTH * (GRID_SIZE - 1)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Dots and Boxes")

# Game state
grid = [[False] * (GRID_SIZE - 1) for _ in range(GRID_SIZE - 1)]
player_turn = 1
player_scores = [0, 0]

# Function to draw the grid
def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.circle(screen, BLACK, (i * 2 * DOT_RADIUS + DOT_RADIUS, j * 2 * DOT_RADIUS + DOT_RADIUS), DOT_RADIUS)

    for i in range(GRID_SIZE - 1):
        for j in range(GRID_SIZE - 1):
            if grid[i][j]:
                pygame.draw.rect(screen, BLACK, (i * 2 * DOT_RADIUS + DOT_RADIUS, j * 2 * DOT_RADIUS + DOT_RADIUS, 2 * DOT_RADIUS, 2 * DOT_RADIUS))

# Function to draw a line between two dots
def draw_line(dot1, dot2):
    pygame.draw.line(screen, BLACK, dot1, dot2, LINE_WIDTH)

# Function to check if a box is completed
def check_box_completed(x, y):
    return grid[x][y] and grid[x + 1][y] and grid[x][y + 1] and grid[x + 1][y + 1]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the clicked position
            x, y = event.pos
            i = x // (2 * DOT_RADIUS)
            j = y // (2 * DOT_RADIUS)

            # Check if it's a valid dot
            if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE:
                print(f"Clicked on dot ({i}, {j})")

                # Check if the line is already drawn
                if i % 2 == j % 2:  # Horizontal line
                    line_x = i // 2
                    line_y = (j - 1) // 2
                else:  # Vertical line
                    line_x = (i - 1) // 2
                    line_y = j // 2

                if not grid[line_x][line_y]:
                    grid[line_x][line_y] = True

                    # Check for completed boxes
                    completed_boxes = 0
                    for x in range(GRID_SIZE - 1):
                        for y in range(GRID_SIZE - 1):
                            if check_box_completed(x, y):
                                completed_boxes += 1
                                if player_turn == 1:
                                    player_scores[0] += 1
                                else:
                                    player_scores[1] += 1

                    # Switch player turn if no boxes completed
                    if completed_boxes == 0:
                        player_turn = 3 - player_turn  # Toggle between 1 and 2

    # Draw the grid and lines
    screen.fill(WHITE)
    draw_grid()

    # Display player scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Player 1: {player_scores[0]}  Player 2: {player_scores[1]}", True, BLACK)
    screen.blit(score_text, (10, SCREEN_SIZE - 40))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
