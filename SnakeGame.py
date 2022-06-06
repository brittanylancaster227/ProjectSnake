import pygame
from pygame.locals import *
import SnakeSegment
import random 

#initializing pygame functions
pygame.init()

#CONSTANTS
BLACK = (0,0,0)
WHITE = (255,255,255)
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

#Create game window
window_x = 720
window_y = 480
window_size = (window_x, window_y)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')
#Initialize clock
clock = pygame.time.Clock()

def main():
    
    #######INITIALIZE GAME ###########
    #Initial conditions
    size = 20
    initial_pos_x = 180
    initial_pos_y = window_y - size
    initial_direction = RIGHT
    snake_length = 10
    ss_list = []
    ss_group = pygame.sprite.Group()
    #Create snake segments
    k = 1
    while k <= snake_length:
        name = 'ss' + str(k)
        ss_list.append(SnakeSegment.SnakeSegment(name, BLACK, size, window_x, window_y, initial_pos_x, initial_pos_y, initial_direction))
        initial_pos_x -= size
        k += 1
    #Link snake segments
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

    game_running = True
    game_over = False
    #######END INITIALIZE GAME#########

    while game_running:
        #Handle game over
        if(game_over):
            print('SHOW GO SCREEN HAS FIRED!')
            #window.fill(BLACK)
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
                    if event.type == pygame.QUIT:
                        waiting = False
                        game_running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_n:
                            waiting = False
                            game_running = False
                        elif event.key == K_y:
                            main()
                            
        
        #DETECT A CRASH
        #print('*************************************')
        #print('WHILE LOOP # ' + str(count))
        for ss in ss_group:
            #print('------------------------')
            for other_ss in ss_group:
                #print('comparing ' + ss.name + ' to ' + other_ss.name + ', ' + str(ss.rect.x) + ' to ' + str(other_ss.rect.x) + ', and ' + str(ss.rect.y) + ' to ' + str(other_ss.rect.y))
                if(ss.name is not other_ss.name and ss.rect.x == other_ss.rect.x and ss.rect.y == other_ss.rect.y):
                    game_over = True
                    print('******************SS HAVE CRASHED!!!!!')
        
        #Create listener for keystrokes
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

        #Draw the snake on the window
        window.fill(BLACK)
        ss_group.draw(window)

        #Update Snake segments
        for ss in ss_group:
            ss.update()

        #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
        pygame.display.flip()
          
        #Advance the clock
        clock.tick(7)
    #end game at end of main method
    pygame.QUIT
    quit()
#Call main method!
main()