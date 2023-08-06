from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Skills",
    page_icon=im,
)


load_css()

title_header("Skills", line=False)

with open(f"{portfolio_folder}/skills.json", "r") as f:
    skills_json = json.load(f)

with st.container():
    st.markdown(skill_builder(skills_json, level="All Skills"), unsafe_allow_html=True)
st.write("##")
