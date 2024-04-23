import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load player image
        original_image = pygame.image.load("bird_icon.png")

        # Resize the image to desired dimensions
        self.image = pygame.transform.scale(original_image, (30, 30))
        self.rect = self.image.get_rect()  # Get the Rect object from the image
        self.rect.center = (320, 240)

        # X and Y velocity
        self.velocity = -15

    def update(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = -10
