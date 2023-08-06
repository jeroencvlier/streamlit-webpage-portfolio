from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Thank You!",
    page_icon=im,
)


load_css()
from streamlit_extras.let_it_rain import rain


rain(
    emoji="🎈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

gif_url = "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif"
st.title("Thank you for your reaching out!")
st.image(gif_url)
st.write("I will get back to you as soon as possible.")
