#!/usr/bin/python

#Game engine class file for Megaman
#Gamedevelopers: Mosterann and Darkdefender

import pygame
import os
import platform
from Player import Player
#from ImageHandler import ImageHandler

class GameEngine:

    #Keep gamewindow centered
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    def game_loop(self):

        #Initialize variables
        pygame.init()
        running = True
        screen_height = 500
        screen_width = 500
        background_colour = [0,0,0]
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Megaman")
        screen.fill(background_colour) #Background colour
        player = Player()
        

        #Game functions
        def handle_keyevents():
            y = 1
            #handle keyevents - TODO

        def update():
            x = 1
            #update all - TODO

        def render_all():
            #render all - TODO
            screen.blit(player.get_image(),(player.get_x_pos(),player.get_y_pos()))
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
	
