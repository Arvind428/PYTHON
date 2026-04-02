import streamlit as st
st.title("To-Do-List")

#Create Empty List
if "tasks" not in st.session_state:
    st.session_state.tasks=[]

#Input box
task=st.text_input("Enter your task")

#Add Task
if st.button("Add"):
     if task:
        st.session_state.tasks.append({"task":task, "done":False})
#Show Tasks
st.write("### Your Tasks")

for i in range(len(st.session_state.tasks)):
    t=st.session_state.tasks[i]

    #Check Box
    done=st.checkbox(t["task"],value=t["done"],key=i)
    st.session_state.tasks[i]["done"]=done

# Rmove finished tasks
if st.button("Remove Finished Tasks"):
    st.session_state.tasks=[
        t for t in st.session_state.tasks if not t["done"]
    ]
    st.success("finshed taks removed")