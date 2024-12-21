import pygame


class Stats:
    def __init__(self) -> None:
        self.width = 120
        self.height = 50
        self.color = (220, 220, 220)
        self.name_text = pygame.font.SysFont("Arial", 12)
        self.stack_text = pygame.font.SysFont("Arial", 12)

    def draw_rect(self, surface: pygame.Surface, position: tuple[int, int]) -> None:
        self.rect = pygame.Rect(position[0], position[1] + 90, self.width, self.height)
        pygame.draw.rect(surface, self.color, self.rect)

    def update_name(
        self, surface: pygame.Surface, position: tuple[int, int], content: str
    ) -> None:
        surface.blit(self.name_text.render(content, True, (255, 255, 255)), position)

    def update_stack(
        self, surface: pygame.Surface, position: tuple[int, int], content: str
    ) -> None:
        surface.blit(self.stack_text.render(content, True, (255, 255, 255)), position)


class Card:
    def __init__(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 90))

    def draw(self, surface: pygame.Surface, x: int, y: int) -> None:
        self.rect = self.image.get_rect(topleft=(x, y))
        surface.blit(self.image, self.rect)
        return

    def update(self) -> None:
        pass


class Button:
    def __init__(self, image_path) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (110, 110))

    def draw(self, surface: pygame.Surface, position: tuple[int, int]) -> None:
        self.rect = self.image.get_rect(topleft=(position[0], position[1]))
        surface.blit(self.image, self.rect)
        return
