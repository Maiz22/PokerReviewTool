from table import Table
from stage import Stage


class Round:
    def __init__(self, 
                 identifier:int=None, 
                 tournament:str=None,  
                 table:Table=None,
                 stages: list[Stage] = None) -> None: #limit:str=None,
        self.id = identifier
        self.tournament = tournament
        #self.limit = limit
        self.table = table
        self.stages = stages

    def __repr__(self):
        return f"Tournament: {self.tournament}\n Table: {self.table}\n" #Limit: {self.limit}\n
