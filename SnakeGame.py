import pygame
from pygame.locals import *
import SnakeSegment as ss
import random 

#initializing pygame functions
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

#window, must be x and y by pixel
window_x = 720
window_y = 480
window_size = (window_x, window_y)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')

#List used for initializing snake segments
ss_list = []
#Group used for updating snake segments in the game loup
ss_group = pygame.sprite.Group()
    
####### Initial Conditions ########
size = 20
initial_pos_x = 180
initial_pos_y = window_y - size
initial_direction = 'right'
snakelength = 5
number_of_fruits = 5
initial_direction = RIGHT
snakelength = 15
###################################
#Create Snake Segments

def init_snake():
    k = 1
    while k <= snakelength:
        name = 'ss' + str(k)
        ss_list.append(ss.SnakeSegment(name, BLACK, size, window_x, window_y, initial_pos_x, initial_pos_y, initial_direction))
        #increment loop variables
        initial_pos_x -= size
        k += 1

    for snakeSegment in ss_list:
        index = ss_list.index(snakeSegment)
        if index == 0:
            snakeSegment.segment_behind = ss_list[index+1]
        elif index == len(ss_list)-1:
            snakeSegment.segment_in_front = ss_list[index-1]
        else:
            snakeSegment.segment_behind = ss_list[index+1]
            snakeSegment.segment_in_front = ss_list[index-1]
        ss_group.add(snakeSegment)

    snake_sprite_position = [100, 50]

k = 1
while k <= snakelength:
    name = 'ss' + str(k)
    ss_list.append(ss.SnakeSegment(name, BLACK, size, window_x, window_y, initial_pos_x, initial_pos_y, initial_direction))
    #increment loop variables
    initial_pos_x -= size
    k += 1

#Link Snake Segments
for ss in ss_list:
    index = ss_list.index(ss)
    if index == 0:
        ss.segment_behind = ss_list[index+1]
    elif index == len(ss_list)-1:
        ss.segment_in_front = ss_list[index-1]
    else:
        ss.segment_behind = ss_list[index+1]
        ss.segment_in_front = ss_list[index-1]
    ss_group.add(ss)

#clocks are fun
fps = pygame.time.Clock()

#snake position
snake_sprite_position = [100, 50]

def main():
    #start to the game functionality
    count = 1
    #game running



    game_running = True
    while game_running:
        init_snake()
        game_over = False
        #HANDLE GAME OVER
        #print('*************************************')
        #print('WHILE LOOP # ' + str(count))
        count += 1
        for ss in ss_group:
            #print('------------------------')
            for other_ss in ss_group:
                #print('comparing ' + ss.name + ' to ' + other_ss.name + ', ' + str(ss.rect.x) + ' to ' + str(other_ss.rect.x) + ', and ' + str(ss.rect.y) + ' to ' + str(other_ss.rect.y))
                if(ss.name is not other_ss.name and ss.rect.x == other_ss.rect.x and ss.rect.y == other_ss.rect.y):
                    game_over = True
                    print('******************SS HAVE CRASHED!!!!!')

        if(game_over):
            print('SHOW GO SCREEN HAS FIRED!')
            gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
            playAgainFont = pygame.font.Font('freesansbold.ttf', 50)
            gameOverSurf = gameOverFont.render('Game Over', True, WHITE)
            playAgainSurf = playAgainFont.render('Play Again? (y/n)', True, WHITE)
            gameOverRect = gameOverSurf.get_rect()
            playAgainRect = playAgainSurf.get_rect()
            gameOverRect.midtop = (window_x / 2, 10)
            playAgainRect.midtop = (window_x / 2, gameOverRect.height + 10 + 25)
            window.blit(gameOverSurf, gameOverRect)
            window.blit(playAgainSurf, playAgainRect)
            pygame.display.update()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        waiting = False
                        game_running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_n:
                            print('N WAS PUSHED')
                            game_running = False
                            waiting = False
                        elif event.key == K_y:
                            print('Y WAS PUSHED')
                            waiting = False
                            game_over = False
                            main()
            

        #handling any sort of escapes:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if(ss_list[0].direction is not RIGHT):
                        ss_list[0].direction = LEFT
                elif event.key == K_RIGHT:
                    if(ss_list[0].direction is not LEFT):
                        ss_list[0].direction = RIGHT
                elif event.key == K_UP:
                    if(ss_list[0].direction is not DOWN):
                        ss_list[0].direction = UP
                elif event.key == K_DOWN:
                    if(ss_list[0].direction is not UP):
                        ss_list[0].direction = DOWN
        
        #snake.update()
        for ss in ss_group:
            ss.update()

        window.fill(BLACK)

        ss_group.draw(window)
    

        #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
        pygame.display.flip()

        #fps
        fps.tick(5)
    pygame.QUIT()

main()
pygame.QUIT()
quit()