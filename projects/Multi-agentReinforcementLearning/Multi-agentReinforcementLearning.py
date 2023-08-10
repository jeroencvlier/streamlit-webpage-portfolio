from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | RL - MultiAgent!",
    page_icon=im,
)

load_css()
title_header("Multi-agent RL", line=True)
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




gif_local_file = load_gif(f"{this_project}/Tennis.gif")


with st.container():
    st.markdown(gif_local_file, unsafe_allow_html=True)
