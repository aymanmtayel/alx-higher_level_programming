#!/usr/bin/python3
"""append after module """


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: the file to be modified
        search_string: the char to add the new string after
        new_string: the string to be written
    """
    with open(filename, 'r', encoding="utf-8") as file:
        lista = []
        while True:
            lines = file.readline()
            if lines == "":
                break
            lista.append(lines)
            if search_string in lines:
                lista.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lista)
