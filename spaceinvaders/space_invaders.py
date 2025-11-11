import pygame
import os
import time
import random
pygame.font.init()

#convention in python is named in capitals and baki in lowercase, hence spaceship and laser capital kiya
WIDTH = 750
HEIGHT = 675

WIN = pygame.display.set_mode((WIDTH , HEIGHT)) #by this we set the window
pygame.display.set_caption("Space Invaders") #named the window, by default it would be "pygame window"

#load images
RED_SPACESHIP = pygame.image.load(os.path.join("Assets" , "pixel_ship_red_small.png"))
                #from the pygame module use the image.load method, then load the image that is located at os.path.join which is in assets
GREEN_SPACESHIP = pygame.image.load(os.path.join("Assets" , "pixel_ship_green_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("Assets" , "pixel_ship_blue_small.png"))

#player ship
YELLOW_SPACESHIP = pygame.image.load(os.path.join("Assets" , "pixel_ship_yellow.png"))

#lasers
RED_LASER = pygame.image.load(os.path.join("Assets" , "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Assets" , "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Assets" , "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Assets" , "pixel_laser_yellow.png"))

#background 
BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "background-black.png")) , (WIDTH , HEIGHT)) #two arguments, the bg img and its scale

class Laser:
    def __init__(self, x , y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,window):
       window.blit(self.img, (self.x, self.y)) 

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (self.y <= height or self.y >= 0)
    
    def collision(self, obj):
        return collide(obj, self)
    
class Ship: #oop  ; this is a general class, badme we will use childclass
    
    COOLDOWN = 10  

    def __init__(self , x , y , health = 100): #constructor

            self.x = x #position
            self.y = y
            self.health = health
            self.ship_img = None #These will later store what the ship looks like and what its laser looks like.
            self.laser_img = None
            self.lasers = [] #Every ship can shoot multiple lasers. This list will store all the lasers that the ship fires.
            self.cool_down_counter = 0 #This is a timer that helps control how fast the ship can shoot. Without it, the player could just spam bullets every frame.
    
    def draw(self, window):

        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        else:
            self.cool_down_counter += 1


    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACESHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def health_bar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
                

class Enemy(Ship):
    COLOUR_MAP = {
                "red":(RED_SPACESHIP, RED_LASER),
                "green":(GREEN_SPACESHIP, GREEN_LASER),
                "blue":(BLUE_SPACESHIP, BLUE_LASER)
                }
    
    def __init__(self, x, y, colour, health = 100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOUR_MAP[colour]
        self.mask = pygame.mask.from_surface(self.ship_img)

    
    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None 

def main():
    run = True
    FPS = 60 #frames per seconds/ 60 times per second loop ruun karega, sets how fast/slpw the game is gonna run
    clock = pygame.time.Clock()
    level = 1
    lives = 5  
    main_font = pygame.font.Font("PressStart2P-Regular.ttf" , 22) #here because we have downloaded and atteched a file, we used font.font, if we were using the fonts already in pygame we couldve used font.SysFont
    lost_font = pygame.font.Font("PressStart2P-Regular.ttf" , 52) #here because we have downloaded and atteched a file, we used font.font, if we were using the fonts already in pygame we couldve used font.SysFont

    player_vel = 5 #ships position changes by 5 pixels when you press the key once
    laser_vel = 5
    player = Player(WIDTH//2 - 25, HEIGHT - 130) #ship and its position
    
    player_width = player.ship_img.get_width()
    player_height = player.ship_img.get_height()


    enemies = []
    wave_length = 5
    enemy_vel = 1 + (level * 0.2)
    
    lost = False

    # .blit() tells pygame to put the text or image onto the window
    
    def redraw_window(): #we used function inside function here so that we can access all the already deifned variables run fps in this; also we can only call this function inside main()
        WIN.blit(BG, (0,0)) # draw bg img at 0,0

        #draw text
        lives_label = main_font.render(f"Lives: {lives}" , 1 , (255,0,0)) #always just ahve to use 1 when rendering
        level_label = main_font.render(f"Level: {level}" , 1 , (0,230,255))
        
        
        WIN.blit(level_label, (WIDTH - 10 - level_label.get_width(), 10)) #level are at the rhs at a distance 10 from border, we solved it like this because we dont know the width of the text
        WIN.blit(lives_label, (10,10))

        player.draw(WIN)


        for enemy in enemies:
            enemy.draw(WIN) # this works because this inherits from ship, ship has a draw method and we have defined the ship in here

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))
        pygame.display.update() #this refreshes/updates my surface

    while run:
        clock.tick(FPS) #saare computers pe same speed mein chalega no matter what
        
        # ensure at least 5 enemies are always on screen
        if len(enemies) < 10:
            enemy = Enemy(
                random.randrange(50, WIDTH - 100),     # random x
                random.randrange(-1500, -100),         # start off-screen (above)
                random.choice(["red", "blue", "green"])  # random color/type
            )
            enemies.append(enemy)

        if lives <= 0 or player.health <= 0:
            lost = True
            flash_duration = 80   # milliseconds per flash — half as fast as before

            for i in range(12):  # more flashes, faster pace
                WIN.blit(BG, (0, 0))

                # alternate red and transparent black every frame
                if i % 2 == 0:
                    lost_label = lost_font.render("YOU LOST!!", True, (255, 0, 0))
                else:
                    lost_label = lost_font.render("YOU LOST!!", True, (0, 0, 0))

                WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))
                pygame.display.update()
                pygame.time.delay(flash_duration)

            # hold final text for readability
            final_label = lost_font.render("YOU LOST!!", True, (255, 0, 0))
            WIN.blit(BG, (0, 0))
            WIN.blit(final_label, (WIDTH/2 - final_label.get_width()/2, HEIGHT/2 - final_label.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1500)

            run = False 


    
        #check if player has quit the window/game
        for event in pygame.event.get(): #check if any event has occured
            #note: event is not a keyword, it is a variable used to represent each event from pygame event in queue
            if event.type == pygame.QUIT:  #pygame.QUIT is a Pygame event constant, it checks if the user has pressed the X of the window and exited
                run = False
    
        if len(enemies) == 0:
            level +=1
            wave_length += 5

            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500,-1000), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        keys  = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: #left and the regin when we press left where the player is allowed to move
            player.x -= player_vel                             #we count this posiyion by the player bloack fro its top left position

        if keys[pygame.K_RIGHT] and player.x + player_vel < WIDTH - player_width : #right
            player.x += player_vel

        if keys[pygame.K_UP] and player.y -player_vel > 0: #up
            player.y -= player_vel

        if keys[pygame.K_DOWN] and player.y + player_vel + 20 < HEIGHT - player_height : #down
            player.y += player_vel

        if keys[pygame.K_SPACE]:
            player.shoot()


        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10

            elif enemy.y > HEIGHT:
                lives -= 1
                enemies.remove(enemy)


        player.move_lasers(-laser_vel, enemies)

        redraw_window()

def main_menu():
    run = True
    title_font = pygame.font.Font("PressStart2P-Regular.ttf", 32)

    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Click to begin...", 1 , (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT/2 - title_label.get_height()/2))
        run = True

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

main_menu() 
