FILEPATH= "todos.txt"


def get_todo(filepath=FILEPATH):
    """open a file, read it and return a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg,filepath=FILEPATH):
    """open a file, write it and nothing return"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print('hello')
    print(get_todo())