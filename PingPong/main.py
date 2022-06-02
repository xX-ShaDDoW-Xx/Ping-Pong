from pygame import *

run = True
fps = 60
lose = False
window = display.set_mode((900, 500))
background = transform.scale(image.load('background.png'), (900, 500))

clock = time.Clock()
platforms = sprite.Group()


game_font = 'arial'

font.init()
font1 = font.SysFont(game_font, 70)
if_lose = font1.render('GAME OVER', True, (213, 0, 8))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, speed2, width, height, up, down):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.speed = speed
        self.speed2 = speed2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.up = up
        self.down = down

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Platform(GameSprite):

    def update(self):

        keys = key.get_pressed()

        if keys[self.up] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[self.down] and (self.rect.y + self.height) <= 500:
            self.rect.y += self.speed


class Ball(GameSprite):

    def update(self):
        global lose

        
        if sprite.collide_rect(self, Platform1):
            self.speed *= -1
        if sprite.collide_rect(self, Platform2):
            self.speed *= -1
        if self.rect.y <= 0:
            self.speed2 *= -1
        if self.rect.y >= 470:
            self.speed2 *= -1


        if self.rect.x <= 0:
            lose = True
        if self.rect.x >= 870:
            lose = True


        self.rect.x += self.speed
        self.rect.y += self.speed2




Platform1 = Platform('platform.png', 20, 20, 3, None, 15, 100, K_w, K_s)
platforms.add(Platform1)

Platform2 = Platform('platform.png', 870, 20, 3, None, 15, 100, K_UP, K_DOWN)
platforms.add(Platform2)

balll = Ball('circle.png', 445, 245, 4, 4, 30, 30, None, None)


while run:

    if lose == False:

        window.blit(background, (0, 0))


        platforms.draw(window)
        platforms.update()

        balll.reset()
        balll.update()










    elif lose == True:
        window.blit(if_lose, (280, 150))




    for e in event.get():

        if e.type == QUIT:
             run = False

    clock.tick(fps)
    display.update()