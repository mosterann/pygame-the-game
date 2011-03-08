#!/usr/bin/python

#Menu file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

import pygame

class Menu:

    button_list = []

    #def __init__(self):

    def add_button(self, button_obj):
        self.button_list.append(button_obj)

    def get_button_list(self):
        return self.button_list
    

    
