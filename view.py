import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PokerReview")
        self.resizable(False, False)
        self.geometry("400x400")

        self.setup_frame = tk.Frame(self)
        self.setup_frame.pack(fill="both", expand=True, pady=10)
        self.path_button = tk.Button(self.setup_frame, text="Open handhistory")
        self.path_button.pack(side="left", padx=10)
        self.read_txt_button = tk.Button(self.setup_frame, text="Read")
        self.read_txt_button.pack(side="left", padx=10)

        self.text_frame = tk.Frame(self)
        self.text_frame.pack(fill="both", expand=True)
        self.text_field = tk.Text(self.text_frame)
        self.text_field.pack(fill="both", expand=True, pady=5, padx=5)

    def path_button_on_click(self, callback) -> None:
        self.path_button.bind("<Button-1>", callback)

    def read_button_on_click(self, callback) -> None:
        self.read_txt_button.bind("<Button->", callback)

    def open_txt_file(self) -> str:
        file_path = askopenfilename(filetypes=[("Text file", ".txt")])
        return file_path

        # self.canvas = tk.Canvas(self.main_frame, width=960, height=540)
        # self.canvas.pack(fill="both", expand=True)
        # self.image = Image.open("images/poker_table.jpg")
        # self.resized = self.image.resize((960, 540))
        # self.tk_image = ImageTk.PhotoImage(image=self.resized)
        # self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")
