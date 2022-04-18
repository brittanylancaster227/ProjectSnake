import pygame
from Snake import Snake
import SnakeSegment as ss

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

#create snake segments!
size = 20
initial_height = window_y - size
ss1 = ss.SnakeSegment(BLACK, size, window_x, window_y, 180, initial_height, 'right')
ss2 = ss.SnakeSegment(BLACK, size, window_x, window_y, 160, initial_height, 'right')
ss3 = ss.SnakeSegment(BLACK, size, window_x, window_y, 140, initial_height, 'right')
ss4 = ss.SnakeSegment(BLACK, size, window_x, window_y, 120, initial_height, 'right')
ss5 = ss.SnakeSegment(BLACK, size, window_x, window_y, 100, initial_height, 'right')
ss6 = ss.SnakeSegment(BLACK, size, window_x, window_y, 80, initial_height, 'right')
ss7 = ss.SnakeSegment(BLACK, size, window_x, window_y, 60, initial_height, 'right')
ss8 = ss.SnakeSegment(BLACK, size, window_x, window_y, 40, initial_height, 'right')
ss9 = ss.SnakeSegment(BLACK, size, window_x, window_y, 20, initial_height, 'right')
ss10 = ss.SnakeSegment(BLACK, size, window_x, window_y, 0, initial_height, 'right')

#link the snake segments to one another
ss1.segment_behind = ss2
ss2.segment_in_front = ss1
ss2.segment_behind = ss3
ss3.segment_in_front = ss2
ss3.segment_behind = ss4
ss4.segment_in_front = ss3
ss4.segment_behind = ss5
ss5.segment_in_front = ss4
ss5.segment_behind = ss6
ss6.segment_in_front = ss5
ss6.segment_behind = ss7
ss7.segment_in_front = ss6
ss7.segment_behind = ss8
ss8.segment_in_front = ss7
ss8.segment_behind = ss9
ss9.segment_in_front = ss8
ss5.segment_behind = ss10
ss10.segment_in_front = ss9

#add all to the list for updating
all_sprites_list.add(ss1)
all_sprites_list.add(ss2)
all_sprites_list.add(ss3)
all_sprites_list.add(ss4)
all_sprites_list.add(ss5)
all_sprites_list.add(ss6)
all_sprites_list.add(ss7)
all_sprites_list.add(ss8)
all_sprites_list.add(ss9)
all_sprites_list.add(ss10)

#clocks are fun
fps = pygame.time.Clock()

#start to the game functionality
game_running = True
while game_running:
    #good form to put the escape first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    #get pressed :)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ss1.direction = 'left'
    if keys[pygame.K_RIGHT]:
        ss1.direction = 'right'
    if keys[pygame.K_UP]:
        ss1.direction = 'up'
    if keys[pygame.K_DOWN]:
        ss1.direction = 'down'

    all_sprites_list.update()

    window.fill(BLACK)

    all_sprites_list.draw(window)
    

    #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
    pygame.display.flip()

    #fps
    fps.tick(6)

#End Game
pygame.QUIT()
