import pygame
from Snake import Snake

#initializing pygame functions
pygame.init()
#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#window, must be x and y by pixel
window_x = 720
window_y = 480
window_size = (window_x, window_y)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')

#good to use a group of sprites for flexibility to add more later
all_sprites_list = pygame.sprite.Group()

#create an instance of our snake class and specify its location
snake_sprite = Snake(GREEN, 100,10)
snake_sprite.rect.x = 200
snake_sprite.rect.y = 300
#add instance of snake to our sprite list
all_sprites_list.add(snake_sprite)
#clocks are fun
fps = pygame.time.Clock()

game_running = True
while game_running:
    #good form to put the escape first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    #get pressed :)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_sprite.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        snake_sprite.moveRight(5)
    if keys[pygame.K_UP]:
        snake_sprite.moveUp(5)
    if keys[pygame.K_DOWN]:
        snake_sprite.moveDown(5)

    all_sprites_list.update()

    window.fill(BLACK)

    all_sprites_list.draw(window)

    #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
    pygame.display.flip()

    #fps
    fps.tick(60)

#End Game
pygame.QUIT()
