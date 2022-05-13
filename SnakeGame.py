import pygame
import SnakeSegment as ss
from Snake import Snake
import random 

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
#snake = pygame.sprite.Group()
snake = []
ss_group = pygame.sprite.Group()

#create snake segments!
size = 20
initial_pos_x = 180
initial_pos_y = window_y - size
initial_direction = 'right'
k = 1
while k <= 10:
    name = 'ss' + str(k)
    snake.append(ss.SnakeSegment(name, BLACK, size, window_x, window_y, initial_pos_x, initial_pos_y, initial_direction))
    #increment loop variables
    initial_pos_x -= size
    k += 1

for ss in snake:
    index = snake.index(ss)
    if index == 0:
        ss.segment_behind = snake[index+1]
    elif index == 9:
        ss.segment_in_front = snake[index-1]
    else:
        ss.segment_behind = snake[index+1]
        ss.segment_in_front = snake[index-1]
    ss_group.add(ss)

#clocks are fun
fps = pygame.time.Clock()
'''
def show_game_over_screen():
    window.blit(background, background_rect)
    draw_text(window, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        fps.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
'''
#snake position
snake_sprite_position = [100, 50]

# food position
food_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
food_spawn = True



#start to the game functionality

#game running
game_running = True
while game_running:

    game_over = False
    #HANDLE GAME OVER
    print('*************************************')
    count = 1
    print('WHILE LOOP # ' + str(count))
    for ss in ss_group:
        print('------------------------')
        for other_ss in ss_group:
            print('comparing ' + ss.name + ' to ' + other_ss.name + ', ' + str(ss.rect.x) + ' to ' + str(other_ss.rect.x) + ', and ' + str(ss.rect.y) + ' to ' + str(other_ss.rect.y))
            if(ss.name is not other_ss.name and ss.rect.x is other_ss.rect.x and ss.rect.y is other_ss.rect.y):
                game_over = True
                print('******************SS HAVE CRASHED!!!!!')

    if(game_over):
        game_over = True
    #if game_over:
        #Pop up a screen saying you lose
        #show_game_over_screen()
    #good form to put the escape first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    #get pressed :)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake[0].direction = 'left'
    if keys[pygame.K_RIGHT]:
        snake[0].direction = 'right'
    if keys[pygame.K_UP]:
        snake[0].direction = 'up'
    if keys[pygame.K_DOWN]:
        snake[0].direction = 'down'

    #snake.update()
    for ss in ss_group:
        ss.update()

    window.fill(BLACK)

    ss_group.draw(window)
    

    #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
    pygame.display.flip()

    #fps
    fps.tick(30)

#End Game
pygame.QUIT()
