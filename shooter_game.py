from pygame import *
from random import randint
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

font.init()

lost = 0
max_lost = 25
score = 0
goal = 25

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ship(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()
            

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 


        if self.rect.y > win_height:
            self.rect.x = randint(-10, win_width - 8)
            self.rect.y = 1
            lost += 1


            
       
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()

ship = Ship('rocket.png',  65, 400, 50, 50, 5)
bullets = sprite.Group()
def shoot(self):
    all_sprites.add(bullet)
    bullets.add(bullet)
for i in range(1, 6):
    if key == K_SPACE:
        player.shoot()

monsters = sprite.Group()
for i in range(1, 19):
    monster = Enemy('ufo.png', randint(80, win_width-80), 90, 80, 60, randint(1, 1))
    monsters.add(monster)


sprites_list = sprite.spritecollide(
    ship, monsters, False
)

sprites_list = sprite.groupcollide(
    monsters, bullets, True, True
)


run = True
finish = False
FPS = 60
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))

        ship.update()
        ship.reset()
        
        monsters.update()
        monsters.draw(window)

        bullets.update()
        bullets.draw(window)
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            win.blit(win, (200, 200))

        if score >= goal:
            finish = Truewindow.blit(win, (200, 200))

        display.update ()
        clock.tick(90)

    
    

# Здесь можно добавить дополнительный код для отрисовки объектов в окне









