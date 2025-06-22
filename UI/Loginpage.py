import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/" # djangp api

st.set_page_config(page_title="SpaceShipAI - Login", page_icon="🚀", layout="wide")
def login(username, password):
    print(f"username: {username}, password: {password}")
    url = f"{API_URL}/login/"
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()  # Returns token and user id
    else:
        st.warning("Login Unsuccessfully")


def main():

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

   
    st.title("SpaceShipAI")
    
    username = st.text_input("Username", placeholder="Enter your username", key="username")
    password = st.text_input("Password",placeholder="Enter your password", type="password", key="passoword")
    
    if st.button("Login"):
        result = login(username, password)
        
        if result:
            st.session_state["logged_in"] = True
            st.session_state["user_id"] = result["user_id"]  # Store user data
            #st.experimental_rerun()  # Rerun to check login state
            if "logged_in" in st.session_state and st.session_state["logged_in"]:
                st.success("Login successful! Redirecting...")
                st.switch_page(r"pages/Astronaut.py")
            #elif True :
            #   st.success("Login successful! Redirecting...")
            #  st.switch_page(r"pages/SpaceShip.py")

        

        

if __name__ == "__main__":
    main()