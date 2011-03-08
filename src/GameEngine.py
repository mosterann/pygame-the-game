#!/usr/bin/python

#Game engine class file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame
import os
from Player import Player
from StartMenu import StartMenu
from GameState import GameState

class GameEngine:

    #Keep gamewindow centered
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    def set_state(self,str_state):
        if(str_state == "game"):
            current_state = game
        elif(str_state == "menu"):
            current_state = menu
            

    def game_loop(self):

        #Initialize variables
        pygame.init()
        running = True
        screen_height = 600
        screen_width = 800
        background_colour = [0,0,0]
        
        menu = StartMenu()
        game = GameState()
        current_state = menu
        
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("The chronicles of Mosterann")
        screen.fill(background_colour) #Background colour        

        #Game functions
        def handle_keyevents():
            for event in pygame.event.get():
                current_state.handle_keyevents(event)
            #handle keyevents - TODO

        def update():
            current_state.update()
            #update all - TODO

        def render_all():
            current_state.render(screen)
            #Update the screen
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
	
