import pygame

MOVING_IMAGE = "Tennis_Ball.png"
PINK = (255,20,148)

class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image.set_colorkey(PINK)
        self.__vx = 5
        self.__vy = 5

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_v(self,vx,vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x ,self.rect.y

    def get_v(self):
        return self.__vx, self.__vy