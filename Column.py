import pygame


class UpperColumn(pygame.sprite.Sprite):

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, center - 150))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (1250, (center - 150) / 2)

    def update(self):
        self.rect.x -= 2




class LowerColumn(pygame.sprite.Sprite):

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 950 - center))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (1250, ((950  - center) / 2) + center)

    def update(self):
        self.rect.x -= 2