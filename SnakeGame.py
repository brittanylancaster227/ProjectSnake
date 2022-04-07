import pygame

#window, must be x and y by pixel
window_x = 720
window_y = 480

#initializing pygame functions
pygame.init()

#show game window
pygame.display.set_caption('Snake Game')
#this required double () not sure why
game_window = pygame.display.set_mode((window_x, window_y))

#fps = pygame.time.Clock()

game_running = True
while game_running:
    #content
    


   

#it puts the snake on the screen
    snake_postition = [100, 50]

#body of the snake (for dynamic ability) making it 4 blocks long to start
    snake_body = [ [100, 50], 
                    [90, 50],       
                    [80, 50], 
                    [70, 50]
                ]      

    #snake_body.insert(0, snake_postition)
    #pygame.display.update()


    for pos in snake_body:
        pygame.draw.rect(game_window, pygame.Rect(
          pos[0], pos[1], 10, 10))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False


#End Game
pygame.QUIT()
