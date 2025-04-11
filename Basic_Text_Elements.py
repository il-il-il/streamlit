import streamlit as st
# Basic Text Elements of Streamlit
st.title("Streamlit Tutorial")
st.subheader("1-Basic Text Elements of Streamlit")


st.text("streamlit is an open-source Python library that " \
"allows you to quickly and easily create interactive web " \
"applications for data science and machine learning projects.")

st.markdown("**Streamlit** supports Markdown, allowing you to " \
"display formatted *text*, *headers*, *lists*, *links*, *images*,"
" and more in your app. You can use the `st.markdown()` function" \
" to easily render Markdown content.")

st.markdown("---")

st.markdown("[Github](https://github.com/il-il-il)")


st.caption("`st.caption()` in Streamlit is used to display" \
" small, gray, and less prominent text — great for footnotes," \
" image descriptions, or subtle explanations.")
st.markdown("---")
st.caption("**5:00** Streamlit Tutorial 4")