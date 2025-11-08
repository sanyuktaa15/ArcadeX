import pygame
import time
import random
pygame.font.init() #initialize the font module -- reuirement of the pygame!!


#creating windows
WIDTH, HEIGHT = 800 , 500  #comstant values 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #tuples
pygame.display.set_caption("Space Dodge")  #we wrote title of the game
#WIN is a surface object, badme used to draw things

BG = pygame.image.load("bgimg.png")  #attached the bg pic
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))  #this is necessary otherwise if the image is not 1000x600, it will not fill  up the screen

PLAYER_WIDTH = 120 
PLAYER_HEIGHT = 130
PLAYER_VELOCITY = 5

PLAYER_IMG = pygame.image.load("player.png").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

PLAYER_VELOCITY = 5

RAINDROP_WIDTH = 6
RAINDROP_HEIGHT = 15
RAINDROP_VELOCITY = 2

FONT = pygame.font.Font("PressStart2P-Regular.ttf", 22)
BIG_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 60)  # Bigger font for the 'You Lost' text

#we'll do all the drawing in a new functin just to keep it clear

def draw(player, elapsed_time, drops):   #pass the player in draw function
        
        WIN.blit(BG , (0,0))  #blit is used when an image is to be used onto the screen
        #to draw elapsedtime we need to font, hence we initialised the font
        
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1 , "white")
        #here first we passed the dtring which we want to render on the screen, we used a fstring, first wew did Time: rounded off the elapsed timw to the nearest second, 1 makes text to look better, the text is white 
        
        WIN.blit(time_text , (10,10)) #blits the time display?
        
        
        WIN.blit(PLAYER_IMG, (player.x, player.y))

        #telling what to draw: WIN se where i want to draw my rectangle, then colour, then coordinates of the rectangle
        
        #adding stars/ passing stars to the draw function
        #if you draw them beofre the player it will appear behind the player and if you draw aftter the player it will appear on top of the player
        
        for drop in drops:
            x, y = drop.centerx, drop.centery
            
            # draw the rounded bottom
            pygame.draw.circle(WIN, (100, 180, 255), (x, y + 4), 4)

            # draw the pointy top (small triangle)
            tip = (x, y - 6)
            left = (x - 3, y + 2)
            right = (x + 3, y + 2)
            pygame.draw.polygon(WIN, (100, 180, 255), [tip, left, right])


        
        pygame.display.update()  #applies all the draws we make (above done)



#in python the (0,0) coordinates are on the top left of the screen
#y  increases downwards and x inc to rhs
def main():

    run = True #controls the main game loop

    #create a moving player
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH * 0.6, PLAYER_HEIGHT * 0.8)
    player.centerx = WIDTH // 2  # recenter player if needed

                        #player is at bottom line, 200 to the right, then we pass his width and height

    clock = pygame.time.Clock()  #a object - runs the loop in a specific time only, no matter how fast the while loop is running
    
    #keeping track of time
    start_time = time.time() #gives us the current time
    elapsed_time = 0 


    drop_add_increment = 500 #first star will be added in 2000 milliseconds
    drop_count = 0 #tells us when we should add another star

    drops = []
    hit = False
    last_increment_time = 0


    while run:  #main game loop

        drop_count += clock.tick(60)  #clock,tick(60) will run the loop max 60 times per second,,,,, star_count += clock.tick(60) is essentially counting how many milli seconds have occured since the last clock tick; means we are doing this to keep precise tarck of the time
        elapsed_time = time.time() - start_time #time is the current time
                # every 4 seconds, increase star spawn frequency
        if elapsed_time - last_increment_time >= 4:
            drop_add_increment = max(200, drop_add_increment - 50)
            last_increment_time = elapsed_time


        #generation of stars:
        if drop_count > drop_add_increment:
            for _ in range(1):
                drop_x  = random.randint(0, WIDTH - RAINDROP_WIDTH)
                drop = pygame.Rect(drop_x, -RAINDROP_HEIGHT, RAINDROP_WIDTH, RAINDROP_HEIGHT) #negative because neeche aa rha hai toh value badhne pe neeche aayega((0,0) is at top left) negative star height and we did not put zero because we did not want the star to pop up, it will come form top
                drops.append(drop)

            drop_add_increment = max(200, drop_add_increment - 50) #generates stars faster, minimum value will be 200 milli seconds
            drop_count = 0


        #events of the game
        for event in pygame.event.get():  #a list that contains events like key presses, movements, quit which occur in the last iterartion of the loop 
            if event.type == pygame.QUIT:
                run = False #loop stops
                break  #loop exit


        #moving the stars
        for drop in drops[:]: #making a copy of the stars list, because we will remove the ones which hit the player or the ones which hit the ground, making a copy helps as when i modify the list while working on it, it can show a lot of wierd errors. modifying the 
            drop.y += RAINDROP_VELOCITY
            if drop.y > HEIGHT:
                drops.remove(drop)
            elif drop.y + drop.height >= player.y and drop.colliderect(player):
                drops.remove(drop)
                hit = True
                break


#to move the player we must listen to the key presses!

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0 :  #this is just the code for left key(look-up pygame key codes)
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:  #this is just the code for left key(look-up pygame key codes)
            player.x += PLAYER_VELOCITY
        draw(player, elapsed_time, drops)


        if hit:
            
            lose_text = BIG_FONT.render("You Lost!", 1, (255,0,0))
            WIN.blit(lose_text, (WIDTH/2 - lose_text.get_width()/2, HEIGHT/2 - lose_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elapsed_time, drops)
    pygame.quit() #closes pygame

if __name__ == "__main__": #function calling
    main()