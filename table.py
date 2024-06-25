from player import Player


class Table:
    def __init__(self, total_seats:int, players: list[Player], table_stack:int|None) -> None:
        self.players = players
        self.table_stack = table_stack
        self.seats = [None for _ in range(total_seats)]

    def setup(self):
        self.find_hero()
        self.position_players()

    def find_hero(self):
         """
         Returns index of the hero in the players list.
         """
         for i, player in enumerate(self.players):
              if player.is_hero:
                   return i

    def position_players(self):
        """
        Creates the seats list and gets the position of the 
        dealer. Done in one function to avoid looping twice.
        """
        counter = 0
        player_count = len(self.players)
        i = self.find_hero()
        while counter < player_count:
             self.seats[counter] = self.players[i]
             if self.players[i].is_dealer:
                  self.dealer_position = i
             counter += 1
             if i == player_count - 1:
                  i = 0
             else: i += 1