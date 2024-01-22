#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    i = 0
    count = 0
    while i < list_length:
        try:
            div.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            div.append(0)
            pass
        except (ZeroDivisionError):
            print("division by 0")
            div.append(0)
            pass
        except (IndexError):
            print("out of range")
            div.append(0)
            pass
        finally:
            i += 1
    return (div)
