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


racket_1 = Player(0, 100, 10, 'racket.png', 50, 250)
racket_2 = Player(750, 100, 10, 'racket.png', 50, 250)

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

    
    pygame.display.update()
    clock.tick(40)