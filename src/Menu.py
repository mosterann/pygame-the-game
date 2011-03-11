#!/usr/bin/python

#Menu file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame
from Cursor import Cursor

class Menu:

    button_list = []
    selectedbutton = 0
    cursor = Cursor("images/arrow.png",100,0,100,100)
    introani = True

    def handle_keyevents(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                self.selectedbutton += 1
            elif(event.key == pygame.K_LEFT):
                self.selectedbutton -= 1
            elif(event.key == pygame.K_UP):
                self.selectedbutton -= 1
            elif(event.key == pygame.K_DOWN):
                self.selectedbutton += 1

    def update(self):
        # TODO
        if self.selectedbutton >= len(self.button_list):
            self.selectedbutton = 0
        elif self.selectedbutton < 0:
            self.selectedbutton = len(self.button_list) - 1
        self.cursor.set_x_pos(self.button_list[self.selectedbutton].get_x_pos() - 15)
        self.cursor.set_y_pos(self.button_list[self.selectedbutton].get_y_pos())

    def render(self, screen):
        for button in self.button_list:
            screen.blit(button.get_image(),(button.get_x_pos(),button.get_y_pos()))
        screen.blit(self.cursor.get_image(),(self.cursor.get_x_pos(),self.cursor.get_y_pos()))

    def add_button(self, button_obj):
        self.button_list.append(button_obj)

    def get_button_list(self):
        return self.button_list
