#!/usr/bin/python

#Menu file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame

class Menu:

    button_list = []

    def handle_keyevents(self, event):
        if(event.type == pygame.KEYDOWN):
            print("Hasse")
            if(event.key == pygame.K_RIGHT):
                button_list[0].set_x_pos(500)

    def update(self):
        # TODO
        x = 1
        
    def render(self, screen):
        for button in self.button_list:
            screen.blit(button.get_image(),(button.get_x_pos(),button.get_y_pos()))

    def add_button(self, button_obj):
        self.button_list.append(button_obj)

    def get_button_list(self):
        return self.button_list
    

    
