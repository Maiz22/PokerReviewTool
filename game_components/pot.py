from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from .card import Card


class Pot:
    def __init__(self) -> None:
        self.total_chips = 0
        self.coords = (380, 300)
        self.font = pygame.font.SysFont("Sans-Serif", 20)
        self.horizontal_space = 70

    def deal_flop(
        self, surface: pygame.Surface, cards: tuple[Card, Card, Card]
    ) -> None:
        x, y = self.coords
        for card in cards:
            card.draw(surface=surface, x=x, y=y)
            x += self.horizontal_space

    def deal_turn(self, surface: pygame.Surface, card: Card) -> None:
        x, y = self.coords
        card.draw(surface=surface, x=x + 3 * self.horizontal_space, y=y)

    def deal_river(self, surface: pygame.Surface, card: Card) -> None:
        x, y = self.coords
        card.draw(surface=surface, x=x + 4 * self.horizontal_space, y=y)

    def update_pot(self, surface: pygame.Surface, chips: float = None) -> None:
        x, y = self.coords
        if chips:
            self.total_chips += chips
        rect = pygame.Rect(x + 400, y, 80, 30)
        pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=3)
        surface.blit(
            self.font.render(f"{str(self.total_chips)}$", True, (0, 0, 0)),
            (x + 410, y + 8),
        )
