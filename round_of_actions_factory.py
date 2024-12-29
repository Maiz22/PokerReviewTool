import os
from file_io import parse_txt_to_list
from action_registry import ActionRegistry
from action import *


def parse_list_to_rounds_of_actions(
    txt_list: list[str],
) -> tuple[list[list[BaseAction]], int, int, int, int]:
    """
    Loops through the list of raw lines (string) of the
    raw handhistory input. Parses each line and creates
    and instance of an Action using the
    ActionRegistry.get_action() method, that stores each
    Action and its regex pattern in a list. Actions are
    stored in single rounds which are added to the rounds
    list, once a single round is completed.
    Returns:
    rounds: BaseAction instances in lists of lists
    total_actions, total_known_actions, total_unknown_actions,
    unknown_lines: int values describing the parsing
    """
    total_actions, total_known_actions, total_unknown_actions = 0, 0, 0
    rounds, single_round = [], []

    # for debugging unknown actions
    unknown_lines = []

    linebreak_counter = 0
    for i, line in enumerate(txt_list):
        if line == "\n":
            if linebreak_counter == 2:
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
