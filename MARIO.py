import pygame
pygame.init()

#Global variable
global screen
screen = 1
screenWidth = 600
screenHeight = 380

#Create Pygame window
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Mario")

#Load images
try:
    ICON = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/super-mario.png')
    MarioR1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/R1.gif')
    MarioR2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/R2.gif')
    MarioR3 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/R3.gif')
    MarioL1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/L1.gif')
    MarioL2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/L2.gif')
    MarioL3 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/L3.gif')
    bg = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/BG.png')
    char = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/Standing.gif')
    coinBox = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/CoinBox.png')
    coinBox2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/coinBox2.png')
    coin = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/coin.png')
    Brick = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/brick.png')
    TurtleRight = [pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/E_R1.gif'),
                   pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/E_R2.gif')]
    TurtleLeft = [pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/E_L1.gif'),
                  pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/E_l2.gif')]
    TurtleDeath = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/E_Death.gif')
    Tube = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/Tube.png')
    TubeCopy = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/Tube copy.png')
    flower = [pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/P1.gif'),
              pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/P2.gif')]
    Mushroom_1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/M_1.gif')
    Mushroom_2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/M_2.gif')
    Mario_mushroom = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/Mario_mushroom.png')
    Mushroom_Death = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/M_death.gif')
    CL1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/CL1.gif')
    CL2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/CL2.gif')
    CR1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/CR1.gif')
    CR2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/CR2.gif')
    RT1 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/RedTurtle1.gif')
    RT2 = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/RedTurtle2.gif')
    block = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/block.png')
    flag = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/flag.png')
    castle = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/castle.png')
    Mflag = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/Mflag.gif')
    start = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/startscreen.gif')
    scoreT = pygame.image.load('/Users/jojo/Documents/y1s1/Python/Mario/Pic/score.png')

except:
    print('could not load image')
    
#Rezise images
MarioR1_B = pygame.transform.scale(MarioR1, (50, 50))
MarioR2_B = pygame.transform.scale(MarioR2, (50, 50))
MarioR3_B = pygame.transform.scale(MarioR3, (50, 50))
MarioL1_B = pygame.transform.scale(MarioL1, (50, 50))
MarioL2_B = pygame.transform.scale(MarioL2, (50, 50))
MarioL3_B = pygame.transform.scale(MarioL3, (50, 50))
char_B = pygame.transform.scale(char, (50, 50))
Mario_mushroomB = pygame.transform.scale(Mario_mushroom, (30, 30))
Mushroom_1B = pygame.transform.scale(Mushroom_1, (40, 40))
Mushroom_2B = pygame.transform.scale(Mushroom_2, (40, 40))
CL1_B = pygame.transform.scale(CL1, (40, 40))
CL2_B = pygame.transform.scale(CL2, (40, 40))
CR1_B = pygame.transform.scale(CR1, (40, 40))
CR2_B = pygame.transform.scale(CR2, (40, 40))
RT1_B = pygame.transform.scale(RT1, (40, 40))
RT2_B = pygame.transform.scale(RT2, (40, 40))
block_B = pygame.transform.scale(block, (20, 20))
flag_B = pygame.transform.scale(flag, (170, 200))
castle_B = pygame.transform.scale(castle, (150, 120))
Mushroom_DeathB = pygame.transform.scale(Mushroom_Death, (40, 40))
Tubecopy = pygame.transform.scale(TubeCopy,(60,60))
TubeBig = pygame.transform.scale(Tube,(60,60))
Brick_big = pygame.transform.scale(Brick,(30,30))
TurtleDeath = pygame.transform.scale(TurtleDeath, (30, 30))
coinBox_big = pygame.transform.scale(coinBox, (30, 30))
coinBox2_big = pygame.transform.scale(coinBox2, (30, 30))
coin_big = pygame.transform.scale(coin, (20, 20))

#List sprite sheet
walkRight = [MarioR1,MarioR2,MarioR3]
walkLeft_B = [MarioL1_B,MarioL2_B,MarioL3_B]
walkLeft = [MarioL1,MarioL2,MarioL3]
walkRight_B = [MarioR1_B,MarioR2_B,MarioR3_B]
Mushroom = [Mushroom_1B,Mushroom_2B]
cloudLeft = [CL1_B,CL2_B]
cloudRight = [CR1_B,CR2_B]
RedTurtle = [RT1_B,RT2_B]

#Import music
try:
    bumpSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/bump.wav")
    coinSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/coin.wav")
    music = pygame.mixer.music.load("/Users/jojo/Documents/y1s1/Python/Mario/Music/main_theme.wav")
    jumpSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/small_jump.wav")
    stompSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/stomp.wav")
    kickSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/kick.wav")
    powerupSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/powerup.wav")
    flagSound = pygame.mixer.Sound("/Users/jojo/Documents/y1s1/Python/Mario/Music/Flag.wav")
except:
    print("Could not load music")
    
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()

#Font
font = pygame.font.SysFont(None,25)
pygame.display.set_icon(ICON)


##Class Button
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#Class Mario        
class player(object):
    def __init__(self,x,y,width,height,walkLeft,walkRight,walkLeft_B,walkRight_B):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.neg = 1
        self.kill = False
        self.big = False
        self.death = False


    #draw mario
    def draw(self,win):
        global screen
        if self.death == True:
            screen = 6
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
            
        if self.left:
            if self.big == False:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            else:
                win.blit(walkLeft_B[self.walkCount//3],(self.x,self.y-20))
            self.walkCount +=1
            
        elif self.right:
            if self.big == False:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            else:
                win.blit(walkRight_B[self.walkCount//3], (self.x,self.y-20))
            self.walkCount += 1
        else:
            if end.F == False:
                if self.big == False:
                    win.blit(char, (self.x, self.y))
                else:
                    win.blit(char_B, (self.x, self.y-20))
            else:
                win.blit(Mflag, (self.x, self.y))
            self.walkCount = 0
            self.kill = False
            
            
        #Rect
        if self.big == False:
            self.hitbox = pygame.Rect(self.x-5,self.y,28,30)
        else:
            self.hitbox = pygame.Rect(self.x-5,self.y,28,30)

#Class display score and coin
class Score():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
    #function coin message
    def Coin_Message(self,win):
        global screen
        screen_text = font.render(box.msg, True, (0,0,0))
        win.blit(screen_text,[250,200])
        win.blit(coin_big, (230, 196))
        
    #function score message 
    def Score_Message(self,win):
        screen_text_score = font.render(box.score, True, (0,0,0))
        win.blit(screen_text_score,[300,200])
        win.blit(scoreT,(190,100))

    def StartOver(self):
        global screen
        screen = 2
        man.death = False
        man.x = 50
        man.y = 300
        man.big = False
        man.isJump = False
        man.Jumpcount = 0
        box.msg_score = 0
        box.msg_coin = 0
        box.score = "%04d"%box.msg_score
        box.msg = "%02d"%box.msg_coin
        end.F = False
        Mush.right = True
        Mush.left = False
        Mush.death = False
        Mush.kick = False
        Mush.x = 400
        Mush.y = 290
        Mush.count = 0
        box.coin = False
        box.count_coin = 0
        box.brick = True
        box.brick2 = True
        box.coin2 = False
        box.count_coin2 = 0
        box.coin3 = False
        box.count_coin3 = 0
        box.coin4 = False
        box.count_coin4 = 0
        box.MarioBig =  False
        turtle.x = 300
        turtle.y = 300
        turtle.walkCount = 0
        turtle.right = True
        turtle.left = False
        turtle.death = False
        turtle.kick = False
        turtle.count = 0
                   
    
##Start screen
class Start():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #function render images
    def draw(self,win):
        global screen
        win.blit(start, (self.x,self.y))

#class last stage        
class End():
    def __init__(self):
        self.F = False

    #render bricks
    def box(self,win):
        win.blit(block_B, (100,305))
        win.blit(block_B, (120,305))
        win.blit(block_B, (140,305))
        win.blit(block_B, (160,305))
        win.blit(block_B, (180,305))
        win.blit(block_B, (200,305))
        win.blit(block_B, (220,305))
        win.blit(block_B, (240,305))
        win.blit(block_B, (260,305))
        win.blit(block_B, (120,285))
        win.blit(block_B, (140,285))
        win.blit(block_B, (160,285))
        win.blit(block_B, (180,285))
        win.blit(block_B, (200,285))
        win.blit(block_B, (220,285))
        win.blit(block_B, (240,285))
        win.blit(block_B, (260,285))
        win.blit(block_B, (140,265))
        win.blit(block_B, (160,265))
        win.blit(block_B, (180,265))
        win.blit(block_B, (200,265))
        win.blit(block_B, (220,265))
        win.blit(block_B, (240,265))
        win.blit(block_B, (260,265))
        win.blit(block_B, (160,245))
        win.blit(block_B, (180,245))
        win.blit(block_B, (200,245))
        win.blit(block_B, (220,245))
        win.blit(block_B, (240,245))
        win.blit(block_B, (260,245))
        win.blit(block_B, (180,225))
        win.blit(block_B, (200,225))
        win.blit(block_B, (220,225))
        win.blit(block_B, (240,225))
        win.blit(block_B, (260,225))
        win.blit(block_B, (200,205))
        win.blit(block_B, (220,205))
        win.blit(block_B, (240,205))
        win.blit(block_B, (260,205))
        win.blit(block_B, (220,185))
        win.blit(block_B, (240,185))
        win.blit(block_B, (260,185))
        win.blit(block_B, (240,165))
        win.blit(block_B, (260,165))
        
    #hitbox bricks
    def hit(self,win):
        self.rect_block_1 = (100,305,10,1)
        if man.hitbox.colliderect(self.rect_block_1) and man.isJump == False:
            man.x = 100-25
        self.rect_block_1y = (105,305,15,20)
        if man.hitbox.colliderect(self.rect_block_1y) and man.isJump == True:
            man.y = 305-30
            man.jumpCount = -2
            if keys[pygame.K_SPACE]:
                    man.jumpCount = 10
                    jumpSound.play()
                    
        self.rect_block_2 = (120,290,1,10)
        self.RectBlock2 = pygame.draw.rect(win,(0,0,0),self.rect_block_2)
        if man.hitbox.colliderect(self.rect_block_2):
            man.x = 120-25
        self.rect_block_2y = (125,285,15,20)
        if man.hitbox.colliderect(self.rect_block_2y):
            man.y = 285-30
            man.jumpCount = -2
            if keys[pygame.K_SPACE]:
                    man.jumpCount = 10
                    jumpSound.play()
                    
        self.rect_block_3 = (140,265,20,20)
        if man.hitbox.colliderect(self.rect_block_3):
            if man.y <= 275:
                man.y = 265-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    man.jumpCount = 10
                    jumpSound.play()
            else:
                man.x = 140+20
                
        self.rect_block_4 = (160,245,20,20)
        if man.hitbox.colliderect(self.rect_block_4):
            if man.y <= 255:
                man.y = 245-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
            else:
                man.x = 160+20
                
        self.rect_block_5 = (180,225,20,20)
        if man.hitbox.colliderect(self.rect_block_5):
            if man.y <= 235:
                man.y = 225-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
            else:
                man.x = 180+20
                
        self.rect_block_6 = (200,205,20,20)
        if man.hitbox.colliderect(self.rect_block_6):
            if man.y <= 215:
                man.y = 205-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
            else:
                man.x = 200+20
                
        self.rect_block_7 = (220,185,40,20)
        if man.hitbox.colliderect(self.rect_block_7):
            if man.y <= 195:
                man.y = 185-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
            else:
                man.x = 220+20

        self.rect_block_8 = (240,165,20,20)
        if man.hitbox.colliderect(self.rect_block_8):
            if man.y <= 175:
                man.y = 165-30
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
            else:
                man.x = 240+20
                
        self.rect_block_9 = (260,185,20,140)
        if man.hitbox.colliderect(self.rect_block_9):
            man.x = 280+5

    #Ending flag     
    def flag(self,win):
        global screen
        self.rect_flag = (375,125,20,180)
        self.rectC = (485,280,20,50)
        
        win.blit(flag_B, (300,125))
        win.blit(castle_B, (420,210))
        
        if man.hitbox.colliderect(self.rect_flag) and self.F == False:
            man.y = 125
            flagSound.play()
            if man.y == 125:
                self.F = True
            
        if self.F == True:
            man.y += 5
            man.isJump = False
            if man.y >= 300:
                man.y = 300
                man.x += 2
                if man.hitbox.colliderect(self.rectC):
                    screen+=1
                    
    #display coing message               
    def Coin_Message(self,win):
        screen_text = font.render(box.msg, True, (0,0,0))
        win.blit(screen_text,[20,3])
        win.blit(coin_big, (0, 0))
        
    #display score message
    def Score_Message(self,win):
        screen_text_score = font.render(box.score, True, (0,0,0))
        win.blit(screen_text_score,[100,3])
           
            
#class Cloud     
class Cloud():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.walkCount = 0
        self.right = True
        self.left = False
        self.yTurtle = self.y
        self.yTurtle2 = self.y
        self.yTurtle3 = self.y
        self.yTurtle4 = self.y
        self.xTurtle = self.x
        self.xTurtle2 = self.x
        self.xTurtle3 = self.x
        self.xTurtle4 = self.x
        self.count = 0

    #function hitbox turtle  
    def drawCloud(self,win):
        global screen
        self.rect_Tao1 = (self.xTurtle+5,self.yTurtle+3,30,30)
        self.rect_Tao2 = (self.xTurtle2+5,self.yTurtle2+3,30,30)
        self.rect_Tao3 = (self.xTurtle3+5,self.yTurtle3+3,30,30)
        self.rect_Tao4 = (self.xTurtle4+5,self.yTurtle4+3,30,30)
        
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        if self.x <= 500 and self.right == True:
            self.x += self.vel 
            win.blit(cloudLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
            if self.x == 500:
                self.right = False
                self.left = True
                
            
        elif self.x >= 200 and self.left == True:
            self.x -= self.vel 
            win.blit(cloudRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            if self.x == 200:
                self.right = True
                self.left = False
        #summon turtle1     
        if self.yTurtle == 300:
            self.yTurtle = self.y
            self.xTurtle = self.x    
        win.blit(RedTurtle[self.walkCount//3], (self.xTurtle,self.yTurtle))
        self.yTurtle += 2

        ##Collision
        if man.hitbox.colliderect(self.rect_Tao1):
            if man.big == True:
                man.jumpCount = 8
                man.big = False
            else:
                man.death = True
            
        #summon turtle2      
        self.count +=1
        if self.count >= 30:
            if self.count == 30:
                self.xTurtle2 = self.x 
            if self.yTurtle2 == 300:
                self.yTurtle2 = self.y
                self.xTurtle2 = self.x    
            win.blit(RedTurtle[self.walkCount//3], (self.xTurtle2,self.yTurtle2))
            self.yTurtle2 += 2.5
            
        ##Collision
        if man.hitbox.colliderect(self.rect_Tao2):
            if man.big == True:
                man.jumpCount = 8
                man.big = False
            else:
                man.death = True
        
        #summon turtle3     
        if self.count >= 75:
            if self.count == 75:
                self.xTurtle3 = self.x 
            if self.yTurtle3 >= 300:
                self.yTurtle3 = self.y
                self.xTurtle3 = self.x    
            win.blit(RedTurtle[self.walkCount//3], (self.xTurtle3,self.yTurtle3))
            self.yTurtle3 += 3
            
        ##Collision
        if man.hitbox.colliderect(self.rect_Tao3):
            if man.big == True:
                man.jumpCount = 8
                man.big = False
            else:
                man.death = True
                
        #summon turtle4
        if self.count >= 90:
            if self.count == 90:
                self.xTurtle4 = self.x 
            if self.yTurtle4 >= 300:
                self.yTurtle4 = self.y
                self.xTurtle4 = self.x    
            win.blit(RedTurtle[self.walkCount//3], (self.xTurtle4,self.yTurtle4))
            self.yTurtle4 += 4
            
        ##Collision
        if man.hitbox.colliderect(self.rect_Tao4):
            if man.big == True:
                man.jumpCount = 8
                man.big = False
            else:
                man.death = True
                
    #display coin message          
    def Coin_Message(self,win):
        screen_text = font.render(box.msg, True, (0,0,0))
        win.blit(screen_text,[20,3])
        win.blit(coin_big, (0, 0))
        
    #display score message   
    def Score_Message(self,win):
        screen_text_score = font.render(box.score, True, (0,0,0))
        win.blit(screen_text_score,[100,3])
            
       
#class mushroom        
class MushRoom():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.walkCount = 0
        self.right = True
        self.left = False
        self.death = False
        self.kick = False
        self.count = 0
        

    #function collision mushroom 
    def drawEnemy(self,win):
        self.rect_Mushroom = (self.x+5,self.y,30,30)
        if self.death == False:
            if self.walkCount + 1 >= 6:
                self.walkCount = 0
            if self.x <= 500 and self.right == True and self.death == False:
                self.x += 1
                win.blit(Mushroom[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
                if self.x == 500:
                    self.right = False
                    self.left = True
                    
                
            elif self.x >= 400 and self.left == True and self.death == False:
                self.x -= 1
                win.blit(Mushroom[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                if self.x == 400:
                    self.right = True
                    self.left = False
                
        elif self.death == True:
            win.blit(Mushroom_DeathB, (self.x+5,self.y))

    #function stomp on mushroom
    def stomp(self,win):
        global screen
        if man.hitbox.colliderect(self.rect_Mushroom):
            if man.isJump == True:
                man.jumpCount = 8
                stompSound.play()
                self.death = True
                self.count +=1
                if self.count >2:
                    self.kick = True
                box.msg_score += 500
                box.score = "%04d"%box.msg_score
                
            elif man.isJump == False and self.death == False:
                if man.big == True:
                    man.jumpCount = 8
                    man.big = False
                else:
                    man.death = True
                
            elif self.death == True:
                self.kick = True
                kickSound.play()
                
                
        if self.kick == True and self.x<700:
            self.x+=20
                
#class Tube       
class Tube():
    def __init__(self):
        self.rect_tube = (195,265,65,60)
        self.rect_tube2 = (300,200,60,130)
        self.rect_floor = (0,325,700,200)
        self.rect_flower = (318,175,20,20)
        self.ontube = False
        self.walkCount = 0

    #function render tube
    def draw(self,win):
        win.blit(TubeBig, (200, 265))
        win.blit(TubeBig, (300, 200))
        win.blit(Tubecopy, (300, 230))
        win.blit(Tubecopy, (300, 265))
    

    #function collision tube
    def hit(self,win):
        ##Tube1
       
        if man.hitbox.colliderect(self.rect_tube):
            if man.isJump == True:
                self.ontube = True
                man.y = 235
            if man.big == False:
                if man.x<=200:
                    man.x = 176
                if man.x >=250 and man.isJump == False:
                    man.x = 261
            if man.big == True:
                if man.x<=180:
                    man.x = 160
                if man.x >= 240 and man.isJump == False:
                    man.x = 251
                    
        if man.big == False:         
            if (man.x < 176 or man.x > 251) and man.isJump == False:
                man.y += 30
                self.ontube = False
                if man.y >= 300:
                    man.y = 300
                    
        elif man.big == True:
            if (man.x < 180 or man.x > 230) and man.isJump == False:
                man.y += 30
                self.ontube = False
            if man.y >= 300:
                man.y = 300
                    
        if man.hitbox.colliderect(self.rect_floor):
            man.y = 300
            
        ##Tube2
        
        if man.hitbox.colliderect(self.rect_tube2):
            if man.big == False:
                if man.x<=285:
                    man.x = 280
                elif man.x >=355 and man.isJump == False:
                    man.x = 360
                    
            if man.big == True:
                if man.x<=265:
                    man.x = 260
                elif man.x >=335 and man.isJump == False:
                    man.x = 350
                
            else:
                man.y = 170
                man.jumpCount = -2
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 10
                    
        if man.x<250 and man.x>200 and man.isJump == False:
            man.y = 235

    #function collision flower               
    def flower(self,win):
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        
        win.blit(flower[self.walkCount//3],(320,170))
        self.walkCount +=1

        if man.hitbox.colliderect(self.rect_flower):
            if man.big == True:
                man.jumpCount = 10
                man.big = False
            else:
                man.death = True

    #function display message
    def Coin_Message(self,win):
        screen_text = font.render(box.msg, True, (0,0,0))
        win.blit(screen_text,[20,3])
        win.blit(coin_big, (0, 0))
        
    #function display score
    def Score_Message(self,win):
        screen_text_score = font.render(box.score, True, (0,0,0))
        win.blit(screen_text_score,[100,3])
        

#class coin box
class Coin():
    def __init__(self):
        #Rect
        self.rect = (202,152,25,25)
        self.rect_brick = (350,152,25,25)
        self.rect_coin2 = (382,152,25,25)
        self.rect_brick2 = (415,152,20,25)
        self.rect_coin3 = (382,50,20,25)

        ##Coin1
        self.coin = False
        self.count_coin = 0
        self.msg_coin = 0
        self.msg = "%02d"%self.msg_coin

        ##Brick
        self.brick = True
        self.brick2 = True

        ##Coin
        self.coin2 = False
        self.count_coin2 = 0
        self.coin3 = False
        self.count_coin3 = 0
        self.coin4 = False
        self.count_coin4 = 0
        self.MarioBig =  False
        #Score
        self.msg_score = 0
        self.score = "%04d"%self.msg_score

    #function render coin images
    def draw(self,win):
        
        self.test_rect = pygame.draw.rect(win,(255,0,0),self.rect)
            
        if self.coin == False:
            win.blit(coinBox_big, (200, 150))
        else:
            win.blit(coinBox2_big, (200, 150))
        win.blit(coin_big, (0, 0))

        if self.coin2 == False:
            win.blit(coinBox_big, (380, 152))
        else:
            win.blit(coinBox2_big, (380, 152))

        if self.coin3 == False:
            win.blit(coinBox_big, (380, 50))
        else:
            win.blit(coinBox2_big, (380, 50))
       
    #Hit coin box
    def hit(self,win):
        ##Coin1
        if man.hitbox.colliderect(self.rect):
            if man.y <= (150):
                man.y = 150-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
                    man.kill = True
               
                
            elif man.y-28 >= (150-25):
                pygame.draw.rect(win,(0,0,0),self.rect)
                man.jumpCount = -7
                if self.coin == True:
                    bumpSound.play()
                else:
                    coinSound.play()
                
                if self.coin == False:
                    self.msg_coin += 1
                    self.msg_score += 200
                self.coin = True
                self.msg = "%02d"%self.msg_coin
                self.score = "%04d"%self.msg_score
            

        if self.coin == True:
            self.count_coin += 1
            if self.count_coin <= 5:
                win.blit(coin_big, (205, 130))
                
        ##Coin2:
        if man.hitbox.colliderect(self.rect_coin2):
            if man.y <= (150):
                man.y = 150-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
                    man.kill = True
                        
            elif man.y-28 >= (150-25):
                pygame.draw.rect(win,(0,0,0),self.rect_coin2)
                man.jumpCount = -7
                if self.coin2 == True:
                    bumpSound.play()
                else:
                    coinSound.play()
                    
                if self.coin2 == False:
                    self.msg_coin += 1
                    self.msg_score += 200
                self.coin2 = True
                self.msg = "%02d"%self.msg_coin
                self.score = "%04d"%self.msg_score                   

        if self.coin2 == True:
            self.count_coin2 += 1
            if self.count_coin2 <= 5:
                win.blit(coin_big, (385, 130))
               
                
        ##Coin3
        if man.hitbox.colliderect(self.rect_coin3):
            if man.y <= (50):
                man.y = 50-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
                    man.kill = True
                
                        
            elif man.y-28 >= (50-25):
                pygame.draw.rect(win,(0,0,0),self.rect_coin3)
                man.jumpCount = -7
                if self.coin3 == True:
                    bumpSound.play()
                else:
                    coinSound.play()

                 
                if self.coin3 == False:
                    self.msg_coin += 1
                    self.msg_score += 200
                self.coin3 = True
                self.msg = "%02d"%self.msg_coin
                self.score = "%04d"%self.msg_score                   

        if self.coin3 == True:
            self.count_coin3 += 1
            if self.count_coin3 <= 5:
                win.blit(coin_big, (385, 28))
                

        
        ##Brick1
        if man.hitbox.colliderect(self.rect_brick) and self.brick == True:
            if man.y <= (150):
                man.y = 150-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
                    man.kill = True
                
                    
            elif man.y-28 >= (150-25):
                man.jumpCount = -7
                bumpSound.play()
                self.brick = False
                self.msg_score += 100
                self.score = "%04d"%self.msg_score
                
        if self.brick == True:
            self.rect_drawBrick = pygame.draw.rect(win,(255,0,0),self.rect_brick)
            win.blit(Brick_big, (350, 152))
        
        ##Brick2
        if man.hitbox.colliderect(self.rect_brick2) and self.brick2 == True:
            if man.y <= (150):
                man.y = 150-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
                    man.kill = True
                
                    
            elif man.y-28 >= (150-25):
                man.jumpCount = -7
                bumpSound.play()
                self.brick2 = False
                self.msg_score += 100
                self.score = "%04d"%self.msg_score
                
        if self.brick2 == True:
            self.rect_drawBrick = pygame.draw.rect(win,(255,0,0),self.rect_brick2)
            win.blit(Brick_big, (410, 152))

    ##BigMushRoom    
    def coin_4(self,win):
        self.rect_coin4 = (100,150,20,25)
        
        if self.coin4 == False:
            win.blit(coinBox_big, (100, 150))
        else:        
            win.blit(coinBox2_big, (100, 150))
        win.blit(coin_big, (0, 0))

    def hit_BigMushroom(self,win):
        self.bool_Mushroom = False
        self.rect_MarioMushroom = (100,120,30,30)
        if man.hitbox.colliderect(self.rect_coin4):
            if man.y <= (150):
                man.y = 150-25
                man.jumpCount = 0
                
                if keys[pygame.K_SPACE]:
                    jumpSound.play()
                    man.jumpCount = 8
               
                
            elif man.y-28 >= (150-25):
                pygame.draw.rect(win,(0,0,0),self.rect_coin4)
                man.jumpCount = -7
                self.coin4 = True
                bumpSound.play()

                
                self.msg = "%02d"%self.msg_coin
                self.score = "%04d"%self.msg_score
            
        #Mushroom Pic
        if self.coin4 == True and self.MarioBig == False:
            win.blit(Mario_mushroomB, (100, 120))
            self.bool_Mushroom = True

        ##Mario Big   
        if man.hitbox.colliderect(self.rect_MarioMushroom) and self.MarioBig == False and self.bool_Mushroom == True:
            self.MarioBig = True
            self.bool_Mushroom = False
            man.big = True
            powerupSound.play()
            self.msg_score += 700
            self.score = "%04d"%self.msg_score
    
    ##Display coin message    
    def Coin_Message(self,win):
        screen_text = font.render(self.msg, True, (0,0,0))
        win.blit(screen_text,[20,3])

    #display score message   
    def Score_Message(self,win):
        screen_text_score = font.render(self.score, True, (0,0,0))
        win.blit(screen_text_score,[100,3])


#class enemy       
class enemy():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.walkCount = 0
        self.right = True
        self.left = False
        self.death = False
        self.kick = False
        self.count = 0

    #function hit box turtle
    def drawEnemy(self,win):
        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        if self.x <= 500 and self.right == True and self.death == False:
            self.x += self.vel
            win.blit(TurtleRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
            if self.x == 500:
                self.right = False
                self.left = True
                
            
        elif self.x >= 300 and self.left == True and self.death == False:
            self.x -= self.vel
            win.blit(TurtleLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            if self.x == 300:
                self.right = True
                self.left = False
        ##rect
        self.rect_turtle = (self.x,self.y,20,25)

    #function stomp on turtle
    def stomp(self,win,rect_mario):
        if rect_mario.colliderect(self.rect_turtle):
            if self.death == False and man.isJump == False:
                if man.big == True:
                    man.big = False
                    man.jumpCount = 8
                else:
                    man.death = True
            elif man.isJump == True:
                self.death = True
                stompSound.play()
                self.count += 1
                if self.count >1:
                    self.kick = True
            if man.isJump == True:
                man.jumpCount = 10
                box.msg_score += 500
                box.score = "%04d"%box.msg_score
            
        if self.death == True and self.x<600:
                win.blit(TurtleDeath,(self.x,self.y))
        
        if self.death == True and rect_mario.colliderect(self.rect_turtle) and man.isJump == False:
            self.kick = True
            kickSound.play()
            
        if self.kick == True:
                self.x+=20
            

                       
def redrawGameWindow():
    win.blit(bg,(0,0))
    if screen == 1:
        startScreen.draw(win)
        ButtonStart.draw(win,(0,0,0))
        ButtonQuit.draw(win,(0,0,0))
    elif screen == 2:
        man.draw(win)
        box.draw(win)
        box.hit(win)
        box.Coin_Message(win)
        box.Score_Message(win)
        turtle.drawEnemy(win)
        turtle.stomp(win,man.hitbox)
    elif screen == 3:
        man.draw(win)
        tube.draw(win)
        tube.hit(win)
        tube.flower(win)
        tube.Coin_Message(win)
        tube.Score_Message(win)
        Mush.drawEnemy(win)
        Mush.stomp(win)
        box.coin_4(win)
        box.hit_BigMushroom(win)
    elif screen == 4:
        man.draw(win)
        cloud.drawCloud(win)
        cloud.Coin_Message(win)
        cloud.Score_Message(win)
    elif screen == 5:
        man.draw(win)
        end.box(win)
        end.hit(win)
        end.flag(win)
        end.Coin_Message(win)
        end.Score_Message(win)
    elif screen == 6:
        score.Coin_Message(win)
        score.Score_Message(win)
        
        ButtonRestart.draw(win,(0,0,0))

    pygame.display.update()
    

#mainloop
man = player(50,300,20,30,walkLeft,walkRight,walkLeft_B,walkRight_B)
run = True
turtle = enemy(300,300,30,30)
box = Coin()
tube = Tube()
Mush = MushRoom(400,290,50,50)
cloud = Cloud(200,100,50,50)
end = End()
startScreen = Start(70,50)
score = Score(0,0)
pygame.mixer.music.play(-1)
ButtonStart = button((255,0,0),150,300,100,50,"Start")
ButtonQuit = button((0,255,0),300,300,100,50,"Exit")
ButtonRestart = button((255,0,0),250,250,100,50,"Restart")

while run:
    clock.tick(27)
    
    #gameloop
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.QUIT:
            run = False
            
        ##Mouse Event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen == 1 and ButtonStart.isOver(pos):
                screen = 2
            if screen == 1 and ButtonQuit.isOver(pos):
                run = False
            if screen == 6 and ButtonRestart.isOver(pos):
                score.StartOver()

    keys = pygame.key.get_pressed()

    #key input
    if keys[pygame.K_2]:
        man.death = True
        
    if keys[pygame.K_LEFT] and man.x > man.vel:
        if end.F == False:
            man.x -= man.vel
            man.left = True
            man.right = False
        

    elif keys[pygame.K_RIGHT]:
        if end.F == False:
            man.x += man.vel
            man.left = False
            man.right = True
            if man.x + 30 >= screenWidth:
                screen += 1
                man.x = 50

       
    else: 
        man.left = False
        man.right = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            jumpSound.play()
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
            man.kill = True
            
    else:
        
        if man.jumpCount >= -10:
            man.neg = 1
            if man.jumpCount < 0:
                man.neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * man.neg
            man.jumpCount -= 1
        else:
            if man.y>=300:
                man.y = 300
            man.isJump = False
            man.jumpCount = 10
            if tube.ontube == False:
                man.y = 300

    redrawGameWindow() 
    
    
pygame.quit()




    
    


    
