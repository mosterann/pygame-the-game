#!/usr/bin/python

#Button file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

from Menu import Menu
from Button import Button

class StartMenu(Menu):

    def __init__(self):
        game_button = Button("images/Megaman.jpg",100,0,100,100)
        quit_button = Button("images/Megaman.jpg",0,0,100,100)

        self.add_button(game_button)
        self.add_button(quit_button)
    
