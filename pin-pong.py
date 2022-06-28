from  pygame import *
from random import *
up = 600
wid = 1000
window = display.set_mode((wid, up))
display.set_caption('Пин-понг')
background = transform.scale(image.load('res/sky.png'), (wid, up))
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, file_name, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(file_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
        spisok = (-1, 1)
        self.dirX = choice(spisok)
        self.dirY = choice(spisok)
    def auto_move(self):
        self.rect.x += self.speed * self.dirX
        self.rect.y += self.speed * self.dirY
        if self.rect.y < 0:
            self.dirY *= -1
        elif self.rect.y > up - 30:
            self.dirY *= -1 

ball = Ball(int(wid/2), int(up/2), 'res/ball.png', 3, 30, 30)
rocket1 = Player(int(wid/10), int(up/2), 'res/right-rocket.png', 7, 120, 120)
rocket2 = Player(wid-(int(wid/7)), int(up/2), 'res/left-rocket.png', 7, 120, 120)
font.init()

clock = time.Clock()
game = True
finish = False 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        # if e.type == KEYDOWN:
        #     if e.key == K_SPACE:
        #         rocket.fire()
        #         kick.play()
           
    window.blit(background, (0, 0))
    ball.draw()
    rocket1.draw()
    rocket2.draw()
    if finish == False:
        # if sprite.collide_rect(rocket):
        #     kick.play()
        #     finish = True
        # if sprite.collide_rect(rocket):
        #     money.play()
        #     finish = True
        #     win = font.SysFont('Verdana', 100).render('YOU WIN!!!', True, (6, 246, 167))
        ball.auto_move()
        rocket2.move2()
        rocket1.move1()
    else:
        # window.blit(win, (int(wid/2-150), int(up/2-100)))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            finish = False

    display.update()
    clock.tick(120)