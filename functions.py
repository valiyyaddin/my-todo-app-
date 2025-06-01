FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local
def write_todos(todos_arg,filepath_arg=FILEPATH):
    with  open(filepath_arg, "w") as file_arg:
        file_arg.writelines(todos_arg)