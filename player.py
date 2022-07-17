import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, obstacle_sprites, image, pos, speed):
        super(Player, self).__init__(groups)
        self.animation = 0

        self.image_list = image
        self.image = self.image_list[self.animation]

        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites

        self.direction = pygame.math.Vector2()
        self.speed = speed

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.animation = 1
            self.direction.x = 1
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.animation = 2
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.animation = 3
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.animation = 0
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collision()
        self.rect.y += self.direction.y * self.speed
        self.vertical_collision()

    def horizontal_collision(self):
        for obstacle in self.obstacle_sprites:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = obstacle.rect.left
                if self.direction.x < 0:
                    self.rect.left = obstacle.rect.right

    def vertical_collision(self):
        for obstacle in self.obstacle_sprites:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = obstacle.rect.top
                if self.direction.y < 0:
                    self.rect.top = obstacle.rect.bottom

    def update(self):
        self.input()
        self.move()
        self.image = self.image_list[self.animation]
