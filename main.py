import pygame
import sys
from Block import *

pygame.init()

#Our screen is 7x12 blocks
screen = pygame.display.set_mode([525,900])
fpsClock = pygame.time.Clock()

BLUE = (5, 11, 77)
LIGHT_BLUE = (38, 222, 255)
GREEN = (91, 201, 100)

blocksMovingRight = True
gameIsRunning = True
movingBlockCount = 3
FPS = 10
playerWon = True

#Creating moving blocks sprite group and initialize for first 3 blocks
movingBlocks = pygame.sprite.Group()
startingXPosition = 150
for i in range(movingBlockCount):
    movingBlocks.add(Block(startingXPosition, 825))
    startingXPosition += 75

#Creating placed blocks sprite group for setting blocks when the player presses space
placedBlocks = pygame.sprite.Group()


def increaseDifficulty():
    global FPS
    FPS += 1  

def blockExistsBelow(blockToBePlaced):
    blockBelowX = blockToBePlaced.rect.x
    blockBelowY = blockToBePlaced.rect.y + 75
    if(blockBelowY > 825):
        return True
    for block in placedBlocks:
        if(blockBelowX == block.rect.x and blockBelowY == block.rect.y):
            return True
    return False

def checkIfGameOver():
    global movingBlocks, gameIsRunning, movingBlockCount, playerWon
    for block in movingBlocks:
        if(block.rect.y < 0):
            print("You Won!")
            gameIsRunning = False
            playerWon = True
    
    if(movingBlockCount <= 0):
        print ("You Lose!")
        playerWon = False
        gameIsRunning = False
        

def createNewMovingBlocks():
    global movingBlocks, movingBlockCount
    newYPosition = movingBlocks.sprites()[0].rect.y - 75
    #Wiping and creating new sprite group to clear movingBlocks
    movingBlocks = pygame.sprite.Group()
    #Creating new starting position for movingBlock train
    startingXPosition = 150
    for i in range(movingBlockCount):
        movingBlocks.add(Block(startingXPosition, newYPosition))
        startingXPosition += 75
    
    increaseDifficulty()

def placeBlocks():
    global placedBlocks, movingBlocks, movingBlockCount
    blocksSuccessfullyPlaced = 0
    for block in movingBlocks:
        if blockExistsBelow(block):
            placedBlocks.add(block)
            blocksSuccessfullyPlaced += 1
    movingBlockCount = blocksSuccessfullyPlaced
    createNewMovingBlocks()
    

def eventChecks():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
                raise SystemExit
            if(event.key == pygame.K_SPACE):
                placeBlocks()
            
def moveBlocks():
    global blocksMovingRight
    for block in movingBlocks:
        block.moveBlock(blocksMovingRight)
    checkIfGameOver()
    

def checkIfAnyBlocksOnEdge():
    global blocksMovingRight
    for block in movingBlocks:
        if(block.isAtEdge()):
            blocksMovingRight = not blocksMovingRight
            break

while gameIsRunning:
    eventChecks()
    screen.fill(BLUE)
    checkIfAnyBlocksOnEdge()
    moveBlocks()
    movingBlocks.draw(screen)
    placedBlocks.draw(screen)
    pygame.display.update()
    fpsClock.tick(FPS)

#At this point the main game loop as ended as the player as won or lost
font = pygame.font.Font('VT323-Regular.ttf', 125)

winText = font.render('You Win!', True, GREEN)
lostText = font.render('You Lose!', True, GREEN)
textRect = winText.get_rect()
textRect.x = 75
textRect.y = 200

def postGameEventChecks():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
                raise SystemExit
            
        
print("player won boolean set to " + str(playerWon))

while True:
    postGameEventChecks()
    if(playerWon):
        screen.blit(winText, textRect)
    else:
        screen.blit(lostText, textRect)
    pygame.display.update()
    