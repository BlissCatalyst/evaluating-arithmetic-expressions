string1 = "[+, 23, -8, -67]"   # == -52
string2 = "[-, 89, 5, -9, 16]"  # == 77
string3 = "[x, 23, 22, -1, 0]"  # == 0
string4 = "[+, [-, 1, 4], [+, 98, 3, -56], [x, 1, 6, 15]]"  # == 2112


def make_list(string):
    new_list = list()
    open_lists = 0
    for char in string:
        if char == = "[":
            open_lists += 1
            if not new_list:
                pass


def eval_string(string):
    pass
