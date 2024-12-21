import pygame
import os

# from action import MockAction
from game_components import Card, Stats, Button


"""
Determine total num of seats
Create Seat -> give it coords at creation
Create Player -> give it a seat
add player to review tools dict of players
through player change things
"""


class Player:
    def __init__(
        self,
        name: str,
        stack: float | None = None,
        cards: tuple[str, str] | None = None,
        is_active: bool = False,
    ) -> None:
        self.name = name
        self.seat = None
        self.stack = stack
        self.cards = cards
        self.is_active = is_active

    def take_seat(self, seat_dict: dict, seat: int) -> None:
        """
        Method to assign a seat instance to a player to access
        the seats card coordinates.
        """
        self.seat = seat_dict[seat]

    def update_stack(self) -> None:
        pass

    def __repr__(self) -> str:
        return "Name:{} Stack: {} Seat: {}".format(self.name, self.stack, self.seat.num)


class Seat:
    def __init__(self, num: int, card_coords: tuple, button_coords: tuple) -> None:
        self.num = num
        self.cards_coords = card_coords
        self.button_position = button_coords
        # self.is_button = False

    def draw_dealer_button(self, surface: pygame.Surface) -> None:
        button = Button("images/dealer.png")
        button.draw(surface, self.button_position)

    def draw_cards(self, surface: pygame.Surface, cards: tuple[str, str]) -> None:
        pass


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

    def get_seat_positions(self) -> list[tuple[int, int]]:
        if self.total_seats == 6:
            return [
                [(40, 325), (185, 305)],
                [(380, 40), (385, 160)],
                [(780, 40), (785, 160)],
                [(1120, 325), (968, 305)],
                [(380, 570), (385, 450)],
                [(780, 570), (785, 450)],
            ]
        elif self.total_seats == 8:
            return [
                [(40, 325), (185, 305)],
                [(280, 40), (285, 160)],
                [(580, 40), (585, 160)],
                [(880, 40), (885, 160)],
                [(1120, 325), (968, 305)],
                [(280, 570), (285, 450)],
                [(580, 570), (585, 450)],
                [(880, 570), (885, 450)],
            ]
        elif self.total_seats == 9:
            return [
                [(40, 325), (185, 305)],
                [(270, 45), (275, 170)],
                [(480, 40), (485, 160)],
                [(680, 40), (685, 160)],
                [(890, 45), (895, 170)],
                [(1120, 325), (968, 305)],
                [(280, 570), (285, 450)],
                [(580, 570), (585, 450)],
                [(880, 570), (885, 450)],
            ]
        else:
            raise ValueError("Invalid number of seats")

    def setup(self) -> None:
        positions = self.get_seat_positions()
        try:
            return {i + 1: position for i, position in enumerate(positions)}
        except IndexError:
            print("Too many players at the selected table")


class ReplayViewer:
    def __init__(self, hand_history: list) -> None:
        pygame.init()
        self.hand_history = hand_history
        self.geometry = (1280, 720)
        self.max_fps = 60
        self.background_img = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "images\poker_table_bg.jpg")
        )
        self.background_img = pygame.transform.scale(self.background_img, self.geometry)
        self.card_images = self.pre_load_card_images()
        self.player_dict = {}

        print(len(self.card_images))

    # def get_table_positions(total_players: int) -> None:
    #    if total_players == 6:
    #        return [
    #            (40, 325),
    #            (380, 60),
    #            (780, 60),
    #            (380, 570),
    #            (780, 570),
    #            (1120, 325),
    #        ]

    # for testing
    def setup_table(num_player: int = 6) -> None:
        pass

    def pre_load_card_images(self) -> dict[str:Card]:
        cards_dir = os.path.join(os.path.dirname(__file__), "images\cards")
        cards_dict = {
            card.split(".")[0]: Card(os.path.join(cards_dir, card))
            for card in os.listdir(cards_dir)
        }
        return cards_dict

    def create_seats(self, positions: list) -> list[Seat]:
        seat_dict = {
            i + 1: Seat(num=i + 1, card_coords=position[0], button_coords=position[1])
            for i, position in enumerate(positions)
        }
        return seat_dict
        # seat = Seat(card_coords=position[0], button_coords=position[1])

    def draw_hand(
        self,
        position: tuple[int],
        cards: tuple[str],
        screen: pygame.Surface,
    ) -> None:
        card_width, card_height = 60, 90
        # card1 = Card(
        #    x=position[0], y=position[1], image_path="images/{}".format(cards[0])
        # )
        # card2 = Card(
        #    x=position[0] + card_width,
        #    y=position[1],
        #    image_path="images/{}".format(cards[0]),
        # )
        # cards = pygame.sprite.Group()
        # cards.add(card1, card2)
        # card1.update()
        # card2.update()
        # cards.draw(screen, position)
        # print(position)
        # b = Button("images/dealer.png")
        # b.draw(screen, (position[1][0], position[1][1]))
        card1 = self.card_images["as"]
        card2 = self.card_images["2s"]
        card1.draw(screen, x=position[0][0], y=position[0][1])
        card2.draw(screen, x=position[0][0] + 60, y=position[0][1])
        stats = Stats()
        stats.draw(screen, position[0])

    def run(self) -> None:
        """
        Start the pygame event loop.
        """
        self.main_surface = pygame.display.set_mode(self.geometry)
        self.main_surface.blit(self.background_img, (0, 0))
        pygame.display.flip()

        self.clock = pygame.time.Clock()

        # list of
        # list_of_actions = [MockAction() for _ in range(10)]
        print(self.hand_history)
        list_of_actions = [i for i in range(10)]
        action_index = None

        # setupt table
        # total_seats = get_total_seats()
        total_seats = 9
        table = Table(total_seats=total_seats)
        positions = table.get_seat_positions()
        self.seat_dict = self.create_seats(positions)
        # seats["seat2"].draw_dealer_button(self.main_surface)
        # table_dict = table.setup()

        # for seat in positions:
        #    # print(seat)
        #    self.draw_hand(
        #        seat,
        #        ("card-back_final.png", "card-back_final.png"),
        #        screen=self.main_surface,
        #    )
        pygame.display.flip()

        running = True

        while running:

            # check for inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print("key right")
                        if action_index is None:
                            action_index = 0
                        # elif action_index < (len(list_of_actions) - 1):
                        else:
                            action_index += 1
                        self.hand_history[action_index].execute(parent=self)
                        print(action_index)

                    if event.key == pygame.K_LEFT:
                        print("key left")
                        if action_index is None:
                            action_index = 0
                        # elif action_index > 0:
                        #    action_index -= 1
                        self.hand_history[action_index].execute()
                        print(action_index)

                    pygame.display.flip()
            #            seats = [
            #                (40, 325),
            #                (380, 40),
            #                (780, 40),
            #                (380, 570),
            #                (780, 570),
            #                (1120, 325),
            #            ]

            # self.main_surface.blit(self.background_img, (0, 0))
            self.clock.tick(self.max_fps)

        pygame.quit()


if __name__ == "__main__":
    replay_viewer = ReplayViewer(hand_history=None)
    replay_viewer.run()
    replay_viewer.pre_load_card_images()
