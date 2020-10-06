"""
Nokia Snake Game Made by Aledelmon
01/08/2020
"""
import pygame
import random
import time



# initializing pygame
pygame.init()

# Colors
white = (255, 255, 255) # rgb format
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
programIcon = pygame.image.load('índice.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Aledelmon")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

#Main Menu
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameWindow.fill(white)
        text_screen("Snake", green, 400, 250)
        text_screen("Pulsa Enter para comenzar", black, 200, 300)         
        pygame.display.update()
        clock.tick(15)
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(60, screen_height -20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 30  # fps = frames per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Perdiste, presiona Enter para continuar", red, 100, 250)
            text_screen("Tu puntuación: " + str(score), red, 300, 300)

            

            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()



        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                
                if event.type == pygame.KEYDOWN:
                        
                        if (snake_x - food_x)>30:
                            velocity_x = - init_velocity
                            velocity_y = 0
                            time.sleep(0.001)
                            
                            
                        elif(snake_x - food_x)<0:
                            velocity_x = init_velocity
                            velocity_y = 0
                            time.sleep(0.001)
                           

                            
                        if(snake_y - food_y)>30:
                            velocity_y = - init_velocity
                            velocity_x = 0
                            time.sleep(0.001)
                           
                            
                        elif (snake_y - food_y)<0:
                            velocity_y = init_velocity
                            velocity_x = 0
                            time.sleep(0.001)
                            






            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<30 and abs(snake_y - food_y)<30:
                score +=1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length +=5
                
            gameWindow.fill(white)
            text_screen("Score: " + str(score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (0,40), (900,40),5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
game_intro()
gameloop()

