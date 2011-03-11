#!/usr/bin/python

#Game engine class file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame
import os
from Player import Player
from StartMenu import StartMenu
from GameState import GameState

class GameEngine:

    pygame.init()
    running = True
    screen_height = 200
    screen_width = 320
    background_colour = [0,0,0]

    menu = StartMenu()
    game = GameState()
    current_state = menu

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("The chronicles of Mosterann")

    #Keep gamewindow centered
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    def set_state(self,str_state):
        if(str_state == "game"):
            current_state = game
        elif(str_state == "menu"):
            current_state = menu

    def game_loop(self):
        
    #Main gameloop
        while self.running:
            self.handle_keyevents()
            self.update()
            self.render_all()

        #Game functions
    def handle_keyevents(self):
        events = pygame.event.get()
        for e in events:
            self.current_state.handle_keyevents(e)
            if e.type == pygame.QUIT:
                self.running = False
            #handle keyevents - TODO

    def update(self):
        self.current_state.update()
    #update all - TODO

    def render_all(self):
        self.screen.fill(self.background_colour) #Background colour
        self.current_state.render(self.screen)
    #Update the screen
        pygame.display.flip()



    def clean_up(self):
        pygame.quit()

    def start(self):
        self.game_loop()
        self.clean_up()
	
