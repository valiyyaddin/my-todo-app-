import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# Launch Header with Emoji and Styling
st.markdown("## 🚀 **Launch Your Day with Purpose**", unsafe_allow_html=True)
st.markdown("### **Your tasks, tracked and tackled.**", unsafe_allow_html=True)
st.markdown("On the way to success,one must do one thing a at a time")

st.divider()  # horizontal divider

# Show the todo items
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Add a new todo
st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=add_todo,
    key='new_todo'
)
