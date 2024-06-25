import tkinter as tk
from PIL import ImageTk, Image


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PokerReview")
        self.resizable(False, False)
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)
        self.image = Image.open("images/poker_table.jpg")
        self.resized = self.image.resize((960, 540))
        self.tk_image = ImageTk.PhotoImage(image=self.resized)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")