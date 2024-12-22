import pygame
import os

# from action import MockAction
from game_components import Card, Stats, Table


"""
Determine total num of seats
Create Seat -> give it coords at creation
Create Player -> give it a seat
add player to review tools dict of players
through player change things
"""


class ReplayViewer:
    def __init__(self, hand_history: list) -> None:
        pygame.init()
        self.geometry = (1280, 720)
        self.max_fps = 60
        self.background_img = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "images\poker_table_bg.jpg")
        )
        self.background_img = pygame.transform.scale(self.background_img, self.geometry)
        self.card_images = self.pre_load_card_images()
        self.hand_history = hand_history
        self.seat_dict = {}
        self.player_dict = {}

    def pre_load_card_images(self) -> dict[str:Card]:
        """
        Open images from images\cards directory and create a dictionary
        containing of card short strings as keys and Card instances
        as values.
        """
        cards_dir = os.path.join(os.path.dirname(__file__), "images\cards")
        cards_dict = {
            card.split(".")[0]: Card(os.path.join(cards_dir, card))
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
        print(self.hand_history)

        self.main_surface = pygame.display.set_mode(self.geometry)
        self.main_surface.blit(self.background_img, (0, 0))
        pygame.display.flip()
        self.clock = pygame.time.Clock()

        list_of_actions = [i for i in range(len(self.hand_history))]
        action_index = None

        # setupt table
        # total_seats = get_total_seats()

        total_seats = 9
        table = Table(total_seats=total_seats)
        self.seat_dict = table.create_seats()

        for seat in self.seat_dict.values():
            seat.draw_frame(self.main_surface)

        pygame.display.flip()

        # table_dict = table.setup()

        # for key, val in self.seat_dict:

        # for seat in positions:
        #    # print(seat)
        #    self.draw_hand(
        #        seat,
        #        ("card-back_final.png", "card-back_final.png"),
        #        screen=self.main_surface,
        #    )

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

            self.clock.tick(self.max_fps)

        pygame.quit()


if __name__ == "__main__":
    replay_viewer = ReplayViewer(hand_history=None)
    replay_viewer.run()
    replay_viewer.pre_load_card_images()
