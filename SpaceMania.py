import pygame
import time
import random

pygame.init()

display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Space Mania")
icon = pygame.image.load("Assets/Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#=====================================================
#
#=====================================================

#=====================================================
#Images and Variables
#=====================================================
imagesWidth = 130
imagesHeight = 97

car_width = 95
car_height = 100

enemycar_width = 95
enemycar_height = 100

framerate = 60

car = pygame.image.load('Assets/Images/car.png')
enemycar = pygame.image.load('Assets/Images/enemycar.png')

desert = pygame.image.load('Assets/Images/desert.png')
forest = pygame.image.load('Assets/Images/forest.png')
arctic = pygame.image.load('Assets/Images/arctic.png')

desertLevel = pygame.image.load('Assets/Images/desertLevel.png')
forestLevel = pygame.image.load('Assets/Images/forestLevel.png')
arcticLevel = pygame.image.load('Assets/Images/arcticLevel.png')
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
#Functions
#=====================================================
class Levels:
    def levelOne():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(desertLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(1,"desert",1,10)

    def levelTwo():

        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(forestLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(2,"forest",2,15)

    def levelThree():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(arcticLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(2,"arctic",3,25)

    def levelFour():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(forestLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(3,"forest",4,35)

    def levelFive():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(arcticLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(3,"arctic",5,40)

    def levelSix():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(desertLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(4,"desert",6,50)

    def levelSeven():
        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(forestLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(4,"forest",7,60)

    def levelEight():

        levelchoosee = False

        gameDisplay.fill(white)


        gameDisplay.blit(desertLevel,(0,0))
        pygame.display.update()
        gameFunctions.game_loop(5,"desert",8,75)

    def levelInfinite():
        levelchoosee = False


        gameDisplay.fill(white)
        level = random.randrange(0,300)
        if level <= 100:
            randomLevel = desertLevel
        elif level >= 100 and level <= 200:
            randomLevel = forestLevel
        elif level >= 200 and level <= 300:
            randomLevel = arcticLevel

        gameDisplay.blit(randomLevel,(0,0))
        pygame.display.update()
        if randomLevel == desertLevel:
            gameFunctions.game_loop(1,"desert",9,0)
        elif randomLevel == forestLevel:
            gameFunctions.game_loop(1,"forest",9,0)
        elif randomLevel == arcticLevel:
            gameFunctions.game_loop(1,"arctic",9,0)

class gameFunctions:

    def wait(time):
        waiting = 0
        while waiting <= time:
            waiting += 1
            print(waiting)

    def game_quit():
        pygame.quit()
        quit()

    def game_lose(difficulty,level,theme,finishArgument1):
        gamelose = True
        gameloop = False
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))

        pygame.mixer.music.stop()

        while gamelose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #message(text,x,y,fontsize)
            GUI.message("YOU LOST!",120,165,75)
            time.sleep(2.5)
            gamelose = False
            gameDisplay.fill(white)
            gameFunctions.game_loop(difficulty,theme,level,finishArgument1)

    def game_win(level):
        gamewin = True
        gameloop = False
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))

        pygame.mixer.music.stop()
        winSound = pygame.mixer.Sound("Assets/Sounds/win.wav")
        pygame.mixer.Sound.play(winSound)

        if level == 1:
            secondLevelActive = True
            print(secondLevelActive)
        elif level == 2:
            thirdLevelActive = True
        elif level == 3:
            fourthLevelActive = True
        elif level == 4:
            fifthLevelActive = True
        elif level == 5:
            sixthLevelActive = True
        elif level == 6:
            seventhLevelActive = True
        elif level == 7:
            eigthLevelActive = True
        elif level == 8:
            infiniteLevelActive = True

        while gamewin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            GUI.message("YOU WON!",120,165,75)


            time.sleep(2.5)
            GUI.levelchoose()

    def car(carx,cary):
        #print("Carx is:",str(carx))
        #print("Cary is:",str(cary))
        gameDisplay.blit(car,(carx,cary))

    def enemycar(x,y):
        enemycar = pygame.image.load('Assets/Images/enemycar.png')
        gameDisplay.blit(enemycar,(x,y))

    def bullet(x,y):
        gameDisplay.blit(bullet,(x,y))

    def game_loop(difficulty,theme,level,finishArgument1):
        loadlevel = False
        gamelose = False
        gamewin = False
        gameloop = True

        global drivingPause
        global distanceDrived
        global destroyedCars

        drivingPause = 0
        distanceDrived = 0
        destroyedCars = 0
        speed = 0

        secondCarActive = False
        bulletActive = False

        enemyx = random.randrange(0,498 - enemycar_height)
        enemyy = 0 - enemycar_height

        x = display_width * 0.45
        y = display_height * 0.8 - car_height/2
        if difficulty <= 2:
            car_Speed = difficulty * 2.5
        else:
            car_Speed = difficulty * 1.5
        x_change = 0
        y_change = 0

        gameDisplay.fill(white)

        if theme == "desert":
            game_Theme = pygame.mixer.music.load("Assets/Sounds/dTheme.wav")
            gameDisplay.blit(desertLevel,(0,0))
        elif theme == "forest":
            game_Theme = pygame.mixer.music.load("Assets/Sounds/fTheme.wav")
            gameDisplay.blit(forestLevel,(0,0))
        elif theme == "arctic":
            game_Theme = pygame.mixer.music.load("Assets/Sounds/aTheme.wav")
            gameDisplay.blit(arcticLevel,(0,0))




        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)

        while gameloop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keyStates = pygame.key.get_pressed()

            if keyStates[pygame.K_LEFT]:
                x_change = -5
                #print("X_change is:",str(x_change))
            elif keyStates[pygame.K_RIGHT]:
                x_change = 5
                #print("X_change is:",str(x_change))
            elif keyStates[pygame.K_SPACE]:
                bulletActive = True
            else:
                x_change = 0
                y_change = 0

            x += x_change
            y += y_change

            if theme == "desert":
                gameDisplay.blit(desertLevel,(0,0))
            elif theme == "forest":
                gameDisplay.blit(forestLevel,(0,0))
            elif theme == "arctic":
                gameDisplay.blit(arcticLevel,(0,0))

            gameFunctions.enemycar(enemyx,enemyy)
            gameFunctions.car(x,y)

            if bulletActive:
                bulletx = x + 59
                bullety = y - 300
                bulletRectange = pygame.draw.rect(gameDisplay,yellow,(bulletx,bullety,10,250))
                if enemyy < bullety + 250:
                    if bulletx + 10 > enemyx and bulletx < enemyx + enemycar_width:
                        destroyedCars += 1
                        speed += 1
                        if speed == 10 and level == 9:
                            car_Speed += 1
                        enemycar.fill(transparent)
                        enemyx = random.randrange(0,498 - enemycar_height)
                        enemyy = 0 - enemycar_height
                        gameFunctions.enemycar(enemyx,enemyy)
                gameFunctions.wait(1)
                bulletActive = False

            if level != 9:
                if destroyedCars == finishArgument1:
                    gameFunctions.game_win(level)

            enemyy += car_Speed
            if enemyy > enemycar_height + 350:
                if secondCarActive:
                    enemyx = random.randrange(143,306 - enemycar_height)
                    enemyy = 0 - enemycar_height
                else:
                    enemyx = random.randrange(0,498 - enemycar_height)
                    enemyy = 0 - enemycar_height
            if y < enemyy + enemycar_height:

                if x + car_width > enemyx and x < enemyx + enemycar_width:
                    #GUI.message(text,x,y,fontsize)
                    gameFunctions.game_lose(difficulty,level,theme,finishArgument1)

            if x <= 0:
                x += 5
            if x > display_width - (car_width + 63):
                x = x - 5
            #print("X is:",str(x))
            #print("Y is:",str(y))

            #imageButton(image,x,y,wid,hei,text,action=None)
            GUI.imageButton(close,605,12.5,25,25,"",GUI.levelchoose)
            #GUI.message(text,x,y,fontsize)
            GUI.message("Score: "+str(destroyedCars),2,5,25)

            pygame.display.update()
            clock.tick(framerate)


class GUI:

    def message(text,x,y,fontsize):
        font = pygame.font.Font('freesansbold.ttf',fontsize)
        gameDisplay.blit(font.render(text,False,(255,255,255)),(x,y))
        pygame.display.update()

    def button(color,x,y,wid,hei,text,textx,texty,action=None):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if x + wid > mouse[0] > x and y + hei > mouse[1] > y:
            pygame.draw.rect(gameDisplay,black,(x-5,y-5,wid+10,hei+10))
            pygame.draw.rect(gameDisplay,gray,(x,y,wid,hei))
            if click[0] == 1 and action != None:
                clickSound = pygame.mixer.Sound("Assets/Sounds/click.wav")
                pygame.mixer.Sound.play(clickSound)
                gameFunctions.wait(10)
                action()

        else:
            pygame.draw.rect(gameDisplay,black,(x-5,y-5,wid+10,hei+10))
            pygame.draw.rect(gameDisplay,color,(x,y,wid,hei))

        GUI.message(text,textx,texty,25)
        pygame.display.update()

    def imageButton(image,x,y,wid,hei,text,action=None):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if x + wid > mouse[0] > x and y + hei > mouse[1] > y:
            pygame.draw.rect(gameDisplay,gray,(x-5,y-5,wid+10,hei+10))
            gameDisplay.blit(image,(x,y))
            if click[0] == 1 and action != None:
                clickSound = pygame.mixer.Sound("Assets/Sounds/click.wav")
                pygame.mixer.Sound.play(clickSound)
                gameFunctions.wait(10)
                action()

        else:
            pygame.draw.rect(gameDisplay,black,(x-5,y-5,wid+10,hei+10))
            gameDisplay.blit(image,(x,y))

        #GUI.message(text,x,y,fontsize)
        GUI.message(text,x+25,y+105,25)
        pygame.display.update()

    def levelchoose():
        global imagesWidth
        global imagesHeight

        menuu = False
        gameloop = False
        levelchoosee = True
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))

        pygame.mixer.music.stop()

        while levelchoosee:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #imageButton(image,x,y,wid,hei,text,action=None)
            GUI.imageButton(desert,20,25,imagesWidth,imagesHeight,"Level 1",Levels.levelOne)
            GUI.imageButton(forest,170,25,imagesWidth,imagesHeight,"Level 2",Levels.levelTwo)
            GUI.imageButton(arctic,320,25,imagesWidth,imagesHeight,"Level 3",Levels.levelThree)
            GUI.imageButton(forest,470,25,imagesWidth,imagesHeight,"Level 4",Levels.levelFour)
            GUI.imageButton(arctic,20,172,imagesWidth,imagesHeight,"Level 5",Levels.levelFive)
            GUI.imageButton(desert,170,172,imagesWidth,imagesHeight,"Level 6",Levels.levelSix)
            GUI.imageButton(forest,320,172,imagesWidth,imagesHeight,"Level 7",Levels.levelSeven)
            GUI.imageButton(desert,470,172,imagesWidth,imagesHeight,"Level 8",Levels.levelEight)
            #if infiniteLevelActive:
            GUI.button(green,250,320,130,50,"INFINITE",262.5,332.5,Levels.levelInfinite)

##            print(secondLevelActive)
##            print(thirdLevelActive)
##            print(fourthLevelActive)
##            print(fifthLevelActive)
##            print(sixthLevelActive)
##            print(seventhLevelActive)
##            print(eighthLevelActive)
##            print(infiniteLevelActive)

            #GUI.button(color,x,y,wid,hei,text,textx,texty,action)
            GUI.button(blue,270,400,85,50,"BACK",277.5,412.5,GUI.menu)
            pygame.display.update()
            clock.tick(framerate)



    def menu():
        menuu = True
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(car,(262.5,200))

        menu_Theme = pygame.mixer.music.load("Assets/Sounds/menutheme.wav")
        pygame.mixer.music.play(-1)

        while menuu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #GUI.button(color,x,y,wid,hei,text,textx,texty,action)
            GUI.button(green,80,350,100,50,"START",90,362.5,GUI.levelchoose)
            GUI.button(red,480,350,85,50,"EXIT",490,362.5,gameFunctions.game_quit)
            GUI.message("SPACE MANIA",60,100,75)
            pygame.display.update()
            clock.tick(framerate)


GUI.menu()
