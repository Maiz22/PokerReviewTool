

class Stage:
    def __init__(self, name:str, steps:list) -> None:
        self._name = name
        self.steps = steps

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        valid_names = {
            "PREPARATION", 
            "PREFLOP", 
            "FLOP",
            "TURN",
            "RIVER", 
            "SHOWDOWN", 
            "SUMMARY"
            }
        if name not in valid_names:
            raise ValueError("Invalid Stage Name.")
        self._name = name