import os
from file_io import parse_txt_to_list
from round_of_actions_factory import parse_list_to_rounds_of_actions


def test_open_txt_and_parse_to_round_of_actions_success() -> None:
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    input_dir = r"{}\input".format(parent_dir)
    filename = "HH20191006 T2702134214 No Limit Hold'em $9,80 + $1,20.txt"
    input_file = r"{}\{}".format(input_dir, filename)
    txt_list = parse_txt_to_list(path=input_file)
    (
        rounds,
        total_actions,
        total_known_actions,
        total_unknown_actions,
        unknown_lines,
    ) = parse_list_to_rounds_of_actions(txt_list=txt_list)
    assert total_unknown_actions >= 0
