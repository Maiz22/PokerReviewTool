import pygame


class Button:
    def __init__(self, image_path) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (80, 80))

    def draw(self, surface: pygame.Surface, position: tuple[int, int]) -> None:
        self.rect = self.image.get_rect(topleft=(position[0], position[1]))
        surface.blit(self.image, self.rect)
        return
