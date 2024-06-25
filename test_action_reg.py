from file_io import TxtFileHandler
from hand_history_parser import RoundParser
from action_registry import ActionRegistry
from action import *
import os



if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
    file_handler = TxtFileHandler(filename="HH20191006 T2702134214 No Limit Hold'em $9,80 + $1,20.txt", path=f"{path}\input")
    round_parser = RoundParser(file_handler=file_handler)
    list_of_rounds = round_parser.split()
    with open("output.txt", "a") as file:
        for round in list_of_rounds:
            for line in round:
                file.write(ActionRegistry.get_action(line).__repr__() + "\n")
                print(ActionRegistry.get_action(line))
            