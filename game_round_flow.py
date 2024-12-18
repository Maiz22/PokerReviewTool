"""
Game Setup:
- Get total number of seats (typical 3, 6, 8, 9 at the beginning)
- setup talbe according to total num of seats
- every seat gets a position number


Round Setup
- Update Table:
    1) Set active players in seats:
        - seat them in correct position
        - update stack
    2) set button position
    3) check place ante:
        - post if necessary
        - update player stack
        - update pot
        - optional(summarize in one step)

"""


class Table:
    def __init__(self, total_seats: int) -> None:
        self.total_seats = total_seats
        self.seat_dict = {i: None for i in range(1, total_seats + 1)}

    def setup(self) -> None:
        """
        Should only be called once at the beginning of a game.
        Draws the seats on the table depending ont the total seat
        number.
        """

    def seat_player(self, seat_number: int, player) -> None:
        self.seat_dict[seat_number] = player


class Pot:
    def __init__(self, stack: float = 0.0) -> None:
        self.stack = stack

    def add_chips_to_stack(self, amount: float) -> None:
        self.stack += amount

    def remove_chips_from_stack(self, amount: float) -> None:
        if self.stack >= amount:
            self.stack -= amount
        else:
            raise ValueError("Not enough chips in the pot")


class Player:
    def __init__(
        self,
        name: str,
        stack: float,
        is_active: bool = True,
        cur_position: int | None = None,
    ) -> None:
        self.name = name
        self.is_active = is_active
        self.stack = stack
        self.cur_position = cur_position

    def add_chips_to_stack(self, amount: float) -> None:
        self.stack += amount

    def remove_chips_from_stack(self, amount: float) -> None:
        if self.stack >= amount:
            self.stack -= amount
        else:
            raise ValueError("Player does not have enough chips")

    # position may be stored in the table itself
