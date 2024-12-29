from __future__ import annotations
from typing import TYPE_CHECKING
from round_of_actions_factory import parse_list_to_rounds_of_actions
from file_io import parse_txt_to_list
from replay_viewer import ReplayViewer

if TYPE_CHECKING:
    from view import View
    from model import Model


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.input_path = None
        self.all_rounds = []
        self.active_round = None
        self.action_index = None
        self.round_number = 0
        self.view = view
        self.model = model
        self.init_view_buttons()
        self.replay_viewer = None

    def init_view_buttons(self) -> None:
        """
        Create controller functions to views bind events.
        """
        self.view.path_button_on_click(self.get_input_path)
        self.view.round_dropdown_on_change(self.select_round)
        self.view.prev_action_button_on_click(self.prev_action)
        self.view.next_action_button_on_click(self.next_action)
        self.view.review_button_on_click(self.review_hand_history)

    def get_input_path(self, event) -> None:
        """
        Open a txt file through the views function and pass it
        to self.input_path.
        By returning 'break' the button event will be reset.
        """
        self.input_path = self.view.open_txt_file()
        self.process_input_file(event=None)
        return "break"

    def parse_input_file(self) -> None:
        """
        Opens the .txt file, and creates a list of lines of the
        text file. The txt_list passed to the returned
        parse_list_to_rounds_of_actions functions.
        """
        txt_list = parse_txt_to_list(path=self.input_path)
        return parse_list_to_rounds_of_actions(txt_list=txt_list)

    def process_input_file(self, event) -> None:
        """
        Processes the input file by parsing it, printing a
        summary to the views textfield.
        Returns 'break' to reset the views button.
        """
        if self.input_path:
            (
                self.all_rounds,
                total_actions,
                total_known_actions,
                total_unknown_actions,
                unknown_lines,
            ) = self.parse_input_file()
            self.print_to_view(
                self.create_summary(
                    total_actions, total_known_actions, total_unknown_actions
                )
            )
            self.view.round_number_dropdown.configure(
                values=[str(num) for num in range(1, len(self.all_rounds) + 1)]
            )
            self.print_to_view(
                content="Opened file:\n{}".format(self.input_path.split(r"/")[-1])
            )
            self.view.round_number_var.set("1")
            self.select_round()
        else:
            self.view.round_number_dropdown.configure(values=[])
            self.view.round_number_var.set("")
        print(self.all_rounds)
        return "break"

    def create_summary(
        self, total_actions: str, total_known_actions: str, total_unknown_actions: str
    ) -> str:
        """
        Creates a summary as a string with parsing statistics.
        """
        return "--------------------\nTotal Actions: {}\nKnown_actions: {}\nUnknown Actions: {}\n--------------------".format(
            total_actions, total_known_actions, total_unknown_actions
        )

    def print_to_view(self, content: str) -> None:
        """
        Takes a string as content, inserts it to the views
        textfield and scrolls down to the buttom of it.
        """
        self.view.text_field.insert("end", "{}\n".format(content))
        self.view.text_field.see("end")

    def del_text_from_view(self) -> None:
        """
        Delete the last line from the text field.
        """
        self.view.text_field.delete("end-2l", "end-1l")

    def select_round(self, event=None) -> None:
        """ """
        try:
            self.round_number = int(self.view.round_number_var.get()) - 1
            self.active_round = self.all_rounds[self.round_number]
            self.print_to_view("Selected Round {}".format(self.round_number + 1))
            self.action_index = 0
            self.set_action_button_activation_state()
        except IndexError:
            print("Round {} not in all rounds.")

    def set_action_button_activation_state(self) -> None:
        """
        Set the activation state of the next and previous button
        depending on the active round we are in.
        """
        if self.action_index == (len(self.active_round) - 1):
            self.view.next_button.configure(state="disabled")
            self.view.prev_button.configure(state="normal")
            return
        if self.action_index == 0:
            self.view.prev_button.configure(state="disabled")
            self.view.next_button.configure(state="normal")
            return
        self.view.prev_button.configure(state="normal")
        self.view.next_button.configure(state="normal")
        return

    def next_action(self, event) -> None:
        """
        Prints the next action to the views textfield.
        """
        if not self.action_index is None and self.action_index < (
            len(self.active_round) - 1
        ):
            self.action_index += 1
            self.set_action_button_activation_state()
            self.print_to_view(
                content="{} - {}".format(
                    type(self.active_round[self.action_index]),
                    self.active_round[self.action_index],
                )
            )

    def prev_action(self, event) -> None:
        """
        Removes the last action from the views textfield.
        """
        if not self.action_index is None and self.action_index > 0:
            self.action_index -= 1
            self.set_action_button_activation_state()
            self.del_text_from_view()

    def review_hand_history(self, event) -> None:
        """
        Opens the Replay viewer of the currently selected round:
        self.active round.
        """
        if not self.active_round:
            self.print_to_view(content="Please select a round first")
        elif self.replay_viewer is not None:
            self.print_to_view(content="Review player already running")
        else:
            self.replay_viewer = ReplayViewer(hand_history=self.active_round)
            self.replay_viewer.run()
            self.replay_viewer = None
        return "break"

    def run(self) -> None:
        """
        Calls the views mainloop to start the gui.
        """
        self.view.mainloop()
