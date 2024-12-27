import pygame
from config import TABLE_COORDS


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


class Seat:
    def __init__(self, num: int, card_coords: tuple, button_coords: tuple) -> None:
        self.num = num
        self.card_coords = card_coords
        self.button_position = button_coords
        self.stat_coords = (card_coords[0], card_coords[1] + 90)
        self.width = 120
        self.height = 50
        # self.is_button = False

    def draw_frame(self, surface: pygame.Surface) -> None:
        self.rect = pygame.Rect(
            self.stat_coords[0], self.stat_coords[1], self.width, self.height
        )
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def draw_dealer_button(self, surface: pygame.Surface) -> None:
        button = Button("images/dealer.png")
        button.draw(surface, self.button_position)


class Player:
    def __init__(
        self,
        name: str,
        seat: Seat = None,
        stack: float | None = None,
        cards: tuple[str, str] | None = None,
        is_active: bool = False,
    ) -> None:
        self.name = name
        self.seat = seat
        self.stack = stack
        self.cards = cards
        self.font = pygame.font.SysFont("Arial", 16)

    def take_seat(self, seat_dict: dict, seat: int) -> None:
        """
        Method to assign a seat instance to a player to access
        the seats card coordinates.
        """
        self.seat = seat_dict[seat]

    def draw_name(self, surface: pygame.Surface) -> None:
        x, y = self.seat.stat_coords
        surface.blit(self.font.render(self.name, True, (255, 0, 0)), (x, y))

    def update_stack(self, surface: pygame.Surface, difference: float = None) -> None:
        x, y = self.seat.stat_coords[0], self.seat.stat_coords[1] + 20
        rect = pygame.Rect(x, y, 120, 30)
        pygame.draw.rect(surface, (255, 255, 255), rect)
        if difference:
            self.stack += difference
        surface.blit(self.font.render(str(self.stack), True, (0, 0, 0)), (x, y))

    def draw_cards(
        self,
        surface: pygame.Surface,
        cards: tuple[Card, Card],
    ) -> None:
        x, y = self.seat.card_coords
        card1, card2 = cards
        card1.draw(surface=surface, x=x, y=y)
        card2.draw(surface=surface, x=x + 60, y=y)

    def __repr__(self) -> str:
        return "Name:{} Stack: {} Seat: {}".format(self.name, self.stack, self.seat.num)


class Table:
    def __init__(self, total_seats: int) -> None:
        self.total_seats = total_seats

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, value):
        if value not in [6, 8, 9]:
            raise ValueError("Invalid number of seats on a table")
        self._total_seats = value

    def create_seats(self) -> dict[int, Seat]:
        """
        Creates seat instances with coreesponding table coords and
        adds them to a dictionary with seat number as keys.
        Raises a KeyError if total number of seats is not supported.
        """
        try:
            return {
                i
                + 1: Seat(num=i + 1, card_coords=position[0], button_coords=position[1])
                for i, position in enumerate(TABLE_COORDS[self.total_seats])
            }
        except KeyError:
            print("Unaible to create table with {} seats".format(self.total_seats))

    def setup(self) -> None:
        positions = self.get_seat_positions()
        try:
            return {i + 1: position for i, position in enumerate(positions)}
        except IndexError:
            print("Too many players at the selected table")


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
        x, y = position[0], position[1] + 90
        surface.blit(self.name_text.render(content, True, (255, 255, 255)), (x, y))

    def update_stack(
        self, surface: pygame.Surface, position: tuple[int, int], content: str
    ) -> None:
        x, y = position[0], position[1] + 90
        surface.blit(self.stack_text.render(content, True, (255, 255, 255)), (x, y))


class Pot:
    def __init__(self) -> None:
        self.total_chips = 0
        self.coords = (380, 300)
        self.font = pygame.font.SysFont("Arial", 16)
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
        rect = pygame.Rect(x + 400, y, 60, 30)
        pygame.draw.rect(surface, (255, 255, 255), rect)
        surface.blit(self.font.render(str(self.total_chips), True, (0, 0, 0)), (x, y))
