#!/usr/bin/python

#Menu file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame
from Cursor import Cursor

class Menu:

    button_list = []
    cursor = Cursor("images/cursor.jpg",100,0,100,100)

    def handle_keyevents(self, event):
        if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            if(event.key == pygame.K_RIGHT):
                self.cursor.set_x_pos(self.cursor.get_x_pos() + 10)
            elif(event.key == pygame.K_LEFT):
                self.cursor.set_x_pos(self.cursor.get_x_pos() - 10)
            elif(event.key == pygame.K_UP):
                self.cursor.set_y_pos(self.cursor.get_y_pos() - 10)
            elif(event.key == pygame.K_DOWN):
                self.cursor.set_y_pos(self.cursor.get_y_pos() + 10)

    def update(self):
        # TODO
        x = 1

    def render(self, screen):
        for button in self.button_list:
            screen.blit(button.get_image(),(button.get_x_pos(),button.get_y_pos()))
        screen.blit(self.cursor.get_image(),(self.cursor.get_x_pos(),self.cursor.get_y_pos()))

    def add_button(self, button_obj):
        self.button_list.append(button_obj)

    def get_button_list(self):
        return self.button_list
