import streamlit as st
from streamlit import checkbox
import functions
todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("Improve your productivity")


for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo",placeholder="Add new todo",on_change=add_todo,key='new_todo')
st.session_state