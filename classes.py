from setup import *

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, file_name, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(file_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < up - 100:
            self.rect.y += self.speed
    def move1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < up - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, x, y, file_name, speed, w, h):
        super().__init__(x, y, file_name, speed, w, h)
        self.is_outside = False
        spisok = (-1, 1)
        self.dirX = choice(spisok)
        self.dirY = choice(spisok)
    def auto_move(self):
        self.rect.x += self.speed * self.dirX
        self.rect.y += self.speed * self.dirY
        if self.rect.y < 0:
            self.dirY *= -1
        elif self.rect.y > up - self.h:
            self.dirY *= -1 
        if self.rect.x < 0 or self.rect.x > wid - self.w:
            self.is_outside = True
