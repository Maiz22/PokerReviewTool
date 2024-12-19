import pygame
import os
from action import MockAction


class Player:
    def __init__(self, name, stack) -> None:
        self.name = name
        self.stack = stack


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
                (40, 325),
                (380, 60),
                (780, 60),
                (380, 570),
                (780, 570),
                (1120, 325),
            ]
        elif self.total_seats == 8:
            pass
        elif self.total_seats == 9:
            pass
        else:
            raise ValueError("Invalid number of seats")

    def setup(self) -> None:
        positions = self.get_seat_positions()
        try:
            return {i + 1: position for i, position in enumerate(positions)}
        except IndexError:
            print("Too many players at the selected table")


class Seat:
    def __init__(self, player, position) -> None:
        self.player = player

    def draw(self) -> None:
        pass

    def update(self) -> None:
        pass


class Stats(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.width = 120
        self.height = 50
        self.color = (220, 220, 220)

    def draw(self, surface: pygame.Surface, x: int, y: int) -> None:
        self.rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(surface, self.color, self.rect)


class Card(pygame.sprite.Sprite):
    def __init__(self, image_path: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 90))

    def draw(self, surface: pygame.Surface, image, position: tuple[int, int]) -> None:
        self.rect = self.image.get_rect(topleft=position)
        surface.blit(image, position)
        return

    def update(self) -> None:
        pass


class ReplayViewer:
    def __init__(self, hand_history) -> None:
        pygame.init()
        self.hand_history = hand_history
        self.geometry = (1280, 720)
        self.max_fps = 60
        self.background_img = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "images\poker_table_bg.jpg")
        )
        self.background_img = pygame.transform.scale(self.background_img, self.geometry)
        self.card_images = self.pre_load_card_images()

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

    def pre_load_card_images(self) -> None:
        cards_dir = os.path.join(os.path.dirname(__file__), "images\cards")
        cards_dict = {
            card.split(".")[0]: os.path.join(cards_dir, card)
            for card in os.listdir(cards_dir)
        }
        return cards_dict

    def draw_hand(
        self,
        position: tuple[int],
        cards: tuple[str],
        screen: pygame.Surface,
    ) -> None:
        card_width, card_height = 60, 90
        card1 = Card(
            x=position[0], y=position[1], image_path="images/{}".format(cards[0])
        )
        card2 = Card(
            x=position[0] + card_width,
            y=position[1],
            image_path="images/{}".format(cards[0]),
        )
        cards = pygame.sprite.Group()
        cards.add(card1, card2)
        card1.update()
        card2.update()
        cards.draw(screen, position)
        stats = Stats()
        stats.draw(screen, position[0], position[1] + 90)
        pygame.display.flip()

    def run(self) -> None:
        """
        Start the pygame event loop.
        """
        self.main_surface = pygame.display.set_mode(self.geometry)
        self.main_surface.blit(self.background_img, (0, 0))
        pygame.display.flip()
        self.clock = pygame.time.Clock()

        # list of
        list_of_actions = [MockAction() for _ in range(10)]
        action_index = 0
        prev_index = None

        # total_seats = get_total_seats()
        total_seats = 6
        table = Table(total_seats=total_seats)
        table_dict = table.setup()

        running = True

        while running:

            if not prev_index == action_index:
                print(action_index)
            prev_index = action_index

            # check for inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        list_of_actions[action_index].execute()
                        print("key right")
                        if action_index < (len(list_of_actions) - 1):
                            action_index += 1
                    if event.key == pygame.K_LEFT:
                        list_of_actions[action_index].execute()
                        print("key left")
                        if action_index > 0:
                            action_index -= 1

            # seats = [
            #    (40, 325),
            #    (380, 60),
            #    (780, 60),
            #    (380, 570),
            #    (780, 570),
            #   (1120, 325),
            # ]
            # for seat in seats:
            #    self.draw_hand(
            #        seat,
            #       ("card-back_final.png", "card-back_final.png"),
            #        screen=self.main_surface,
            #   )

            self.main_surface.blit(self.background_img, (0, 0))
            self.clock.tick(self.max_fps)

        pygame.quit()


if __name__ == "__main__":
    replay_viewer = ReplayViewer(hand_history=None)
    replay_viewer.run()
    replay_viewer.pre_load_card_images()
