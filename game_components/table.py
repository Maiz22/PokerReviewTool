from .seat import Seat
from .config import TABLE_COORDS


class Table:
    def __init__(self, total_seats: int) -> None:
        self.total_seats = total_seats

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, value):
        if value not in [6, 8, 9]:
            raise ValueError("Invalid number of seats on a table")
        self._total_seats = value

    def create_seats(self) -> dict[int, Seat]:
        """
        Creates seat instances with coreesponding table coords and
        adds them to a dictionary with seat number as keys.
        Raises a KeyError if total number of seats is not supported.
        """
        try:
            return {
                i
                + 1: Seat(num=i + 1, card_coords=position[0], button_coords=position[1])
                for i, position in enumerate(TABLE_COORDS[self.total_seats])
            }
        except KeyError:
            print("Unaible to create table with {} seats".format(self.total_seats))

    def setup(self) -> None:
        positions = self.get_seat_positions()
        try:
            return {i + 1: position for i, position in enumerate(positions)}
        except IndexError:
            print("Too many players at the selected table")
