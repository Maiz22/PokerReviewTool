import pygame
from .button import Button


class Seat:
    def __init__(self, num: int, card_coords: tuple, button_coords: tuple) -> None:
        self.num = num
        self.card_coords = card_coords
        self.button_position = button_coords
        self.stat_coords = (card_coords[0], card_coords[1] + 90)
        self.width = 120
        self.height = 50

    def draw_frame(self, surface: pygame.Surface) -> None:
        self.rect = pygame.Rect(
            self.stat_coords[0], self.stat_coords[1], self.width, self.height
        )
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=5)

    def draw_dealer_button(self, surface: pygame.Surface) -> None:
        button = Button("images/dealer.png")
        button.draw(surface, self.button_position)
