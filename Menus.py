import pygame
import sys
import os
from tkinter import messagebox

from Game import Game

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CE JUMP")

# FONT FILE
font_path = 'Pixeboy-z8XGD.ttf'  # Adjust the font file path as needed
font_2path = 'PressStart2P-vaV7.ttf'
if not os.path.isfile(font_path):
    print("Font file not found:", font_path)
    sys.exit(1)

font = pygame.font.Font(font_path, 32)  # Adjust the font size as needed

# Define colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
COLORS = [RED, BLUE, GREEN, ORANGE, YELLOW]

# Load image frames for background
image_BG = "BG"
frame_files = sorted(os.listdir(image_BG))
background_frames = [
    pygame.transform.scale(pygame.image.load(os.path.join(image_BG, frame)), (WIDTH, HEIGHT)).convert_alpha() for frame
    in frame_files]
background_index = 0
background_frames_count = len(background_frames)
background_frame_rect = background_frames[0].get_rect()

# Initialize mixer for sound
pygame.mixer.init()
pygame.mixer.music.load("power.mp3")  # Load background music
pygame.mixer.music.set_volume(0.5)  # Set volume (0 to 1)
pygame.mixer.music.play(-1)  # Play music on loop (-1 means loop indefinitely)

# Variables to store music status and volume
music_on = True
volume = 0.5


# Function to display text on the screen


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


