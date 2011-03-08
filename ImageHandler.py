#!/usr/bin/python

#Image loader file for Megaman
#Gamedevelopers: Mosterann and Darkdefender

import pygame
import os

class ImageHandler:
    
    #Initialize variables
    path = "images"


    def load_image(name, colorkey=None):
        fullname = os.path.join(path, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
