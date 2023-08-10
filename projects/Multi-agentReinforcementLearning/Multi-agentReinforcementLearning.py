from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | RL - MultiAgent!",
    page_icon=im,
)

load_css()
title_header("Multi Agent RL", title_class="title3", line=True)
this_project = project_folder / "Multi-agentReinforcementLearning"


# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------

with open(f"{this_project}/project_readme.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Image
# --------------------------------------------------------------
st.write("##")

video_file_path = f"{this_project}/Tennis.mp4"
st.markdown(load_mp4(video_file_path), unsafe_allow_html=True)


# --------------------------------------------------------------
# Github link
# --------------------------------------------------------------
st.write("##")
project_html = """
    <p><a href="https://github.com/jeroencvlier/MultiAgent-Tennis-MADDPG" target="_blank">
        <button class='PortMarker homepageButton'>Check out the code >>></button>
    </a></p>
"""
st.markdown(project_html, unsafe_allow_html=True)
