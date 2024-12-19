import pygame


class Card(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, image_path: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self) -> None:
        pass
