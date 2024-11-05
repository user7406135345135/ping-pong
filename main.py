import pygame

win_width = 800 
win_height = 600

pygame.init()
window = pygame.display.set_mode((win_width, win_height))
background = pygame.transform.scale(pygame.image.load('background.jpg'), (win_width, win_height))
pygame.display.set_caption('Пинг-понг')


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, texture, width, height):
        super().__init__()
        self.texture = pygame.transform.scale(pygame.image.load(texture), (width, height))
        self.speed = speed
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.texture, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[pygame.K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_right(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


racket_1 = Player(0, 100, 10, 'racket.png', 50, 150)
racket_2 = Player(750, 100, 10, 'racket.png', 50, 150)
ball = GameSprite(350, 250, 100, 'ball.png', 60, 60)

pygame.font.init()

font1 = pygame.font.Font(None, 60)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))

font2 = pygame.font.Font(None, 60)
lose2 = font2.render('PLAYER 2 LOSE', True, (180, 0, 0))


speed_x = 3
speed_y = 3

clock = pygame.time.Clock()
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))
    racket_1.reset()
    racket_2.reset()
    racket_1.update_left()
    racket_2.update_right()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y <0:
        speed_y *= -1
    if pygame.sprite.collide_rect(racket_1, ball) or pygame.sprite.collide_rect(racket_2, ball):
        speed_x *= -1
    if ball.rect.x < -60:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 800:
        finish = True
        window.blit(lose2, (200, 200))

    pygame.display.update()
    clock.tick(40)