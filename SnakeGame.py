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

#List used for initializing snake segments
ss_list = []
#Group used for updating snake segments in the game loup
ss_group = pygame.sprite.Group()

####### Initial Conditions ########
size = 20
initial_pos_x = 180
initial_pos_y = window_y - size
initial_direction = 'right'
snakelength = 15
###################################
#Create Snake Segments
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

def show_go_screen():
    print('SHOW GO SCREEN HAS FIRED!')
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameOverFont2 = pygame.font.Font('freesansbold.ttf', 50)
    gameSurf = gameOverFont.render('Game Over', True, WHITE)
    overSurf = gameOverFont2.render('Play Again? (y/n)', True, WHITE)
    #playAgainSurf = gameOverFont.render('Play Again? (y/n)', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    #playAgainRect = playAgainSurf.get_rect()
    gameRect.midtop = (window_x / 2, 10)
    overRect.midtop = (window_x / 2, gameRect.height + 10 + 25)
    #playAgainRect.midtop = (window_x / 2, overRect.height + 10 + 25)
    window.blit(gameSurf, gameRect)
    window.blit(overSurf, overRect)
    #window.blit(playAgainSurf, playAgainRect)
    #drawPressKeyMsg()
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting = False
                    main()
                if event.key == pygame.K_n:
                    waiting = False
                    game_running = False



#snake position
snake_sprite_position = [100, 50]

# food position
food_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
food_spawn = True


def main():
    #start to the game functionality
    count = 1
    #game running
    game_running = True
    while game_running:

        game_over = False
        #HANDLE GAME OVER
        print('*************************************')
        print('WHILE LOOP # ' + str(count))
        count += 1
        for ss in ss_group:
            print('------------------------')
            for other_ss in ss_group:
                print('comparing ' + ss.name + ' to ' + other_ss.name + ', ' + str(ss.rect.x) + ' to ' + str(other_ss.rect.x) + ', and ' + str(ss.rect.y) + ' to ' + str(other_ss.rect.y))
                if(ss.name is not other_ss.name and ss.rect.x == other_ss.rect.x and ss.rect.y == other_ss.rect.y):
                    game_over = True
                    print('******************SS HAVE CRASHED!!!!!')

        if(game_over):
            show_go_screen()

        #good form to put the escape first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                
        #get pressed :)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ss_list[0].direction = 'left'
        if keys[pygame.K_RIGHT]:
            ss_list[0].direction = 'right'
        if keys[pygame.K_UP]:
            ss_list[0].direction = 'up'
        if keys[pygame.K_DOWN]:
            ss_list[0].direction = 'down'

        
        #snake.update()
        for ss in ss_group:
            ss.update()

        window.fill(BLACK)

        ss_group.draw(window)
    

        #SUPER IMPORTANT, FLIP REFRESHES THE SCREEN
        pygame.display.flip()

        #fps
        fps.tick(5)

    #End Game
    pygame.QUIT()

main()