import pygame 

class DialogBox:

    X_POSITION = 60
    Y_POSITION = 470

    def __init__(self):
        self.box = pygame.image.load('dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (700, 100))

    def render(self, screen):
        screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))