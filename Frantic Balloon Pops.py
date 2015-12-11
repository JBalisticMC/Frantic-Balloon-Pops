# Balloon Pop Game
# Jake Malley and JBalisticMC (Jake Malley mostly)

# Imports
import pygame, sys, time
from pygame.locals import *
import sprites
                                
class GamePlay:
    """
    This is a class for the main game loop, rather than having the
    whole game in the global scope, I have put it in a class, this
    is not required but I prefer to do it this way.
    """
    
    # Constants used in the game.
    red = (255,0,0)
    black = (0,0,0)
    
    display_width = 700
    display_height = 400

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    
    BACKGROUND_IMAGE_FILE = "images/background.jpg"
    BALLOON_IMAGE_FILE = "images/balloon.png"
    PIN_IMAGE_FILE = "images/pin.png"
    FPS = 100
    icon = pygame.image.load('Untitled-icon.png')
    pygame.display.set_icon(icon)
                        

    def __init__(self, width, height):
        """
        This is the constructor, this method gets called
        when a new object is created from this class. (when we
        run the program the code here will run).
        """

        self.score = 0
        
        # Init pygame.
        pygame.init()
        
        # Setup screen size constants based on the parameters.
        self.SCREEN_SIZE = width, height
        
        # Create the screen.
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        # Add a title.
        pygame.display.set_caption("Frantic Balloon Pops 2.0 (Alpha)")
        pygame.mouse.set_visible(False)
        
        # We will use a sprite group to keep track of all the balloons.
        self.balloon_list = pygame.sprite.Group()
        
        # Create a clock.
        self.clock = pygame.time.Clock()
        
        # Add a background image to the screen.
        self.background = pygame.image.load(self.BACKGROUND_IMAGE_FILE)
		
        
        # Set the score to zero.
        self.score = 0
        
        # Create Pin Sprite
        self.pin = sprites.Pin(self)

        print("Loading...")
        
        # Create some balloons.
        self.create_balloons(1)

        
        print("Your Score Is", self.score)

    def score(score):
        text = smallfont.render("Your Score Is", self.score)
        gameDisplay.blit(text, [0,0])

    
    def main_loop(self):
        """
        Main Game Loop.
        """
        
        while True:
            
            # Handle Events with the handle events method below.
            self.handle_events()
            self.screen.blit(self.background, (0,0))
            
            self.balloon_list.update()
            self.pin.update()
            self.balloon_list.draw(self.screen)
            self.pin.draw(self.screen)
            
            # Check for collisions
            self.check_for_collisions()
            
            # Tick the clock.
            self.clock.tick(self.FPS)
            # Update display
            pygame.display.update()
            
            
    def handle_events(self):
        """Handle game events."""
        
        for event in pygame.event.get():
            
            # If the user has quit.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    def create_balloons(self, number_to_create):
        """
        Creates a number of balloons equal to number_to_create.
        (And sets their position randomly).
        """
        
        for i in range(0, number_to_create):
            # Create balloon object.
            balloon = sprites.Balloon(self)
            # Set the position randomly.
            balloon.set_pos()
            # Add this balloon to the list before creating a new one.
            self.balloon_list.add(balloon)
        
    def check_for_collisions(self):
        """
        Check for object collisions.
        """
        collisions = pygame.sprite.spritecollide(self.pin, self.balloon_list, False) # The true at the end means remove the sprite when it collides.
        for balloon in collisions:
            self.score = self.score + 1
            self.balloon_list.remove(balloon)
            print("Your Score Is", self.score)
            
        time.sleep(0.00000000000000000000000005)
        self.create_balloons(1)

if __name__ == "__main__":
    # Create game object.
    game = GamePlay(700,400)
    # Run the loop.
    game.main_loop()
