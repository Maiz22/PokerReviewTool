class Player:
    def __init__(self, 
                 name:str, 
                 stack:float, 
                 is_dealer:bool=False, 
                 is_hero: bool=False,
                 is_active:bool=False, 
                 is_eliminated:bool=False, 
                 in_hand:bool=False) -> None:
        self.name = name
        self.stack = stack
        self.is_dealer = is_dealer
        self.is_hero = is_hero
        self.is_active = is_active
        self.in_hand = in_hand
        self._is_eliminated = is_eliminated

    @property
    def is_eliminated(self):
        return self._is_eliminated

    @is_eliminated.setter
    def is_eliminated(self, state):
        self._is_eliminated = False
        if state is False:
            self.is_active = False