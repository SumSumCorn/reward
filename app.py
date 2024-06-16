import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from chatbot import chatWidget

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)
name, authentication_status, username = authenticator.login(max_login_attempts=3)

if st.session_state["authentication_status"]:
    authenticator.logout("로그아웃", "main")
    chatWidget()

elif st.session_state["authentication_status"] == False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] == None:
    st.warning("Please enter your username and password")

with open("./config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
