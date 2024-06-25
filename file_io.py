import os

class TxtFileHandler:
    """
    Class created for txt file interaction.
    """
    def __init__(self, filename:str, path:str) -> None:
        self.filename = filename
        self.path = path

    def read_txt(self) -> None|list:
        """
        Takes the path and filename reads it and returns a
        list of lines.
        """
        try:
            if self.path:
                with open(os.path.join(self.path, self.filename), "r", encoding='utf-8-sig') as txt:
                    return txt.readlines()
            with open(self.filename, "r", encoding='utf-8-sig') as txt:
                return txt.readlines()
        except FileNotFoundError:
            print(F"Error: {self.filename} not found.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return 