import streamlit as st
from datetime import date

st.set_page_config(page_title="Task Demo", page_icon="📋", layout="centered")

if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"name": "Finish report", "due": "2026-03-25"},
        {"name": "Prepare slides", "due": "2026-03-27"},
    ]

st.title("Task Demo")
st.caption("Simple Streamlit demo app")

tab1, tab2, tab3 = st.tabs(["Dashboard", "Add Task", "My Tasks"])

with tab1:
    st.subheader("Dashboard")
    col1, col2 = st.columns(2)
    col1.metric("Tasks", len(st.session_state.tasks))
    col2.metric("Completed this week", 12)
    st.info("Upcoming reminder: Team meeting at 3:00 PM")

with tab2:
    st.subheader("Add Task")
    with st.form("task_form", clear_on_submit=True):
        task_name = st.text_input("Task name")
        task_due = st.date_input("Due date", value=date.today())
        submitted = st.form_submit_button("Save task", use_container_width=True)

    if submitted:
        if task_name:
            st.session_state.tasks.insert(0, {"name": task_name, "due": str(task_due)})
            st.success("Task added successfully.")
        else:
            st.error("Please enter a task name.")

with tab3:
    st.subheader("My Tasks")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks, start=1):
            with st.container(border=True):
                st.write(f"{i}. {task['name']}")
                st.caption(f"Due: {task['due']}")
    else:
        st.write("No tasks yet.")
