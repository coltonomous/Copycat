"""
TODO:
    - Add start and loss menus
    - Add sound and maybe zen music.
    - Consider updating graphics.
    - Display round number in corner of screen.
    
"""


import pygame
import Button
import random

# Initializes pygame.
pygame.init()

# Initializes window size.
display = (800, 600)
gameDisplay = pygame.display.set_mode(display)

# Sets window name.
pygame.display.set_caption("Copycat")

# Game clock.
clock = pygame.time.Clock()

# Define game buttons.
greenButton = Button.Button(pygame.Rect(180, 60, 200, 200), "dark_green")
redButton = Button.Button(pygame.Rect(420, 60, 200, 200), "dark_red")
yellowButton = Button.Button(pygame.Rect(180, 300, 200, 200), "dark_yellow")
blueButton = Button.Button(pygame.Rect(420, 300, 200, 200), "dark_blue")

# Defines essential colors in RGB.
colors = {
    "black": (0, 0, 0),
    "green": (0, 255, 0),
    "dark_green": (0, 130, 0),
    "red": (255, 0, 0),
    "dark_red": (130, 0, 0),
    "blue": (0, 0, 255),
    "dark_blue": (0, 0, 130),
    "yellow": (255, 255, 0),
    "dark_yellow": (130, 130, 0),
}

########################################################################################################################
############################################## Game Functions ##########################################################
########################################################################################################################

def rough_render():
    """
    Draws non interactive buttons to the screen for displaying 
    the sequence.
    """
    gameDisplay.fill(colors["black"])    
    pygame.draw.rect(gameDisplay, colors[greenButton.color_string], greenButton.rect)
    pygame.draw.rect(gameDisplay, colors[redButton.color_string], redButton.rect)
    pygame.draw.rect(gameDisplay, colors[yellowButton.color_string], yellowButton.rect)
    pygame.draw.rect(gameDisplay, colors[blueButton.color_string], blueButton.rect)
    
    pygame.display.update()

def hovering_button(mouse, button):
    """ 
    Highlightes button if mouse is hovering over it. 
    """   
    highlighted = "dark_" not in button.color_string

    if button.rect.collidepoint(mouse):
        if not highlighted:
            button.toggle_color()
    elif highlighted:
        button.toggle_color()
    
    pygame.draw.rect(gameDisplay, colors[button.color_string], button.rect)

def clicked_button(mouse, button, step):
    """ 
    Returns True if the correct button was clicked. Returns false is no button is clicked.
    Quits program is wrong button is clicked. 
    """        
    if button.rect.collidepoint(mouse):
        if pygame.mouse.get_pressed()[0]:
            if button == step:
                #play sound
                pygame.time.wait(200)
                return True
            else:
                #play sound
                pygame.time.wait(200)
                pygame.quit()
                quit()
    return False
    
def flash_button(button):
    """ 
    Flashes the passed button.
    """
    rough_render()
    pygame.time.wait(400)

    button.toggle_color()
    rough_render()
    #play sound
    
    pygame.time.wait(400)
    
    button.toggle_color()
    rough_render()
             
def quit_program(event):
    """ 
    Quits program.
    """  
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

########################################################################################################################
############################################## Main Game Loop ##########################################################
########################################################################################################################

def game_loop():
    buttons_list = [greenButton, redButton, yellowButton, blueButton]
    sequence = [greenButton, redButton, yellowButton, blueButton]
    count = -1
        
    while 1:
    
        coordinates = pygame.mouse.get_pos()
    
        # Event handling for quitters.
        for event in pygame.event.get():
            quit_program(event)
        
        # Checks if a new round is beginning and plays sequence.
        if count == -1:
            for button in sequence:
                flash_button(button)
            count += 1
            
        # Draws game to screen.
        else:
            gameDisplay.fill(colors["black"])
            hovering_button(coordinates, greenButton)
            hovering_button(coordinates, redButton)
            hovering_button(coordinates, yellowButton)
            hovering_button(coordinates, blueButton)
        
        # Checks for button clicks.
        green_check = clicked_button(coordinates, greenButton, sequence[count])
        red_check = clicked_button(coordinates, redButton, sequence[count])
        yellow_check = clicked_button(coordinates, yellowButton, sequence[count])
        blue_check = clicked_button(coordinates, blueButton, sequence[count])
            
        # Checks whether correct button in the sequence was clicked.
        if green_check or red_check or yellow_check or blue_check:
            count += 1
            print count
            
        # Checks whether to begin a new round.
        if count == len(sequence):
            # Resets the screen.
            sequence[-1].toggle_color()
            rough_render()
   
            sequence.append(buttons_list[random.randrange(4)])
            count = -1
        
        # Updates the game display at 30 fps.
        pygame.display.update()
        clock.tick(30)


game_loop()
