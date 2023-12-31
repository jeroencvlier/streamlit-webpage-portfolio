import streamlit as st
from pages.utils import load_css, title_header, im, back_button

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Projects!",
    page_icon=im,
)

load_css()
title_header("Projects")


project_items = {
    "Forecasting Dengue Fever": "DengAI",
    "Streamlit Portfolio": "Streamlit Portfolio",
    "Multi-agent Reinforcement Learning": "Multi-agent Reinforcement Learning",
    "Continuous Control Reinforcement Learning": "Continuous Control Reinforcement Learning",
}


# Convert the dictionary items to a list
# project_items = list(projects.items())

# Iterate over the list in chunks of 3
for i in range(0, len(project_items), 3):
    keys = list(project_items.keys())
    sliced_keys = keys[i : i + 3]
    chunk = {key: project_items[key] for key in sliced_keys}

    if len(chunk) == 1:
        blank1, col, blank2 = st.columns([0.33, 0.33, 0.33])
        columns = [col]
    if len(chunk) == 2:
        blank1, left, right, blank2 = st.columns([0.17, 0.33, 0.33, 0.17])
        columns = [left, right]
    if len(chunk) == 3:
        columns = st.columns(3)

    if len(chunk) < 3:
        with blank1:
            st.empty()
        with blank2:
            st.empty()
    for en, (project, page) in enumerate(chunk.items()):  # No zip here
        # for col, proj in zip(columns, chunk):
        with columns[en]:
            st.markdown(
                f"""<p><a href="https://www.jeroencvlier.com/{page.replace(' ','%20')}" target="_self">
                <button class='PortMarker homepageButton projectButton'>{project}</button>
                </a></p>""",
                unsafe_allow_html=True,
            )


# --------------------------------------------------------------
# Back
# --------------------------------------------------------------
st.write("---")

back_button("Homepage")
