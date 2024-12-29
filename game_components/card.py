import pygame


class Card:
    def __init__(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, surface: pygame.Surface, x: int, y: int) -> None:
        self.rect = self.image.get_rect(topleft=(x, y))
        surface.blit(self.image, self.rect)
        return

    def update(self) -> None:
        pass
