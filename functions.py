def show_list(todos):
    nooftodos = len(todos)
    for i in range(nooftodos):
        print(i + 1, ". ", todos[i])
""" Shows the new todos added"""

def load_list():
    todofileR = open('todos.txt', 'r')
    todos = todofileR.readlines()
    todofileR.close()
    return todos
"""Shows the old todos which can be read by user"""

def save_todos(todos):
    todofileW = open('todos.txt', 'w')
    todofileW.writelines(todos)
    todofileW.close()
    return