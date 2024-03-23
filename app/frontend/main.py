from select import select
import streamlit as st
import pandas as pd
from PIL import Image
import requests
import json

# FastAPI endpoints
backend = "http://backend:8088/"

st.set_page_config(
    page_title="Task Catalog",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

top_image = Image.open('static/banner_top.gif')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

st.image(main_image, use_column_width='always')
st.title("📄 Your Task Catalog 🗣")

st.sidebar.image(top_image, use_column_width='auto')
choice = st.sidebar.selectbox("Menu", ["Create Task ✅", "Update Task 👨‍💻", "Delete Task ❌"])
st.sidebar.image(bottom_image, use_column_width='auto')

myCatalog = st.table(data=None)

if choice == "Create Task ✅":
    st.subheader("Add Item")
    col1, col2 = st.columns(2)

    with col1:
        task = st.text_area("Task To Do")

    with col2:
        task_status = st.selectbox("Status", ["Pending", "In Progress", "Done"])
        task_due_date = st.date_input("Due Date")

    if st.button("Add Task"):
        add_data = {
            'title': task,
            "due_date": task_due_date.strftime('%d/%m/%Y'),
            "description": str(task_status)
        }
        if task == "":
            st.error("Can't be empty Task Name! ❌")
        else:
            requests.post(f'{backend}catalog/', json=add_data)
            st.success("Added Task \"{}\" ✅".format(task))
            st.balloons()

    response = requests.get(f"{backend}catalog/").json()

    df = pd.DataFrame.from_dict(data=response)
    if len(df):
        df.columns = ["Task", "Due Date", "Status"]
    myCatalog.table(df)


elif choice == "Update Task 👨‍💻":
    st.subheader("Edit Items")

    response = requests.get(f"{backend}catalog/").json()
    df = pd.DataFrame.from_dict(data=response)
    if len(df):
        df.columns = ["Task", "Due Date", "Status"]
    myCatalog.table(df)

    list_of_jsons = requests.get(f"{backend}catalog/").json()
    list_of_tasks = [dict["title"] for dict in list_of_jsons]
    selected_task = st.selectbox("Task", list_of_tasks)
    task_result = requests.get(f"{backend}catalog/{str(selected_task)}").json()
    if selected_task and len(list_of_tasks) > 0:
        new_task_status = st.selectbox('New Task Status:', ["Pending", "In Progress", "Done"])
        new_task_due_date = st.date_input('New Due Date:')

        if st.button("Update Task 👨‍💻"):
            update_data = {
                'title': str(selected_task),
                'description': str(new_task_status),
                'due_date': new_task_due_date.strftime('%d/%m/%Y')
            }

            requests.put(f'{backend}catalog/{str(selected_task)}', json=update_data)
            response = requests.get(f"{backend}catalog/").json()
            st.success("Updated Task \"{}\" ✅".format(str(selected_task)))
            df = pd.DataFrame.from_dict(data=response)
            if len(df):
                df.columns = ["Task", "Due Date", "Status"]
            myCatalog.table(df)


elif choice == "Delete Task ❌":
    st.subheader("Delete")
    response = requests.get(f"{backend}catalog/").json()
    df = pd.DataFrame.from_dict(data=response)
    if len(df):
        df.columns = ["Task", "Due Date", "Status"]
    myCatalog.table(df)

    list_of_jsons = requests.get(f"{backend}catalog/").json()
    unique_list = [dict["title"] for dict in list_of_jsons]
    delete_by_task_id = st.selectbox("Select Task To Delete", unique_list)
    if st.button("Delete ❌"):
        requests.delete(f"{backend}catalog/{str(delete_by_task_id)}")
        st.warning("Deleted Task \"{}\" ✅".format(delete_by_task_id))
        response = requests.get(f"{backend}catalog/").json()
        df = pd.DataFrame.from_dict(data=response)
        if len(df):
            df.columns = ["Task", "Due Date", "Status"]
        myCatalog.table(df)

st.markdown("<br><hr><center>Made by <strong>Daniel Faykin</strong></a></center><hr>", unsafe_allow_html=True)
