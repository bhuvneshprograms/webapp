import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.save_todos(todos)

todos = functions.load_list()

st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
st.write("Double tap on the ToDo to complete it!")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]

st.text_input(label="Enter a ToDo",placeholder="Add new ToDo....",
             on_change=add_todo,key='new_todo')

