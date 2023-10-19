import streamlit as st
from pages.utils import im, back_button, load_css, v_space, title_header

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Thank You!",
    page_icon=im,
)

load_css()
from streamlit_extras.let_it_rain import rain

gif_url = "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif"
title_header("Message Recieved!", line=False)


# Centering the image
left_col, cent_col, last_col = st.columns(3)

with cent_col:
    st.image(gif_url)

v_space(1)
st.write("Thank you for reaching out, I will get back to you as soon as possible.")


# --------------------------------------------------------------
# Home
# --------------------------------------------------------------
back_button("Home")
