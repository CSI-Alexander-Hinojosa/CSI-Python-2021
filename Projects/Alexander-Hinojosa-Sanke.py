from email import message
from tkinter import Y
import pygame        
pygame.init()
import time
import random

# create the screen
# Display
# pygame.init() = inicia todo los terminales de pygame. 
# pygame.quit() = cierra el programa. 

violet= (237, 28, 234) # Score
green= (101, 250, 95) # Fruit
blue= (15, 113, 214) # Snake
orange= (214, 120, 15) # Game over
black= (0,0,0) 
# yellow= (166, 250, 17) # Background 

dis_widht=500
dis_height=400

dis=pygame.display.set_mode((dis_widht,dis_height))

pygame.display.set_caption("Welcome to Snake Game, by 8bit")
game_over=False


clock= pygame.time.Clock()
snake_speed = 15 

snake_block=10
font_style= pygame.font.SysFont(None, 25)
score_font= pygame.font.SysFont(None, 25)

def My_Score(score):
    value = score_font.render("Your score is:"+ str(score), True, violet)
    dis.blit(value, [0, 0])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_widht/4, dis_height/3])

def game_loop():
    game_over = False
    game_close = False

    x1= dis_widht/2
    y1= dis_height/2

    x1_change= 0
    y1_change= 0

    snake_List= []
    length_of_snake= 1

    foodx= round(random.randrange(0, dis_widht-snake_block)/ 10)*10
    foody= round(random.randrange(0, dis_height-snake_block)/ 10)*10

    while not game_over:
        while game_close ==True:
            dis.fill(black)
            message("F, press Q-Quit or P-Play again", orange)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_widht or x1 < 0 or y1 >= dis_height or y1 <0:    
            game_close = True
 
    #  error in gameover true

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

    # Al realizar movimiento vertical, negativo (-) es hacia arriba, mientras que positivo (+) es hacia abajo.

        pygame.draw.rect(dis, green,[foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(dis, blue,[x1, y1 , snake_block, snake_block])
        snake_head= []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close == True

        my_snake(snake_block, snake_List)
        My_Score(length_of_snake - 1)

        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx= round(random.randrange(0, dis_widht-snake_block)/ 10)*10
            foody= round(random.randrange(0, dis_height-snake_block)/ 10)*10
            length_of_snake += 1

        clock.tick(snake_speed) 
    # time.sleep(5)

    pygame.quit()
    quit()

game_loop()
