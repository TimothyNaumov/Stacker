import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        blockImage = pygame.image.load("images/BlockImage.png")
        self.image = blockImage
        self.rect = blockImage.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveBlock(self, shouldMoveRight):
        changeX = 75 if shouldMoveRight else -75
        self.rect.x += changeX
    
    def isAtEdge(self):
        return self.rect.x >= 450 or self.rect.x <= 0