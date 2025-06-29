import os, sys
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def find_value_file_path():

    if sys.platform.startswith("win"):
        base = os.getenv("LOCALAPPDATA") or os.getenv("APPDATA")
    elif sys.platform.startswith("darwin"):
        base = os.path.expanduser("~/Library/Application Support")
    else:
        base = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))

    money_value_path = os.path.join(base, "googol")

    if not os.path.isdir(money_value_path):
        os.makedirs(money_value_path)

    path = os.path.join(money_value_path, "money_value.txt")
    if not os.path.isfile(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("0")
    return path

def update_value_file(operation, argument):
    path = find_value_file_path()
    def wright_new_money_value(money_value):
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(money_value))
    with open(path, "r") as f:
        money_value = int(f.readline())
    if money_value < argument and operation == "-":#hier noch Bedingung kein Geld ausdenken
        return
    money_value = ops[operation](money_value,argument)
    wright_new_money_value(money_value)

def display_money_value():
    path = find_value_file_path()
    with open(path, "r") as f:
        money_value_show = f.readline()
    return money_value_show




#if __name__ == "__main__":
