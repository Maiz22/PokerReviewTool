import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PokerReview")
        self.resizable(False, False)
        # self.geometry("400x400")

        self.setup_frame = tk.Frame(self)
        self.setup_frame.pack(fill="both", expand=True, pady=10)
        self.path_button = tk.Button(self.setup_frame, text="Open handhistory")
        self.path_button.pack(side="left", padx=10)
        self.round_label = tk.Label(self.setup_frame, text="Select Round:")
        self.round_label.pack(side="left", padx=10)
        self.round_number_var = tk.StringVar()
        self.round_number_dropdown = ttk.Combobox(
            self.setup_frame, state="readonly", textvariable=self.round_number_var
        )
        self.round_number_dropdown.pack(side="left", padx=10)
        self.action_label = tk.Label(self.setup_frame, text="Action:")
        self.action_label.pack(side="left", padx=10)
        self.prev_button = tk.Button(self.setup_frame, state="disabled", text="Prev")
        self.prev_button.pack(side="left", padx=5)
        self.next_button = tk.Button(self.setup_frame, state="disabled", text="Next")
        self.next_button.pack(side="left", padx=5)
        self.review_button = tk.Button(self.setup_frame, text="Review...")
        self.review_button.pack(side="left", padx=10)

        self.text_frame = tk.Frame(self)
        self.text_frame.pack(fill="both", expand=True)
        self.text_field = tk.Text(self.text_frame)
        self.text_field.pack(fill="both", expand=True, pady=5, padx=5)

    def path_button_on_click(self, callback) -> None:
        self.path_button.bind("<Button-1>", callback)

    def round_dropdown_on_change(self, callback) -> None:
        self.round_number_dropdown.bind("<<ComboboxSelected>>", callback)

    def next_action_button_on_click(self, callback) -> None:
        self.next_button.bind("<Button-1>", callback)

    def prev_action_button_on_click(self, callback) -> None:
        self.prev_button.bind("<Button-1>", callback)

    def review_button_on_click(self, callback) -> None:
        self.review_button.bind("<Button-1>", callback)

    def open_txt_file(self) -> str:
        file_path = askopenfilename(filetypes=[("Text file", ".txt")])
        return file_path
