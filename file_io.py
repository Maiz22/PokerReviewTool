def parse_txt_to_list(path: str) -> list[str]:
    """
    Takes a txt file and directory, opens the file and returns
    a all lines in a list of strings.
    """
    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File {} not foun in {}.".format(path, dir))
    except Exception as err:
        print(err)


def write_output_txt() -> None:
    pass
