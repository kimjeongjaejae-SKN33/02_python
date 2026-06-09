import streamlit as st

st.title("Media - image")

# 서버 이미지
st.image("../data/image1.png", "아아 그랬구나")

# 웹 이미지
st.image("https://media.istockphoto.com/id/520700958/ko/%EC%82%AC%EC%A7%84/%EC%95%84%EB%A6%84%EB%8B%A4%EC%9A%B4-%EA%BD%83-%EB%B0%B0%EA%B2%BD%EA%B8%B0%EC%88%A0.jpg?s=2048x2048&w=is&k=20&c=gpEjeueAlPUbIc4tF7Hrz6ke9HW1qdGTfNmB9gSR_Po=", caption = " 웹 이미지 ")
