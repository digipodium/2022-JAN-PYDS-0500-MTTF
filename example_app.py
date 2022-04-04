'''
to run this program

use command:
streamlit run example_app.py

'''

import streamlit as st
from oop.example_db import Task, PythonNews
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


def opendb():
    engine =  create_engine('sqlite:///demo.sqlite3', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

def saveTask(nm):
    db = opendb()
    t = Task(name=nm)
    db.add(t)
    db.commit()
    db.close()

st.title("A sample database app")

c1, c2 = st.columns([2,3])

with c1:
    f = st.form('taskform')
    f.subheader("Add a new task")
    name = f.text_input('Task name')
    btn  = f.form_submit_button('save')
    if btn and name:
        saveTask(name)
        st.success("Task saved")

with c2:
    st.subheader("My Task List")
    db = opendb()
    tasklist = db.query(Task).all()
    for task in tasklist:
        st.markdown(f'''
        ###### {task.id}: {task.name} 🕐{task.created_at}
        ''')
