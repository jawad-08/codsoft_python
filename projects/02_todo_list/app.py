import streamlit as st
st.set_page_config(page_title="To-Do List", layout="wide")
st._config.set_option("global.showDeployButton", False)

import pandas as pd
from src.todo import db, utils

# init database
db.init_db()

st.set_page_config(page_title="To-Do List", layout="wide")
st.title("📝 To-Do List App")

# Sidebar - Add task form
st.sidebar.header("➕ Add New Task")
with st.sidebar.form("task_form"):
    title = st.text_input("Title")
    description = st.text_area("Description")
    due_date = st.date_input("Due Date")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task")
    if submitted and title:
        utils.add_task(title, description, str(due_date), priority)
        st.sidebar.success("Task added!")

# Main area - Task table
st.subheader("📋 Your Tasks")
tasks = utils.get_tasks()
if tasks:
    df = pd.DataFrame(tasks, columns=["ID","Title","Description","Due Date","Priority","Status"])
    df.set_index("ID", inplace=True)
    st.dataframe(df, use_container_width=True)


    # Update/Delete section
    task_ids = [t[0] for t in tasks]
    selected = st.selectbox("Select Task ID", task_ids)
    col1, col2 = st.columns(2)
    with col1:
        new_status = st.selectbox("Update Status", ["Pending", "In Progress", "Done"])
        if st.button("Update"):
            utils.update_task_status(selected, new_status)
            st.success(f"Task {selected} updated!")
    with col2:
        if st.button("Delete"):
            utils.delete_task(selected)
            st.warning(f"Task {selected} deleted!")
else:
    st.info("No tasks yet. Add a task from the sidebar!")
