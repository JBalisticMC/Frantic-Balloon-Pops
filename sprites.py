# Sprites.py
# File for all the sprite classes.
# Jake Malley 2015

# Imports
import pygame
import random
from pygame.locals import *

class Balloon(pygame.sprite.Sprite):
    """
    Class for the Balloon Sprites
    """
    
    def __init__(self, game_object):
        """
        Setup stuff like image and size.
        """
        
        # Call the sprite constructor. 
        pygame.sprite.Sprite.__init__(self)
        
        # Game object, so we can access image filenames etc.
        self.game = game_object
        
        # Load the image file.
        self.image = pygame.image.load(self.game.BALLOON_IMAGE_FILE).convert_alpha()
        # The sprites rect.
        self.rect = self.image.get_rect()
        
        self.width, self.height = self.image.get_size()
        
        
    def set_pos(self):
        """
        Sets the balloons position.
        """
        screen_width, screen_height = self.game.SCREEN_SIZE
        # Set a random x position.
        self.rect.x = random.randint(0, screen_width-self.width)
        # Set a random y position.
        self.rect.y = random.randint(0, screen_height-self.height)
        
class Pin(pygame.sprite.Sprite):
    """
    Class for the Pin Sprite
    """
    
    def __init__(self, game_object):
        """
        Setup stuff like image and size.
        """
        
        # Call the sprite constructor. 
        pygame.sprite.Sprite.__init__(self)
        
        # Game object, so we can access image filenames etc.
        self.game = game_object
        
        # Load the image file.
        self.image = pygame.image.load(self.game.PIN_IMAGE_FILE).convert_alpha()
        # The sprites rect.
        self.rect = self.image.get_rect()
        
        self.width, self.height = self.image.get_size()
        
    def update(self):
        """
        Update the pins position
        """
        
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
        if mouse_x >= 0 and mouse_x <= self.game.SCREEN_SIZE[0]:
            self.rect.x = mouse_x-(self.width/2)
        if mouse_y >= 0 and mouse_y <= self.game.SCREEN_SIZE[1]:
            self.rect.y = mouse_y-(self.height/2)
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)