#!/usr/bin/python

#GameState file for The chronicles of Mosterann
#Gamedevelopers: Mosterann and Darkdefender

class GameState:

    running = False


    def handle_keyevents(self, event):
        # TODO
        y = 1

    def update(self):
        # TODO
        x = 1
        
    def render(self, screen):
        #Update background
        for obj in self.background_list:
            screen.blit(obj.get_image(),(obj.get_x_pos(),obj.get_y_pos()))
        #Update NPCs
        for obj in self.npc_list:
            screen.blit(obj.get_image(),(obj.get_x_pos(),obj.get_y_pos()))
        #Update Player
        for obj in self.player_list:
            screen.blit(obj.get_image(),(obj.get_x_pos(),obj.get_y_pos()))
