import streamlit as st
import requests  # For API calls (if using Django REST Framework)
import pandas as pd
from datetime import datetime

# Constants
DJANGO_API_URL = "http://127.0.0.1:8000/"  # Replace with your Django API URL

# Astronaut's name (you can fetch this dynamically based on login)
astronaut_name = "John Doe"
user_id = st.session_state['user_id']


# Page title and greeting
st.title(f"Welcome, {astronaut_name}!")
st.write("Here's your dashboard.")

# TO-DO
# Fetch tasks from Django (via API or direct database access)
def fetch_missions():
    # Example: Fetch tasks from Django API
    response = requests.get(f"{DJANGO_API_URL}/get_missions/{user_id}")
    if response.status_code == 200:
        tasks = response.json()
        return tasks
    else:
        st.error("Failed to fetch missions.")
        return []
    

 # TO-DO
# Fetch maintenance records from Django

def fetch_maintenance():
    ...
    '''# Example: Fetch maintenance records from Django API
    response = requests.get(f"{DJANGO_API_URL}/get_maintenance_history")
    if response.status_code == 200:
        maintenance_records = response.json()
        return maintenance_records
    else:
        st.error("Failed to fetch maintenance records.")
        return []
'''
# Mark a task as complete

def mark_task_complete(task_id):
    ...
    '''
    # Example: Update task status via Django API
    response = requests.patch(f"{DJANGO_API_URL}astronauts/{task_id}/", json={"status": "completed"})
    if response.status_code == 200:
        st.success("Task marked as complete!")
    else:
        st.error("Failed to update task status.")'''

# Display urgent maintenance notifications
def check_urgent_maintenance(maintenance_records):
    pass
    '''
    urgent_records = [record for record in maintenance_records if record.get("needs_maintenance")]
    if urgent_records:
        st.warning("🚨 Urgent Maintenance Required!")
        for record in urgent_records:
            st.write(f"- {record['description']} (Date: {record['date']})")
'''

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose an option", ["View Tasks", "View Maintenance Records"])

#Check for login before
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("You must log in first!")
    st.stop()
    
# Main content
if option == "View Tasks":
    st.header("Your Tasks")
    tasks = fetch_missions()
    if tasks:
        tasks_df = pd.DataFrame(tasks)
        st.table(tasks_df[["task", "startdate", "enddate", "status"]])
        
        # Mark task as complete
        task_id_to_complete = st.selectbox("Select a task to mark as complete", tasks_df["id"])
        if st.button("Mark as Complete"):
            ...
        #    mark_task_complete(task_id_to_complete)
    else:
        st.write("No missions found.")
'''
elif option == "View Maintenance Records":
    st.header("Maintenance Records")
    st.header("Maintenance Records")
    maintenance_records = fetch_maintenance()
    if maintenance_records:
        maintenance_df = pd.DataFrame(maintenance_records)
        st.table(maintenance_df[["date", "description", "needs_maintenance"]])
        
        # Check for urgent maintenance
        check_urgent_maintenance(maintenance_records)
    else:
        st.write("No maintenance records found.")

'''