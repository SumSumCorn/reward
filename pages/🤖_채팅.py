import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)
name, authentication_status, username = authenticator.login(
    fields={
        "Form name": "로그인",
        "Username": "아이디",
        "Password": "패스워드",
        "Login": "로그인",
    },
    max_login_attempts=3,
)

if st.session_state["authentication_status"]:
    authenticator.logout("로그아웃", "main")
    from chatbot import chatWidget, init

    init()
    chatWidget()

elif st.session_state["authentication_status"] == False:
    st.error("아이디/비밀번호가 일치하지 않습니다.")
elif st.session_state["authentication_status"] == None:
    st.warning("아이디와 패스워드를 입력하시오.")

with open("./config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
