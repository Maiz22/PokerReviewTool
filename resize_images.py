from PIL import Image
import os


def resize_all(dest_dir: str, target_dir: str, width: int, height: int) -> None:
    for file in os.listdir(dest_dir):
        image = Image.open(os.path.join(dest_dir, file))
        image.resize((width, height)).save(os.path.join(target_dir, file))


def resize_one(dest_dir: str, target_dir: str, width: int, height: int) -> None:
    image = Image.open(dest_dir)
    file_name = dest_dir.split("/")[-1]
    image.resize((width, height)).save(os.path.join(target_dir, f"{file_name}_resized"))


if __name__ == "__main__":
    cur_dir = os.path.dirname(__file__)
    # dest_dir = os.path.join(cur_dir, "images_original/cards")
    # target_dir = os.path.join(cur_dir, "images/cards")
    # resize_all(dest_dir=dest_dir, target_dir=target_dir, width=60, height=90)
    dest_dir = os.path.join(cur_dir, "images/dealer.png")
    target_dir = os.path.join(cur_dir, "images")
    resize_one(dest_dir, target_dir, 80, 80)
