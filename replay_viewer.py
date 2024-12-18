import pygame


class ReplayViewer:
    def __init__(self) -> None:
        self.geometry = (1280, 720)
        self.max_fps = 60

    def run(self) -> None:
        """
        Start the pygame event loop.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.geometry)
        self.clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(self.max_fps)
        pygame.quit()


if __name__ == "__main__":
    replay_viewer = ReplayViewer()
    replay_viewer.run()
