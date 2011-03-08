#!/usr/bin/python

#Game engine class file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame
import os
import platform
from Player import Player
from StartMenu import StartMenu
#from ImageHandler import ImageHandler

class GameEngine:

    #Keep gamewindow centered
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    def game_loop(self):

        #Initialize variables
        pygame.init()
        running = True
        screen_height = 600
        screen_width = 800
        background_colour = [0,0,0]
        
        menu = StartMenu()
        
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("The chronicles of Mosterann")
        screen.fill(background_colour) #Background colour
        player = Player()
        

        #Game functions
        def handle_keyevents():
            y = 1
            #handle keyevents - TODO

        def update():
            x = 1
            #update all - TODO

        def render_menu():
            render_list = menu.get_button_list()
            for button in render_list:
                screen.blit(button.get_image(),(button.get_x_pos(),button.get_y_pos()))

        def render_all():
            #render all - TODO
            render_menu()
            #screen.blit(player.get_image(),(player.get_x_pos(),player.get_y_pos()))
            pygame.display.flip()

        
            


        #Main gameloop    
        while running:
            handle_keyevents()
            update()
            render_all()

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False



    #Clean up
    def clean_up(self):
        pygame.quit()

    def start(self):
        self.game_loop()
        self.clean_up()
	
