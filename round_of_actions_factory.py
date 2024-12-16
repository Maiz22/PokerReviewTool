from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from action import BaseAction

from file_io import parse_txt_to_list

# from hand_history_parser import RoundParser
from action_registry import ActionRegistry
from action import *
import os


def parse_list_to_rounds_of_actions(txt_list: list[str]):
    total_actions, total_known_actions, total_unknown_actions = 0, 0, 0
    rounds, single_round = [], []

    # for debugging unknown actions
    unknown_lines = []

    linebreak_counter = 0
    for i, line in enumerate(txt_list):
        if line == "\n":
            if linebreak_counter == 3:
                rounds.append(single_round)
                single_round = []
                linebreak_counter = 0
            else:
                linebreak_counter += 1
        else:
            action = ActionRegistry.get_action(line)
            single_round.append(action)
            if action:
                total_known_actions += 1
            else:
                total_unknown_actions += 1
                unknown_lines.append(i)
        total_actions += 1

    return (
        rounds,
        total_actions,
        total_known_actions,
        total_unknown_actions,
        unknown_lines,
    )


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    dir = f"{path}/input"
    filename = "HH20191006 T2702134214 No Limit Hold'em $9,80 + $1,20.txt"
    txt_list = parse_txt_to_list(filename=filename, dir=dir)

    (
        rounds,
        total_actions,
        total_known_actions,
        total_unknown_actions,
        unknown_lines,
    ) = parse_list_to_rounds_of_actions(txt_list=txt_list)

    for round in rounds:
        print(round)
