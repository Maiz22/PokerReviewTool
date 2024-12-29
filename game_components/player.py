from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from .card import Card
    from .seat import Seat


class Player:
    """
    Player class created for drawing all player related
    components.
    """

    def __init__(
        self,
        name: str,
        seat: Seat = None,
        stack: float | None = None,
        cards: tuple[str, str] | None = None,
    ) -> None:
        self.name = name
        self.seat = seat
        self.stack = stack
        self.cards = cards
        self.font = pygame.font.SysFont("Sans-Serif", 20)

    def take_seat(self, seat_dict: dict, seat: int) -> None:
        """
        Method to assign a seat instance to a player. Takes a
        seat dict holding Seat instances as values an seat numbers
        as keys.
        """
        self.seat = seat_dict[seat]

    def draw_name(self, surface: pygame.Surface) -> None:
        """
        Draw the player name to the pygame surface by using the
        stat_coordinates provided by the corresponding seat
        instance.
        """
        x, y = self.seat.stat_coords
        surface.blit(self.font.render(self.name, True, (0, 0, 0)), (x + 5, y + 5))

    def update_stack(self, surface: pygame.Surface, difference: float = None) -> None:
        """
        Draw the players stack to the pygame sufaces. The total stack
        will be drawn unless a difference is passed as an argument.
        """
        x, y = self.seat.stat_coords[0], self.seat.stat_coords[1] + 22
        rect = pygame.Rect(x, y, 120, 26)
        pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=3)
        if difference:
            self.stack += difference
        surface.blit(
            self.font.render(f"{str(self.stack)}$", True, (0, 0, 0)), (x + 5, y + 5)
        )

    def draw_cards(
        self,
        surface: pygame.Surface,
        cards: tuple[Card, Card],
    ) -> None:
        """
        Draw players cards to the pygame surface. Taking Card
        instances and using the seats card coordinates to draw
        both cards.
        """
        x, y = self.seat.card_coords
        card1, card2 = cards
        card1.draw(surface=surface, x=x, y=y)
        card2.draw(surface=surface, x=x + 60, y=y)

    def __repr__(self) -> str:
        return "Name:{} Seat: {}".format(self.name, self.seat.num)
