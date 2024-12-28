import pygame
import os

# from action import MockAction
from game_components import Card, Stats, Table, Pot


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
        pygame.display.set_caption("PokerReplay")
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
        self.pot = Pot()
        self.pot.update_pot(self.main_surface)

        for seat in self.seat_dict.values():
            seat.draw_frame(self.main_surface)

        pygame.display.flip()

        running = True

        while running:

            # check for inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if action_index is None:
                            action_index = 0
                        else:
                            action_index += 1
                        try:
                            if self.hand_history[action_index] is not None:
                                self.hand_history[action_index].execute(parent=self)
                                print(self.hand_history[action_index])
                        except IndexError:
                            print("Reached the end of the round.")

                    if event.key == pygame.K_LEFT:
                        if action_index is None:
                            action_index = 0
                        elif action_index > 0:
                            action_index -= 1
                        try:
                            if self.hand_history[action_index] is not None:
                                self.hand_history[action_index].execute(parent=self)
                                print(self.hand_history[action_index])
                        except IndexError:
                            print("Reached the end of the round.")

                    pygame.display.flip()

            self.clock.tick(self.max_fps)

        pygame.quit()


if __name__ == "__main__":
    replay_viewer = ReplayViewer(hand_history=None)
    replay_viewer.run()
    replay_viewer.pre_load_card_images()
