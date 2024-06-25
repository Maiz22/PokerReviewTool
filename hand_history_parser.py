from abc import ABC, abstractmethod
from file_io import TxtFileHandler
from pprint import pprint


class HandHistoryParser(ABC):

    @abstractmethod
    def get_breakpoints(self) -> list:
        pass

    @abstractmethod
    def split(self) -> list:
        pass

class RoundParser(HandHistoryParser):
    def __init__(self, file_handler: TxtFileHandler) -> None:
        self.file_handler = file_handler

    def get_breakpoints(self) -> list:
        self.txt_file = self.file_handler.read_txt()
        breakpoints = []
        for i in range(len(self.txt_file)):
            if self.txt_file[i] == "\n" and self.txt_file[i-1] == "\n" and self.txt_file[i-2] == "\n":
                breakpoints.append(i)
        return breakpoints
    
    def split(self) -> list:
        rounds = []
        prev = 0
        for i in self.get_breakpoints():
            rounds.append(self.txt_file[prev:i-2])
            prev=i+1
        return rounds
    

if __name__ == "__main__":
    file_handler = TxtFileHandler(filename="HH20190916 T2694912632 No Limit Hold'em $3,16 + $0,34.txt", path=None)
    round_parser = RoundParser(file_handler=file_handler)
    list_of_rounds = round_parser.split()
    pprint(list_of_rounds)

    #breakpoints = {"*** HOLE CARDS ***", "*** FLOP ***", "*** TURN ***","*** RIVER ***", "*** SHOW DOWN ***", "*** SUMMARY ***"}