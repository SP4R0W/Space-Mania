import pygame
import time
import random

pygame.init()

display_width = 640
display_height = 480

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Space Mania")
icon = pygame.image.load("Assets/Images/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#=====================================================
#Images and Variables
#=====================================================
image_width = 130
image_height = 97

player_width = 95
player_height = 100

player_speed = 5

enemy_width = 95
enemy_height = 100

framerate = 60

score = 0

player = pygame.image.load('Assets/Images/player.png')
enemy = pygame.image.load('Assets/Images/enemy.png')

desert = pygame.image.load('Assets/Images/desert.png')
forest = pygame.image.load('Assets/Images/forest.png')
arctic = pygame.image.load('Assets/Images/arctic.png')

desert_level = pygame.image.load('Assets/Images/desertLevel.png')
forest_level = pygame.image.load('Assets/Images/forestLevel.png')
arctic_level = pygame.image.load('Assets/Images/arcticLevel.png')
background = pygame.image.load('Assets/Images/background.png')

close = pygame.image.load('Assets/Images/close.png')

#=====================================================
#COLORS
#=====================================================
white = (255,255,255)
black = (0,0,0)
transparent = (0,0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
gray = (128,128,128)

#=====================================================
#STATES
#=====================================================
menu_loop = False
level_choose_loop = False
game_loop = False
game_win_loop = False
game_lose_loop = False

#=====================================================
#Functions
#=====================================================
class Levels:
    def level_one():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(desert_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(1,"desert",1,10)

    def level_two():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(forest_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(2,"forest",2,15)

    def level_three():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(arctic_level,(0,0))
        pygame.display.update()
        game_functions.game_loop(2,"arctic",3,20)

    def level_four():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(forest_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(3,"forest",4,25)

    def level_five():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(arctic_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(3,"arctic",5,30)

    def level_six():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(desert_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(4,"desert",6,40)

    def level_seven():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(forest_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(4,"forest",7,45)

    def level_eight():
        # Clear the screen
        game_display.fill(white)

        # Draw the background
        game_display.blit(desert_level,(0,0))
        pygame.display.update()

        # Start the game
        game_functions.game_loop(5,"desert",8,50)

    def level_infinite():
        # Clear the screen
        game_display.fill(white)

        # Pick a random level
        level = random.randrange(0,3)

        if (level <= 1):
            random_level = desert_level
        elif ((level >= 1) and (level <= 2)):
            random_level = forest_level
        elif ((level >= 2) and (level <= 3)):
            random_level = arctic_level

        # Draw the correct background
        game_display.blit(random_level,(0,0))

        pygame.display.update()

        # Start the level
        if random_level == desert_level:
            game_functions.game_loop(1,"desert",9,0)
        elif random_level == forest_level:
            game_functions.game_loop(1,"forest",9,0)
        elif random_level == arctic_level:
            game_functions.game_loop(1,"arctic",9,0)

class game_functions:

    def wait(time: int):
        waiting = 0
        while waiting <= time:
            waiting += 1

    def game_quit():
        pygame.quit()
        quit()

    def game_lose(difficulty,level,theme,finish_arg):
        game_lose_loop = True

        # Clear the screen
        game_display.fill(white)
        game_display.blit(background,(0,0))

        pygame.mixer.music.stop()

        while game_lose_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            GUI.message("YOU LOST!",120,165,75)
            pygame.display.update()

            time.sleep(2.5)

            game_lose_loop = False
            game_display.fill(white)
            game_functions.game_loop(difficulty,theme,level,finish_arg)

    def game_win():
        game_win_loop = True

        # Clear the screen
        game_display.fill(white)
        game_display.blit(background,(0,0))

        pygame.mixer.music.stop()
        winSound = pygame.mixer.Sound("Assets/Sounds/win.wav")
        pygame.mixer.Sound.play(winSound)

        while game_win_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            GUI.message("YOU WON!",120,165,75)
            pygame.display.update()

            time.sleep(2.5)
            GUI.draw_level_choose()

    def draw_player(x: float,y: float):
        game_display.blit(player,(x,y))

    def draw_enemy(x: float,y: float):
        game_display.blit(enemy,(x,y))

    def game_loop(difficulty: int,theme: str,level: int,finish_arg: int):
        game_loop = True

        score = 0

        is_bullet_active = False

        enemy_x = random.randrange(0,498 - enemy_height)
        enemy_y = 0 - enemy_height

        x = display_width * 0.45
        y = display_height * 0.8 - player_height/2

        if (difficulty <= 2):
            enemy_speed = difficulty * 2.5
        else:
            enemy_speed = difficulty * 1.5

        x_change = 0
        y_change = 0

        # Clear the screen
        game_display.fill(white)

        # Load the music for the level
        if (theme == "desert"):
            pygame.mixer.music.load("Assets/Sounds/dTheme.wav")
            game_display.blit(desert_level,(0,0))
        elif (theme == "forest"):
            pygame.mixer.music.load("Assets/Sounds/fTheme.wav")
            game_display.blit(forest_level,(0,0))
        elif (theme == "arctic"):
            pygame.mixer.music.load("Assets/Sounds/aTheme.wav")
            game_display.blit(arctic_level,(0,0))

        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)

        while game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Get pressed keys
            keyStates = pygame.key.get_pressed()

            # Input code
            if keyStates[pygame.K_LEFT] or keyStates[pygame.K_a]:
                x_change = -player_speed
            elif keyStates[pygame.K_RIGHT] or keyStates[pygame.K_d]:
                x_change = player_speed
            else:
                x_change = 0
                y_change = 0

            if keyStates[pygame.K_SPACE]:
                is_bullet_active = True

            # Update the position
            x += x_change
            y += y_change

            # Draw the background
            if (theme == "desert"):
                game_display.blit(desert_level,(0,0))
            elif (theme == "forest"):
                game_display.blit(forest_level,(0,0))
            elif (theme == "arctic"):
                game_display.blit(arctic_level,(0,0))

            game_functions.draw_enemy(enemy_x,enemy_y)
            game_functions.draw_player(x,y)

            if is_bullet_active:
                # Draw the bullet (or rather a huge laser beam lol)
                bulletx = x + 59
                bullety = y - 300
                pygame.draw.rect(game_display,yellow,(bulletx,bullety,10,250))

                # Collision detection code for beam and enemy
                if (enemy_y < bullety + 250):
                    if ((bulletx + 10 > enemy_x) and (bulletx < enemy_x + enemy_width)):
                        score += 1

                        # Raise difficulty for infinite level
                        if ((score % 10 == 10) and (level == 9)):
                            enemy_speed += 1

                        # Move the enemy to a new position
                        enemy_x = random.randrange(0,498 - enemy_height)
                        enemy_y = 0 - enemy_height
                        game_functions.draw_enemy(enemy_x,enemy_y)

                game_functions.wait(1)
                is_bullet_active = False

            # Check if we reached the win condition (ignore if we're playing infinite level)
            if (level != 9):
                if score == finish_arg:
                    game_functions.game_win()

            # Move the enemy
            enemy_y += enemy_speed

            # Enemy went off-screen; move it back to the top
            if (enemy_y > enemy_height + 350):
                enemy_x = random.randrange(0,498 - enemy_height)
                enemy_y = 0 - enemy_height

            # Check if player is colliding with the enemy
            if (y < enemy_y + enemy_height):
                if (x + player_width > enemy_x) and (x < enemy_x + enemy_width):
                    game_functions.game_lose(difficulty,level,theme,finish_arg)

            # Don't let player go off-screen
            if (x <= 0):
                x += player_speed
            if (x > display_width - (player_width + 63)):
                x -= player_speed

            # Draw UI
            GUI.imageButton(close,605,12.5,25,25,"",GUI.draw_level_choose)
            GUI.message("Score: "+str(score),2,5,25)

            pygame.display.update()
            clock.tick(framerate)


class GUI:
    def message(text: str,x: float,y: float,font_size: int):
        # Get the font and display the text
        font = pygame.font.Font('freesansbold.ttf',font_size)
        game_display.blit(font.render(text,False,(255,255,255)),(x,y))

    def button(color: tuple,
               x: float,
               y: float,
               width: float,
               height: float,
               text: str,
               text_x: float,
               text_y: float,
               action=None):
        # Get the pressed mouse buttons and the position of mouse
        mouse_clicked = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is inside the boundaries
        if ((x + width > mouse_pos[0] > x) and (y + height > mouse_pos[1] > y)):
            pygame.draw.rect(game_display,black,(x-5,y-5,width+10,height+10))
            pygame.draw.rect(game_display,gray,(x,y,width,height))

            # Check if LMB (left mouse button is at index 0) is pressed
            if ((mouse_clicked[0] == 1) and (action != None)):
                clickSound = pygame.mixer.Sound("Assets/Sounds/click.wav")
                pygame.mixer.Sound.play(clickSound)

                game_functions.wait(10)
                action()
        else:
            pygame.draw.rect(game_display,black,(x-5,y-5,width+10,height+10))
            pygame.draw.rect(game_display,color,(x,y,width,height))

        # Draw text
        GUI.message(text,text_x,text_y,25)

    def imageButton(image,
                    x: float,
                    y: float,
                    width: float,
                    height: float,
                    text: str,
                    action=None):
         # Get the pressed mouse buttons and the position of mouse
        mouse_clicked = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is inside the boundaries
        if ((x + width > mouse_pos[0] > x) and (y + height > mouse_pos[1] > y)):
            pygame.draw.rect(game_display,gray,(x-5,y-5,width+10,height+10))
            game_display.blit(image,(x,y))

            # Check if LMB (left mouse button is at index 0) is pressed
            if ((mouse_clicked[0] == 1) and (action != None)):
                clickSound = pygame.mixer.Sound("Assets/Sounds/click.wav")
                pygame.mixer.Sound.play(clickSound)

                game_functions.wait(10)

                action()
        else:
            pygame.draw.rect(game_display,black,(x-5,y-5,width+10,height+10))
            game_display.blit(image,(x,y))

        # Draw text
        GUI.message(text,x+25,y+105,25)

    def draw_level_choose():
        level_choose_loop = True

        # Draw the background
        game_display.fill(white)
        game_display.blit(background,(0,0))

        pygame.mixer.music.stop()

        while level_choose_loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

            #Draw all level buttons
            GUI.imageButton(desert,20,25,image_width,image_height,"Level 1",Levels.level_one)
            GUI.imageButton(forest,170,25,image_width,image_height,"Level 2",Levels.level_two)
            GUI.imageButton(arctic,320,25,image_width,image_height,"Level 3",Levels.level_three)
            GUI.imageButton(forest,470,25,image_width,image_height,"Level 4",Levels.level_four)
            GUI.imageButton(arctic,20,172,image_width,image_height,"Level 5",Levels.level_five)
            GUI.imageButton(desert,170,172,image_width,image_height,"Level 6",Levels.level_six)
            GUI.imageButton(forest,320,172,image_width,image_height,"Level 7",Levels.level_seven)
            GUI.imageButton(desert,470,172,image_width,image_height,"Level 8",Levels.level_eight)

            GUI.button(green,250,320,130,50,"INFINITE",262.5,332.5,Levels.level_infinite)

            GUI.button(blue,270,400,85,50,"BACK",277.5,412.5,GUI.menu)

            pygame.display.update()
            clock.tick(framerate)



    def menu():
        menu_loop = True

        # Draw the background
        game_display.fill(white)
        game_display.blit(background,(0,0))
        game_display.blit(player,(262.5,200))

        # Play the music
        pygame.mixer.music.load("Assets/Sounds/menutheme.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while menu_loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

            # Draw all the buttons
            GUI.button(green,80,350,100,50,"START",90,362.5,GUI.draw_level_choose)
            GUI.button(red,480,350,85,50,"EXIT",490,362.5,game_functions.game_quit)
            GUI.message("SPACE MANIA",60,100,75)

            pygame.display.update()
            clock.tick(framerate)

if (__name__ == "__main__"):
    GUI.menu()
