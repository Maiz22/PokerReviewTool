import pygame
import os
from game_components.card import Card
from game_components.pot import Pot
from game_components.table import Table


class ReplayViewer:
    """
    Class representing the hand history replay viewer. Pygame
    is used to setup a poker table and replay a session round
    by round, action by action.
    """

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
        Pygame main loop to replay selected round of the hand history.
        """
        self.main_surface = pygame.display.set_mode(self.geometry)
        self.main_surface.blit(self.background_img, (0, 0))
        self.clock = pygame.time.Clock()

        total_seats = 9

        # create the basic table setup
        table = Table(total_seats=total_seats)
        self.seat_dict = table.create_seats()

        # create an empty pot
        self.pot = Pot()
        self.pot.update_pot(self.main_surface)

        # draw all seats
        for seat in self.seat_dict.values():
            seat.draw_frame(self.main_surface)

        # refresh pygame window
        pygame.display.flip()

        running = True
        action_index = None

        while running:

            # check for inputs
            for event in pygame.event.get():

                # quit pygame loop when window is closed
                if event.type == pygame.QUIT:
                    running = False

                # react to keydown event
                if event.type == pygame.KEYDOWN:

                    # on right arrow increment action index and execute action
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

                    # on left arror decrement action index and execute action
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

                    # refresh pygame window
                    pygame.display.flip()

            # set max fps
            self.clock.tick(self.max_fps)

        # quit pygame main loop
        pygame.quit()
