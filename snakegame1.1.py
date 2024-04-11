import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)  # Orange
SNAKE_SIZE = 40
FOOD_SIZE = 40
SNAKE_SPEED = 10
FRAME_RATE = 10  # Adjust frame rate for game speed

# Set up the font for score display
pygame.font.init()  # Initialize font module
font = pygame.font.SysFont('Arial', 25)

# Function to show the score on the screen
def show_score(score, color, font, x, y):
    score_surface = font.render('Score : ' + str(score), True, color)
    screen.blit(score_surface, (x, y))
def game_over(score):
    screen.fill(BACKGROUND_COLOR)
    # The rest of the game_over function as provided...

# Function to show the game over screen
def game_over():
    screen.fill(BACKGROUND_COLOR)  # Clear the screen with the background color

    # Game Over text
    game_over_font = pygame.font.SysFont('Arial', 50)
    game_over_surface = game_over_font.render('YOU LOSE!!!', True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)

    # Your Score is text (shows below "YOU LOSE!!!")
    score_font = pygame.font.SysFont('Arial', 35)
    score_surface = score_font.render('Your Score is : ' + str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect.midtop = (SCREEN_WIDTH / 2, game_over_rect.bottom + 20)  # Position below the "YOU LOSE!!!" message
    screen.blit(score_surface, score_rect)

    pygame.display.flip()  # Update the display to show the game over message
    time.sleep(2)  # Display the message for 5 seconds before the game restarts

    # Wait for the player to press 'R' to restart or 'Q' to quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Pressing 'R' restarts the game
                    return True  # Signal that the game should restart
                if event.key == pygame.K_q:  # Pressing 'Q' quits the game
                    return False  # Signal that the game should not restart and quit


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sat Snake')

# Load the Bitcoin logo image
bitcoin_logo = pygame.image.load('/Users/anthonyost6/Desktop/Bitcoin logo.jpeg')
bitcoin_logo = pygame.transform.scale(bitcoin_logo, (FOOD_SIZE, FOOD_SIZE))

# Function to get a random new position for food
def get_random_food_pos():
    return [random.randrange(1, (SCREEN_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (SCREEN_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]

# Function to check for collision with food
def collision_with_food(snake_head, food):
    return snake_head[0] == food[0] and snake_head[1] == food[1]


# Main game function
def main():
    # Game variables
    snake_pos = [[100, 50], [80, 50], [60, 50]]  # Initial snake position
    snake_skin = bitcoin_logo
    food_pos = get_random_food_pos()  # Initial food position
    food = bitcoin_logo
    score = 0
    direction = 'RIGHT'
    change_to = direction
    running = True

    # Game loop
    clock = pygame.time.Clock()
    while running:
        # Event handling for a range of different input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Validate direction changes to prevent the snake from going back on itself
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        elif change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_pos[0][1] -= SNAKE_SPEED
        elif direction == 'DOWN':
            snake_pos[0][1] += SNAKE_SPEED
        elif direction == 'LEFT':
            snake_pos[0][0] -= SNAKE_SPEED
        elif direction == 'RIGHT':
            snake_pos[0][0] += SNAKE_SPEED

         # Snake body growing mechanism
            snake_head = snake_pos[0]
        if collision_with_food(snake_head, food_pos):
    score += 1
    food_pos = get_random_food_pos()
    
    # Get the last segment of the snake
    last_segment = snake_pos[-1]
    # Get the second to last segment to determine the growth direction
    if len(snake_pos) > 1:
        second_to_last_segment = snake_pos[-2]
    else:
        # If the snake only has one segment, use the current direction to determine growth
        second_to_last_segment = None

    if second_to_last_segment:
        # Calculate the new segment's position based on the relative positions of the last two segments
        new_segment_x = last_segment[0] + (last_segment[0] - second_to_last_segment[0])
        new_segment_y = last_segment[1] + (last_segment[1] - second_to_last_segment[1])
        new_segment = [new_segment_x, new_segment_y]
    else:
        # If the snake has only one segment, calculate the new segment position directly based on the direction
        if direction == 'UP':
            new_segment = [last_segment[0], last_segment[1] + SNAKE_SIZE]
        elif direction == 'DOWN':
            new_segment = [last_segment[0], last_segment[1] - SNAKE_SIZE]
        elif direction == 'LEFT':
            new_segment = [last_segment[0] + SNAKE_SIZE, last_segment[1]]
        elif direction == 'RIGHT':
            new_segment = [last_segment[0] - SNAKE_SIZE, last_segment[1]]

    # Add the new segment to the snake
    snake_pos.append(new_segment)

	
        # Game Over conditions   if snake_head[0] >= SCREEN_WIDTH or snake_head[0] < 0 or snake_head[1] >= SCREEN_HEIGHT or snake_head[1] < 0 or snake_head in snake_pos[1:]:            
        if game_over() == False:
             return  # Exit the game
        else:
                main()  # Restart the game

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Draw the snake
        for pos in snake_pos:
         screen.blit(snake_skin, pos)


        # Draw the food
        screen.blit(food, food_pos)

        # Show the score
        show_score(score, (255, 255, 255), font, 10, 10)

        # Update the display and the clock
        pygame.display.flip()
        clock.tick(FRAME_RATE)

# Start the game
if __name__ == '__main__':
    main()

# Clean up Pygame and close the window
pygame.quit()
sys.exit()
