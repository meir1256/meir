from pygame import *
from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
#создай окно иг

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 680:
            self.rect.x += self.speed

class Enemy(GameSprite):
    side = 'left'  
    def update(self):
        if self.rect.x <= 470:
            self.side = 'right'
        if self.rect.x >= win_width - 85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()

        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        surface.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
surface = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

def set_sprite(value, pers):
    global filename_pers
    if value[0][0] == 'Синий':
        filename_pers = 'hero_png'
    elif value[0][0] == 'Зеленый':
        filename_pers = 'cyborg.png'
    

def start_the_game():
    global filename_pers

    game = True
    finish = False
    clock = time.Clock()
    FPS = 60

    w1 = Wall(145, 142, 13, 140, 70, 10,450)
    w2 = Wall(145, 142, 13, 100, 480, 350,10)
    w3 = Wall(145, 205, 13, 60, 10, 10,380)
    w4 = Wall(145, 142, 13, 210, 10, 10,350)
    w5 = Wall(145, 142, 13, 450, 130, 10,360)
    w6 = Wall(145, 142, 13, 300, 40, 10,350)
    w7 = Wall(145, 142, 13, 390, 120, 130,10)

    packman = Player('hero.png', 5, 50, 3)
    monster = Enemy('cyborg.png', win_width - 10, 200, 2)
    final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False

        if finish != True:       
            window.blit(background, (0, 0))
            packman.update()
            monster.update()

            packman.reset()
            monster.reset()
            final.reset()

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()
            w5.draw_wall()
            w6.draw_wall()
            w7.draw_wall()

            if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6) or sprite.collide_rect(packman, w7):
                finish = True
                window.blit(lose, (200, 200))
                kick.play()
                display.update()
                sleep(3)
                break
    
            if sprite.collide_rect(packman, final):
                finish = True
                window.blit(win, (200, 200))
                money.play()

        display.update()
        lock.tick(FPS)

def level_menu():
    mainmenu._open(level)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

mainmenu = pygame_menu.Menu('Maze', 700, 500, theme=themwa.THEME_SOLARIZED)
mainmenu.add.text_input('Name:' , default='username',maxchat=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Difficulty', 600, 400, theme=themes.THEME_BLUE    )
level.add.selector('Difficulty :', [('Синий', 1), ('Зеленый', 2)], onchange=set_sprite)    

mainmenu.mainloop(surface)
   



#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
text = font2.render('Счет: '+ str(score), 1, (255, 255, 255))
        window.blit(text, (10, 50))

        text_lose = font2.render('Пропущено: ' +str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))