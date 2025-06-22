import streamlit as st
import requests  
import pandas as pd

MISSION_API_URL = 'http://127.0.0.1:8000/'

def fetch_missions():
    # Making a GET request to the API to fetch mission data
    try:
        response = requests.get(MISSION_API_URL)
        if response.status_code == 200:
            return response.json()  # Returning the JSON data from the response
        else:
            st.error("Failed to fetch missions from the API.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    



def display_missions(missions):
    if missions:
        # Convert the list of missions into a pandas DataFrame for easy display
        df = pd.DataFrame(missions)

        # Flatten foreign key relationships into more readable columns (e.g., astronaut_name, spaceship_name)
        if 'astronaut' in df.columns:
            df['astronaut_name'] = df['astronaut'].apply(lambda x: x.get('name', 'N/A') if isinstance(x, dict) else 'N/A')
            df.drop(columns=['astronaut'], inplace=True)

        if 'spaceship' in df.columns:
            df['spaceship_name'] = df['spaceship'].apply(lambda x: x.get('name', 'N/A') if isinstance(x, dict) else 'N/A')
            df.drop(columns=['spaceship'], inplace=True)

        # Tasks will be a list, so we can convert them to strings to display
        if 'tasks' in df.columns:
            df['tasks'] = df['tasks'].apply(lambda tasks: ', '.join([task['name'] for task in tasks]) if isinstance(tasks, list) else 'No tasks')

        # Display the DataFrame as a table in Streamlit
        st.write(df)
    else:
        st.write("No mission data available.")    





def main():
    st.title("Mission Data")

    # Fetch the missions from the Django API
    missions = fetch_missions()

    # Display the missions data
    display_missions(missions)

    # Add interactivity: Button to navigate to the tasks page
    if st.button("Go to Tasks Page"):
        # Navigate to the tasks page (replace `tasks` with your actual page logic)
        st.session_state.page = "tasks"

if __name__ == "__main__":
    main()
