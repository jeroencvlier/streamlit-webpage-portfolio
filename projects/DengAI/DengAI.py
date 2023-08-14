from pages.utils import (
    load_css,
    title_header,
    project_folder,
    project_buttons,
    load_mp4,
    im,
)
import streamlit as st
import pandas as pd

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | DengAI!",
    page_icon=im,
)

load_css()
title_header("Forecasting Dengue Fever", title_class="title3", line=False)
this_project = project_folder / "DengAI"


# --------------------------------------------------------------
# Project Introduction
# --------------------------------------------------------------

with open(f"{this_project}/introduction.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)


# --------------------------------------------------------------
# Project Image
# --------------------------------------------------------------
# st.write("##")

# video_file_path = f"{this_project}/Tennis.mp4"
# st.markdown(load_mp4(video_file_path), unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Map
# --------------------------------------------------------------

df_city_longlat = pd.read_csv(f"{this_project}/data/city_longlat.csv")

# custom_css = """

# """

# Applying custom CSS
# st.markdown(custom_css, unsafe_allow_html=True)

# Wrapping the map in a custom-styled container
with st.container():
    st.map(df_city_longlat, size=100000, zoom=3)

# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------
# st.write("##")

with open(f"{this_project}/description.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/MultiAgent-Tennis-MADDPG"
project_buttons(github_link)