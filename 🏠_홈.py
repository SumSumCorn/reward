import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="경기도 포상 도우미",
    page_icon="🏅",
    layout="centered",
    initial_sidebar_state="expanded",
)
# 이미지 추가 (원하는 이미지 파일로 대체)
st.image(
    "gyeonggi_logo.png",
    caption="경기도 도지사 포상",
    # use_column_width=True,
    width=300,
)
# 페이지 제목과 설명
st.title(
    "경기도 포상 도우미",
)
st.header("안녕하세요!")
st.subheader("저는 경기도 포상 도우미입니다.")
st.write(
    """
    경기도 2024년도 도지사 포상 업무지침에 관한 정보를 제공해 드리며,
    포상 절차, 기준, 필요한 서류 등을 안내해 드립니다.
    궁금한 사항이나 도움이 필요한 부분이 있으면 언제든지 질문해 주세요!
    """
)


# 포상 절차 안내
st.subheader("포상 절차")
st.write(
    """
    1. 포상 신청서 작성
    2. 관련 서류 제출
    3. 심사 및 검토
    4. 포상 대상자 선정
    5. 포상 수여식
    """
)

# 포상 기준 안내
st.subheader("포상 기준")
st.write(
    """
    - 공공 서비스에 기여한 공로
    - 지역사회 발전에 기여한 업적
    - 기타 도지사가 인정한 공로
    """
)

# 필요한 서류 안내
st.subheader("필요한 서류")
st.write(
    """
    - 포상 신청서
    - 추천서
    - 공적 증빙 자료
    """
)

# 문의 사항 입력 폼
st.subheader("문의 사항")
st.write("궁금한 사항이나 도움이 필요한 부분이 있으면 아래에 작성해 주세요!")
with st.form(key="question_form"):
    user_name = st.text_input("이름")
    user_email = st.text_input("이메일")
    user_question = st.text_area("문의 내용")
    submit_button = st.form_submit_button(label="제출")

if submit_button:
    st.write(
        f"감사합니다, {user_name}님! 귀하의 문의 사항을 접수했습니다. 곧 답변드리겠습니다."
    )

# 푸터
st.write("---")
st.write("© 2024 경기도 포상 도우미. All rights reserved.")
