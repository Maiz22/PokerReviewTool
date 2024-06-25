from abc import ABC

class Game(ABC):
    def __init__(self, rounds:list, identifier:int=None, name:str=None) -> None:
        self.name = name
        self.identifier = identifier
        self.rounds = rounds

class Tournament(Game):
    def __init__(self, rounds:list, identifier:int, name:str) -> None:
        super().__init__(rounds, identifier, name)

class CashGame(Game):
    def __init__(self, rounds: list, identifier: int, name: str) -> None:
        super().__init__(rounds, identifier, name)