#!/usr/bin/python

#StartMenu file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

from Menu import Menu
from Button import ButtonList

class StartMenu(Menu):

    menuentries = ["images/start.png",
                   "images/options.png",
                   "images/exit.png"]

    def __init__(self):
        for buttonobj in ButtonList(self.menuentries, 0,100,10,"vert"):
            self.add_button(buttonobj)
