"""Use assistant api in streamlit app with streaming."""

import streamlit as st
from streamlit import session_state as ss
from openai import OpenAI
import time


def init():
    # variables
    if "stream" not in ss:
        ss.stream = None
    if "messages" not in ss:
        ss.messages = [
            {
                "role": "assistant",
                "content": "안녕하세요! 저는 경기도 포상 도우미입니다. 경기도 2024년도 도지사 포상 업무지침에 관한 정보를 제공해 드리며, 포상 절차, 기준, 필요한 서류 등을 안내해 드립니다. 궁금한 사항이나 도움이 필요한 부분이 있으면 언제든지 질문해 주세요!",
            }
        ]
    if "oaik" not in ss:
        ss["oaik"] = st.secrets["OPENAI_API_KEY"]


# functions
def data_streamer():
    """
    That stream object in ss.stream needs to be examined in detail to come
    up with this solution. It is still in beta stage and may change in future releases.
    """
    for response in ss.stream:
        if response.event == "thread.message.delta":
            value = response.data.delta.content[0].text.value
            yield value
            time.sleep(0.1)


def init_assistant():
    """Define client and assistant"""
    client = OpenAI(api_key=ss.oaik, base_url=st.secrets["BASE_URL"])
    assistant = client.beta.assistants.retrieve(assistant_id=st.secrets["ASST_ID"])

    return client, assistant


def chatWidget():
    if "oaik" not in ss:
        st.text_input("enter openai api key", type="password", key="oaik")
        st.error("Please enter your open api key!")
        st.stop()

    # initialize openai assistant
    client, assistant = init_assistant()

    # show messages
    for message in ss.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # prompt user
    if prompt := st.chat_input("궁금한 내용을 질문하세요!"):

        ss.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        msg_history = [
            {"role": m["role"], "content": m["content"]} for m in ss.messages
        ]

        ss.stream = client.beta.threads.create_and_run(
            assistant_id=st.secrets["ASST_ID"],
            thread={"messages": msg_history},  # type: ignore
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(data_streamer)
            ss.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    chatWidget()
