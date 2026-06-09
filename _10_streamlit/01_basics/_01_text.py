import streamlit as st

# 실행 명령어
# streamlit run [파일명].py

# 제목
st.title('Hello, Streamlit!😁')


st.header("Text")
st.subheader("subheader")
st.subheader(":green[sub]header")

# text : 단순 글자
st.text("text 테스트 !!!")

# write
# - 단순 글자 뿐만 아니라
# 마크다운, 표, 리스트, 차트,
# 입력 타입 등에 따라 출력방식 정해짐
st.write("write 테스트!!!")
st.write("write **markdown** 지원")
st.write("`write`")

st.markdown("### markdown")

st.html("<h3><mark>html</mark>도 지원 </h3>")

st.subheader(":red[magic]", divider = "orange")
" streamlit magic"
"변수나 리터럴 값이 출력 구문 내에 없어도 화면에 값을 기록하는 기능"
100
[10,20,30]
{"a" : 10, "b" : 20}

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)


#metric : 측량, 측정
import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")