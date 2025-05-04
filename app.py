
import streamlit as st
import pandas as pd

st.title("문자 대량 전송 시뮬레이터")

# 1. 수신자 목록 업로드
uploaded_file = st.file_uploader("수신자 목록 업로드 (이름, 전화번호 포함)", type=["xlsx", "csv"])
if uploaded_file:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith("xlsx") else pd.read_csv(uploaded_file)
    st.write("업로드된 목록", df)

    # 2. 메시지 템플릿 입력
    template = st.text_area("문자 템플릿 입력", "예: {이름}님, 오늘 교육은 오후 2시입니다.")

    # 3. 전송 버튼
    if st.button("문자 전송 (가상)"):
        sent_messages = []
        for _, row in df.iterrows():
            name = str(row["이름"])
            phone = str(row["전화번호"])
            message = template.replace("{이름}", name)
            sent_messages.append({"이름": name, "전화번호": phone, "문자내용": message})

        result_df = pd.DataFrame(sent_messages)
        st.success("가상 문자 전송 완료!")
        st.dataframe(result_df)

        # 결과 다운로드
        st.download_button(
            label="결과 엑셀 다운로드",
            data=result_df.to_excel(index=False, engine='openpyxl'),
            file_name="문자전송_시뮬레이션결과.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