# Function to start the game
def start_game(background_frames, background_index, current_color):
    running = True
    while running:
        screen.blit(
            background_frames[background_index], background_frame_rect)

        draw_text("CHOOSE", pygame.font.Font(
            font_path, 200), current_color, 300, 100)
        draw_text("PLAYER", pygame.font.Font(
            font_path, 100), current_color, 300, 200)

        # Load the images
        image1 = pygame.image.load('cechar.png')
        image2 = pygame.image.load('ceboy.png')
        image4 = pygame.image.load('cegirl.png')
        image3 = pygame.image.load('ceprof.png')

        # Get the sizes of the images
        width1, height1 = image1.get_size()
        width2, height2 = image2.get_size()
        width3, height3 = image3.get_size()
        width4, height4 = image4.get_size()

        # Draw the rectangles and images
        pygame.draw.rect(screen, BLACK, (150, 300, 100, 100))
        screen.blit(image1, (150 + (100 - width1) //
                    2, 300 + (100 - height1) // 2))

        pygame.draw.rect(screen, BLACK, (350, 300, 100, 100))
        screen.blit(image2, (350 + (100 - width2) //
                    2, 300 + (100 - height2) // 2))

        pygame.draw.rect(screen, BLACK, (350, 500, 100, 100))
        screen.blit(image3, (350 + (100 - width3) //
                    2, 500 + (100 - height3) // 2))

        pygame.draw.rect(screen, BLACK, (150, 500, 100, 100))
        screen.blit(image4, (150 + (100 - width4) //
                    2, 500 + (100 - height4) // 2))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 50 < mouse_pos[0] < 250 and 250 < mouse_pos[1] < 450:
                    print("First rectangle clicked")
                    character = "cechar.png"
                    running = False
                elif 350 < mouse_pos[0] < 550 and 250 < mouse_pos[1] < 450:
                    print("Second rectangle clicked")
                    character = "ceboy.png"
                    running = False
                elif 50 < mouse_pos[0] < 250 and 500 < mouse_pos[1] < 700:
                    print("Third rectangle clicked")
                    character = "cegirl.png"
                    running = False
                elif 350 < mouse_pos[0] < 550 and 500 < mouse_pos[1] < 700:
                    print("Fourth rectangle clicked")
                    character = "ceprof.png"
                    running = False
    # gives the Game() the selected character
    g = Game(character)
    # Starts the game again
    g.gameExit = False
    if not g.gameExit:
        g.__init__(character)
        # take the score and highscore for drawing in game_over
        score, highscore = g.run()
    return score, highscore
# Function to show game over screen


def game_over(background_frames, background_index, current_color, score, highscore):
    running = True
    while running:
        screen.blit(
            background_frames[background_index], background_frame_rect)

        draw_text("GAME", pygame.font.Font(
            font_path, 200), current_color, 300, 100)
        draw_text("OVER", pygame.font.Font(
            font_path, 100), current_color, 300, 200)

        button_x = 200
        start_button_y = 500
        button_width = 200
        button_height = 50
        button_spacing = 100

        # draw the score
        draw_text("Score: " + str(score), pygame.font.Font(font_path, 36),
                  BLACK, 300, 240)
        draw_text("Highscore: " + str(highscore), pygame.font.Font(font_path, 36),
                  BLACK, 300, 265)

        pygame.draw.rect(screen, (0, 0, 0), (button_x,
                         start_button_y, button_width, button_height))
        draw_text("Try Again", pygame.font.Font(font_path, 36),
                  WHITE, 300, start_button_y + button_height // 2)
        pygame.draw.rect(screen, (0, 0, 0), (button_x, start_button_y +
                         button_spacing, button_width, button_height))
        draw_text("Options", pygame.font.Font(font_path, 36), WHITE,
                  300, start_button_y + button_spacing + button_height // 2)
        pygame.draw.rect(screen, (0, 0, 0), (button_x,
                         700, button_width, button_height))
        draw_text("Quit", pygame.font.Font(font_path, 36), WHITE, 300, 725)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 < mouse_pos[0] < 400 and 500 < mouse_pos[1] < 550:
                    print("Start Button Clicked")
                    running = False
                    score, highscore = start_game(background_frames,
                                                  background_index, current_color)
                    game_over(background_frames,
                              background_index, current_color, score, highscore)
                elif 200 < mouse_pos[0] < 400 and 500 < mouse_pos[1] < 650:
                    print("Options Button Clicked")
                    show_options(background_frames,
                                 background_index, current_color)
                elif 200 < mouse_pos[0] < 400 and 700 < mouse_pos[1] < 750:
                    running = False

# Function to show options


def show_options(background_frames, background_index, current_color):
    global music_on, volume
    running = True
    while running:
        screen.blit(background_frames[background_index], background_frame_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 < mouse_pos[0] < 400 and 400 < mouse_pos[1] < 450:
                    music_on = not music_on
                    if music_on:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif 150 < mouse_pos[0] < 200 and 500 < mouse_pos[1] < 550:
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)
                    # Check if volume reaches 10%, turn on music
                    if volume >= 0.1:
                        music_on = True
                elif 400 < mouse_pos[0] < 450 and 500 < mouse_pos[1] < 550:
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume)
                    # Check if volume is 0%, turn off music
                    if volume == 0.0:
                        music_on = False
                elif 200 < mouse_pos[0] < 400 and 600 < mouse_pos[1] < 650:
                    running = False

        # Draw buttons
        pygame.draw.rect(screen, BLACK, (190, 400, 220, 50))
        pygame.draw.rect(screen, BLACK, (150, 500, 50, 50))
        pygame.draw.rect(screen, BLACK, (400, 500, 50, 50))
        pygame.draw.rect(screen, BLACK, (200, 600, 200, 50))
        pygame.draw.rect(screen, WHITE, (210, 505, 180, 35))

        # Draw text on buttons
        draw_text("", pygame.font.Font(font_path, 30), WHITE, 300, 425)
        draw_text("+", pygame.font.Font(font_path, 30), WHITE, 172, 525)
        draw_text("-", pygame.font.Font(font_path, 30), WHITE, 425, 525)
        draw_text("Back", pygame.font.Font(font_path, 30), WHITE, 300, 625)

        # Draw music indicator
        music_status = "ON" if music_on else "OFF"
        draw_text(f"Music Status: {music_status}", pygame.font.Font(
            font_path, 30), GREEN if music_on else RED, 300, 425)

        # Draw volume level
        draw_text("Volume: {}%".format(int(volume * 100)),
                  pygame.font.Font(font_path, 35), BLACK, 300, 525)

        # Draw game title
        draw_text("CE", pygame.font.Font(
            font_path, 200), current_color, 300, 100)
        draw_text("JUMP", pygame.font.Font(
            font_path, 100), current_color, 300, 200)

        pygame.display.flip()

# Function to show how to play


def show_how_to_play(background_frames, background_index, current_color):
    how_to_play_text = [
        "",
        "How to play CE JUMP game:",
        ""
        "1. Use the arrow keys "
        "to move the character.",
        "2. Jump over obstacles "
        "to score points.",
        "3. Avoid falling or colliding "
        "with obstacles.",
        "4. Collect power-ups for "
        "extra points or abilities."
    ]

    # Font for the instructions
    font = pygame.font.Font(font_2path, 9)

    # Back button coordinates and dimensions
    back_button_rect = pygame.Rect(200, 700, 200, 50)

    running = True
    while running:
        screen.blit(background_frames[background_index], background_frame_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        return  # Exit the function instead of setting running to False

        # Calculate starting y-coordinate for the instructions
        total_text_height = len(how_to_play_text) * 25
        start_y = (HEIGHT - total_text_height) // 2

        # Draw box around instructions and fill it with white color
        box_height = 220 + 30  # Add some padding
        pygame.draw.rect(screen, WHITE, (50, start_y - 10, 500, box_height))
        pygame.draw.rect(screen, BLACK, (50, start_y - 10, 500, box_height), 5)

        # Render the instructions onto the screen
        y = start_y
        for line in how_to_play_text:
            draw_text(line, font, BLACK, 300, y)
            y += 40

        # Draw back button
        pygame.draw.rect(screen, BLACK, back_button_rect)
        draw_text("Back", pygame.font.Font(font_path, 36), WHITE, 300, 725)

        # Draw game title
        draw_text("CE", pygame.font.Font(
            font_path, 200), current_color, 300, 100)
        draw_text("JUMP", pygame.font.Font(
            font_path, 100), current_color, 300, 200)

        pygame.display.flip()


# Main Menu Function
def main_menu(background_frames, background_index):
    background_speed = 1  # Adjust speed as needed
    current_color_index = 0
    running = True
    last_color_change = 0  # Track the time of the last color change
    # Interval in milliseconds for color change (1 second)
    color_interval = 100

    # Time variables for background animation
    last_frame_update = pygame.time.get_ticks()
    # Duration for each frame in milliseconds
    frame_duration = 200 // background_speed

    while running:
        current_time = pygame.time.get_ticks()

        # Check if it's time to change the color
        if current_time - last_color_change > color_interval:
            # Change color
            current_color_index = (current_color_index + 1) % len(COLORS)
            last_color_change = current_time

        # Check if it's time to update the background frame
        if current_time - last_frame_update > frame_duration:
            # Update background frame
            background_index = (background_index + 1) % background_frames_count
            last_frame_update = current_time

        screen.blit(background_frames[background_index], background_frame_rect)

        # Draw game title above the start button with dynamic color
        draw_text("CE", pygame.font.Font(font_path, 200),
                  COLORS[current_color_index], 300, 100)
        draw_text("JUMP", pygame.font.Font(font_path, 100),
                  COLORS[current_color_index], 300, 200)
        # Calculate button positions
        button_x = 200
        start_button_y = 500
        button_width = 200
        button_height = 50
        button_spacing = 100

        # Draw buttons in black color
        pygame.draw.rect(screen, (0, 0, 0), (button_x,
                         start_button_y, button_width, button_height))
        draw_text("Start", pygame.font.Font(font_path, 36),
                  WHITE, 300, start_button_y + button_height // 2)
        pygame.draw.rect(screen, (0, 0, 0), (100, start_button_y +
                         button_spacing, button_width, button_height))
        draw_text("Options", pygame.font.Font(font_path, 36), WHITE, 200,
                  start_button_y + button_spacing + button_height // 2)
        pygame.draw.rect(screen, (0, 0, 0), (310, start_button_y +
                         button_spacing, button_width, button_height))
        draw_text("How to Play", pygame.font.Font(font_path, 36), WHITE, 410,
                  start_button_y + button_spacing + button_height // 2)

        # Draw the quit button
        pygame.draw.rect(screen, (0, 0, 0), (200, 700, 200, 50))
        draw_text("Quit", pygame.font.Font(font_path, 36), WHITE, 300, 725)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 < mouse_pos[0] < 400 and 500 < mouse_pos[1] < 550:
                    print("Start Button Clicked")
                    score, highscore = start_game(background_frames, background_index,
                                                  COLORS[current_color_index])
                    game_over(background_frames, background_index,
                              COLORS[current_color_index], score, highscore)
                    break
                elif 100 < mouse_pos[0] < 300 and 500 < mouse_pos[1] < 650:
                    print("Options Button Clicked")
                    show_options(background_frames, background_index,
                                 COLORS[current_color_index])
                elif 310 < mouse_pos[0] < 510 and 500 < mouse_pos[1] < 650:
                    print("How to Play Button Clicked")
                    show_how_to_play(
                        background_frames, background_index, COLORS[current_color_index])
                # Check if the quit button is clicked
                elif 200 < mouse_pos[0] < 400 and 700 < mouse_pos[1] < 750:
                    pygame.quit()
                    sys.exit()

        # Add a small delay to reduce CPU usage
        pygame.time.delay(10)


# Run the main menu
main_menu(background_frames, background_index)
