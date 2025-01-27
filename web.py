import streamlit as st
import todo_func

todos = todo_func.get_todo()
def add_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo)
    todo_func.write_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("Add in input box, select to remove")


for index, todo in enumerate(todos):
    serial = st.checkbox(todo, key=todo)
    if serial:
        todos.pop(index)
        todo_func.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="your input here", placeholder="Add a new todo", on_change=add_todo,
              key= 'new_todo')
