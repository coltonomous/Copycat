import pygame
import random

pygame.init()

xDisplay = 800
yDisplay = 600
gameDisplay = pygame.display.set_mode((xDisplay, yDisplay))

pygame.display.set_caption("Copycat")

clock = pygame.time.Clock()

greenRect = pygame.Rect(180, 60, 200, 200)
redRect = pygame.Rect(420, 60, 200, 200)
yellowRect = pygame.Rect(180, 300, 200, 200)
blueRect = pygame.Rect(420, 300, 200, 200)

colors = {
    "black": (0, 0, 0),
    "green": (0, 255, 0),
    "darkGreen": (0, 150, 0),
    "red": (255, 0, 0),
    "darkRed": (150, 0, 0),
    "blue": (0, 0, 255),
    "darkBlue": (0, 0, 150),
    "yellow": (255, 255, 0),
    "darkYellow": (150, 150, 0)
}


########################################################################################################################
############################################## Game Functions ##########################################################
########################################################################################################################

def render_game(check, color):
    color_to_rect = {
        "green": greenRect,
        "red": redRect,
        "yellow": yellowRect,
        "blue": blueRect
    }

    if check:
        coordinates = pygame.mouse.get_pos()
    else:
        coordinates = color_to_rect[color].center

    gameDisplay.fill(colors["black"])
    button(coordinates, greenRect, "green", "darkGreen")
    button(coordinates, redRect, "red", "darkRed")
    button(coordinates, yellowRect, "yellow", "darkYellow")
    button(coordinates, blueRect, "blue", "darkBlue")


def button(mouse, rect, active, inactive):
    if rect.collidepoint(mouse):
        pygame.draw.rect(gameDisplay, colors[active], rect)
    else:
        pygame.draw.rect(gameDisplay, colors[inactive], rect)

def quit_program(event):
    if event.type == pygame.event.QUIT:
        pygame.quit()
        quit()

########################################################################################################################
############################################## Main Game Loop ##########################################################
########################################################################################################################

def game_loop():
    color_queue = []
    max_index = 1

    while 1:

        playing = True
        counter = 0

        for event in pygame.event.get():
            quit_program(event)

        render_game(playing, 0)

        #if max_index >= len(color_queue):
            #playing = False
            #color_queue = generate_color_pattern(color_queue)
            #play_color_pattern(color_queue)

        #max_index += 1

        # Updates the game display at 30 fps.
        pygame.display.update()
        clock.tick(30)


game_loop()
