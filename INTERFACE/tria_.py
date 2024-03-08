import random
import pygame
from pygame.locals import QUIT

pygame.init()

# Library of game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
width = 400
height = 500
character1 = pygame.transform.scale(pygame.image.load('male.png'), (50, 50))  # Corrected line
character2 = pygame.transform.scale(pygame.image.load('female.png'), (50, 50))  # Corrected line
fps = 60
TTfont = pygame.font.Font('freesansbold.ttf', 30)
SCfont = pygame.font.Font('freesansbold.ttf', 15)
score = 0
high_score = 0
game_over = False

# Game variables
player_x = 175
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],
             [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10],
             [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
score_last = 0

# Frame
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('CE JUMP')


# Function to check for collision with blocks
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x, player_y + 60, 40, 5]) and y_change > 0:
            j = True
    return j


clock = pygame.time.Clock()


# Function to update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = 0.45
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


# Function to handle movement of platforms as game progresses
def update_platforms(my_list, change):
    global score
    if player_y < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
            score += 1
    return my_list


# Function to display greeting and flash game title
def display_greeting():
    greeting_text = TTfont.render('Welcome to CE JUMP!', True, black)
    screen.blit(greeting_text, (80, 320))
    pygame.display.flip()
    pygame.time.delay(2000)
    for i in range(5):
        screen.fill(white)
        pygame.display.flip()
        pygame.time.delay(200)
        screen.blit(greeting_text, (80, 200))
        pygame.display.flip()
        pygame.time.delay(200)


# Function to ask user to choose from 2 characters
def choose_character():
    global player
    character_text = SCfont.render('Choose your character:', True, black)
    screen.blit(character_text, (120, 200))
    pygame.display.flip()
    pygame.time.delay(1500)
    character1_text = SCfont.render('Press "1" for Character A', True, black)
    character2_text = SCfont.render('Press "2" for Character B', True, black)
    screen.blit(character1_text, (80, 240))
    screen.blit(character2_text, (80, 260))
    pygame.display.flip()
    chosen = False
    while not chosen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player = character1  # Assign character1 image
                    print("Character A chosen")
                    chosen = True
                elif event.key == pygame.K_2:
                    player = character2  # Assign character2 image
                    print("Character B chosen")
                    chosen = True


# Main game loop
def main_game_loop():
    global player
    global player_x, player_y, game_over, y_change, x_change, jump, score, high_score, platforms, score_last
    running = True
    while running:
        clock.tick(fps)
        screen.fill(white)
        screen.blit(player, (player_x, player_y))
        blocks = []
        score_text = SCfont.render('HIGH SCORE: ' + str(score), True, black)
        screen.blit(score_text, (280, 0))
        high_score_text = SCfont.render('SCORE: ' + str(score), True, black)
        screen.blit(high_score_text, (320, 20))

        for i in range(len(platforms)):
            block = pygame.draw.rect(screen, black, platforms[i], 0)
            blocks.append(block)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    screen.blit(score_text, (100, 0))
                    score = 0
                    player_x = 170
                    player_y = 400
                    background = white
                    score_last = 0
                    platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],
                                 [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10],
                                 [175, 40, 70, 10]]
                if event.key == pygame.K_a:
                    x_change = -player_speed
                if event.key == pygame.K_d:
                    x_change = player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        jump = check_collisions(blocks, jump)
        player_x += x_change

        if player_y < 440:
            player_y = update_player(player_y)
        else:
            game_over = True
            y_change = 0
            x_change = 0

        platforms = update_platforms(platforms, y_change)

        if player_x < -20:
            player_x = -20
        elif player_x > 330:
            player_x = 330

        # Update player image based on direction
        if x_change > 0:
            player = pygame.transform.scale(character1, (50, 50))
        elif x_change < 0:
            player = pygame.transform.flip(pygame.transform.scale(character2, (50, 50)), 1, 0)

        if score > high_score:
            high_score = score

        if score - score_last > 15:
            score_last = score
            background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

        pygame.display.flip()

    pygame.quit()

# Main function
def main():
    global player
    display_greeting()
    player = character1  # Set default character image
    choose_character()
    main_game_loop()


if __name__ == "__main__":
    main()
