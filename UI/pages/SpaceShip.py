import streamlit as st
import requests
import pandas as pd

# URL of the Django API endpoint
API_URL = 'http://127.0.0.1:8000/'

# Function to authenticate the user by username and password
def authenticate_user(username, password):
    response = requests.get(API_URL, params={'username': username, 'password': password})
    if response.status_code == 200:
        spaceships = response.json()
        if spaceships:
            return spaceships[0]  # Assuming that the spaceship corresponds to the user
        else:
            st.error("Invalid credentials or spaceship not found.")
            return None
    else:
        st.error("Failed to fetch data from Django API.")
        return None

# Function to display spaceship data in a readable format
def display_spaceship(spaceship):
    if spaceship:
        # Flatten the foreign key fields if needed and convert them into readable fields
        spaceship['data_id_temp'] = spaceship.get('data_id', {}).get('temp', 'N/A')
        spaceship['data_id_pressure'] = spaceship.get('data_id', {}).get('pressure', 'N/A')
        spaceship['data_id_radiationlevel'] = spaceship.get('data_id', {}).get('radiationlevel', 'N/A')
        spaceship['data_id_timestamp'] = spaceship.get('data_id', {}).get('timestamp', 'N/A')
        spaceship['data_id_needs_maintenance'] = spaceship.get('data_id', {}).get('needs_maintenance', 'N/A')

        spaceship['maintenance_id_description'] = spaceship.get('maintenance_id', {}).get('description', 'N/A')
        spaceship['maintenance_id_status'] = spaceship.get('maintenance_id', {}).get('status', 'N/A')
        spaceship['maintenance_id_scheduled_date'] = spaceship.get('maintenance_id', {}).get('scheduled_date', 'N/A')

        # Create a DataFrame for the spaceship
        df = pd.DataFrame([spaceship])
        
        # Display the spaceship in the Streamlit app
        st.write(df)  # This will render a table automatically in Streamlit
    else:
        st.write("No data to display.")

# Main page where spaceship data will be displayed
def main():
    st.title("Spaceship Data")

    # Check if username and password exist in session state
    if 'username' in st.session_state and 'password' in st.session_state:
        username = st.session_state['username']
        password = st.session_state['password']

        # Authenticate and get spaceship details
        spaceship = authenticate_user(username, password)

        # Display the spaceship details
        display_spaceship(spaceship)
    else:
        st.error("User is not logged in. Please login first.")

if __name__ == "__main__":
    main()
