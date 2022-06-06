import pygame

WHITE = (255, 255, 255)
#IMAGE = pygame.image.load('smiley20x20.png').convert_alpha()

class SnakeSegment(pygame.sprite.Sprite):

    def __init__(self, name, color, size, window_x, window_y, initial_x, initial_y, direction):
        
        super().__init__()
        self.name = name
        self.color = color
        self.size = size
        self.image = pygame.image.load('smileyFaceResized.png')
        self.rect = self.image.get_rect()
        #self.image = pygame.Surface([size, size])
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        self.segment_should_move = True
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

    def is_at_right_edge(self):
        if(self.rect.x + self.rect.width >= self.window_x):
            return True
        else:
            return False
    
    def is_at_left_edge(self):
        if(self.rect.x <= 0):
            return True
        else:
            return False
    
    def is_at_top_edge(self):
        if(self.rect.y <= 0):
            return True
        else:
            return False
    
    def is_at_bottom_edge(self):
        if(self.rect.y + self.rect.height >= self.window_y):
            return True
        else:
            return False

    def update(self):
        #USED FOR DEBUGGING POSITIONS
        '''
        leader
        print('------------')
        if(self.segment_in_front is None):
            print('----------------------------------')
            print('I AM THE LEADER!')
        print('I AM AT ' + '(' + str(self.rect.x) + ', ' + str(self.rect.y) + ')')
        print('MY PREVIOUS POSITION WAS ' + '(' + str(self.prev_x) + ', ' + str(self.prev_y) + ')')
        print('I SHOULD MOVE NOW?: ' + self.segment_should_move)
        print()
        '''
        
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

        if self.segment_in_front is None:
            match self.direction:
                case 'right':
                    if(not self.is_at_right_edge()):
                        self.segment_should_move = True
                        self.rect.x += self.size
                    else:
                        self.segment_should_move = False
                case 'left':
                    if(not self.is_at_left_edge()):
                        self.segment_should_move = True
                        self.rect.x -= self.size
                    else:
                        self.segment_should_move = False
                case 'up':
                    if(not self.is_at_top_edge()):
                        self.segment_should_move = True
                        self.rect.y -= self.size
                    else:
                        self.segment_should_move = False
                case 'down':
                    if(not self.is_at_bottom_edge()):
                        self.segment_should_move = True
                        self.rect.y += self.size
                    else:
                        self.segment_should_move = False
        #segments behind
        else:
            #determine if segment in front moved last tick. if it didn't, don't move the segment
            if(self.segment_in_front.segment_should_move):
                self.segment_should_move = True
                self.rect.x = self.segment_in_front.prev_x  
                self.rect.y = self.segment_in_front.prev_y
            else:
                self.segment_should_move = False