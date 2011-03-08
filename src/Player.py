#!/usr/bin/python

#Player file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

#from ImageHandler import ImageHandler

import pygame

class Player:

    #Initialize variables
    movement_speed = 5
    x_pos = 0
    y_pos = 0
    width = 0
    height = 0
    hp = 10
    image_name = "images/megaman.jpg"
    image_surf = pygame.image.load(image_name)
    image_rect = 0

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_hp(self):
        return self.hp

    def get_image(self):
        return self.image_surf

    def get_image_rect(self):
        return self.image_rect

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos

    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_image(self, new_image):
        self.image_surf = new_image

    def set_image_rect(self, new_image_rect):
        self.image_rect = new_image_rect

