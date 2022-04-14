import pygame

WHITE = (255, 255, 255)

class Snake(pygame.sprite.Sprite):

    def __init__(self, color, width, height, window_x, window_y, direction):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.window_x = window_x
        self.window_y = window_y
        self.direction = direction
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels
    
    def moveDown(self, pixels):
        self.rect.y += pixels

    def update(self):
        match self.direction:
            case 'right':
                if(self.rect.x + self.rect.width < self.window_x):
                    self.rect.x += 5
            case 'left':
                if(self.rect.x > 0):
                    self.rect.x -= 5
            case 'up':
                if(self.rect.y > 0):
                    self.rect.y -= 5
            case 'down':
                if(self.rect.y + self.rect.height < self.window_y):
                    self.rect.y += 5