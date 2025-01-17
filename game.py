import pygame

class Game:
  def __init__(self):
    pygame.init() # Initialize pygame
    pygame.display.set_caption("I Can't Stop Spinning")
    
    self.screen = pygame.display.set_mode((640,480)) # Tuple with resolution in px
    self.display = pygame.Surface((320, 240))
    
    self.clock = pygame.time.Clock()  
    self.running = True
    
    self.player = ""
  
  def run(self):
    # Game Loop
    while self.running: 
      self.display.fill((14, 219, 248))
           
      for event in pygame.event.get(): # Get inputs          
        if event.type == pygame.QUIT:
          self.running = False
          
      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()) , (0, 0))
      pygame.display.update()
      self.clock.tick(60) # Force the game to run at 60fps
        
          
    pygame.quit() # Closes pygame
    
Game().run()