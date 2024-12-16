from __future__ import annotations
from typing import TYPE_CHECKING
from round_of_actions_factory import parse_list_to_rounds_of_actions
from file_io import parse_txt_to_list

if TYPE_CHECKING:
    from view import View
    from model import Model


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.input_path = None
        self.all_rounds = []
        self.active_round = None
        self.round_number = 0
        self.view = view
        self.model = model
        self.init_view_buttons()

    def init_view_buttons(self) -> None:
        """
        Create controller functions to views bind events.
        """
        self.view.path_button_on_click(self.get_input_path)
        self.view.round_dropdown_on_change(self.select_round)
        self.view.prev_action_button_on_click(self.prev_action)
        self.view.next_action_button_on_click(self.next_action)

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

    def select_round(self, event=None) -> None:
        try:
            self.round_number = int(self.view.round_number_var.get())
            self.active_round = self.all_rounds[self.round_number]
            self.print_to_view("Selected Round {}".format(self.round_number))
            self.action_index = 0
            self.set_action_button_activation_state()
        except IndexError:
            print("Round {} not in all rounds.")

    def set_action_button_activation_state(self) -> None:
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
        if self.action_index < (len(self.active_round) - 1):
            self.action_index += 1
            self.set_action_button_activation_state()
            self.print_to_view(content=self.active_round[self.action_index])

    def prev_action(self, event) -> None:
        if self.action_index > 0:
            self.action_index -= 1
            self.set_action_button_activation_state()
            self.print_to_view(content=self.active_round[self.action_index])

    # def next_round(self) -> None:
    #    if self.round_number < len(self.all_rounds - 1):
    #        self.round_number += 1
    #    self.activate_round()
    #
    # def prev_round(self) -> None:
    #    if self.round_number > 0:
    #        self.round_number -= 1
    #    self.activate_round()

    def run(self) -> None:
        """
        Calls the views mainloop to start the gui.
        """
        self.view.mainloop()
