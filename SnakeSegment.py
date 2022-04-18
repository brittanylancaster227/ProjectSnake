import pygame

WHITE = (255, 255, 255)
#IMAGE = pygame.image.load('smiley20x20.png').convert_alpha()

class SnakeSegment(pygame.sprite.Sprite):

    def __init__(self, color, size, window_x, window_y, initial_x, initial_y, direction):
        
        super().__init__()
        
        self.image = pygame.image.load('smileyFaceResized.png')
        self.rect = self.image.get_rect()
        #self.image = pygame.Surface([size, size])
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        self.window_x = window_x
        self.window_y = window_y
        self.direction = direction
        self.previous_direction = direction
        self.segment_in_front = None
        self.segment_behind = None
        pygame.draw.rect(self.image, color, [0, 0, size, size], 2, 3)
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.prev_x = initial_x
        self.prev_y = initial_y
    """
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels
    
    def moveDown(self, pixels):
        self.rect.y += pixels
    """
    def update(self):
        #leader
        #print('I AM AT ' + '(' + str(self.rect.x) + ', ' + str(self.rect.y) + ')')
        #print('MY PREVIOUS POSITION WAS ' + '(' + str(self.prev_x) + ', ' + str(self.prev_y) + ')')
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        if self.segment_in_front is None:
            match self.direction:
                case 'right':
                    if(self.rect.x + self.rect.width < self.window_x):
                        self.rect.x += 20
                case 'left':
                    if(self.rect.x > 0):
                        self.rect.x -= 20
                case 'up':
                    if(self.rect.y > 0):
                        self.rect.y -= 20
                case 'down':
                    if(self.rect.y + self.rect.height < self.window_y):
                        self.rect.y += 20
        #segments behind
        else:
            self.rect.x = self.segment_in_front.prev_x  
            self.rect.y = self.segment_in_front.prev_y