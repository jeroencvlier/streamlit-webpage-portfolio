from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Projects!",
    page_icon=im,
)

load_css()
title_header("Projects")


project_items = [
    "Streamlit Portfolio",
    "Multi-agent Reinforcement Learning",
    "Continuous Control Reinforcement Learning",
    "Project 4",
    "Project 5",
    "Project 6",
    "Project 7",
    "Project 8",
]


# Convert the dictionary items to a list
# project_items = list(projects.items())

# Iterate over the list in chunks of 3
for i in range(0, len(project_items), 3):
    chunk = project_items[i : i + 3]

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
    for en, project in enumerate(chunk):
        # for col, proj in zip(columns, chunk):
        with columns[en]:
            st.markdown(
                f"""<p><a href="https://jeroencvlier.com/{project.replace(' ','%20')}" target="_self">
                <button class='PortMarker homepageButton projectButton'>{project}</button>
                </a></p>""",
                unsafe_allow_html=True,
            )
