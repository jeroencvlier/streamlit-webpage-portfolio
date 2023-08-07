from pages.utils import *

load_css()
title_header("Projects")

projects13 = ["project1", "project2", "project3"]
projects46 = ["project4", "project5", "project6"]
projects79 = ["project7", "project8"]

for project in [projects13, projects46, projects79]:
    if len(project) == 1:
        _, col, _ = st.columns([0.33, 0.33, 0.33])
        columns = [col]
    if len(project) == 2:
        _, left, right, _ = st.columns([0.17, 0.33, 0.33, 0.17])
        columns = [left, right]
    if len(project) == 3:
        columns = st.columns(3)

    for col, proj in zip(columns, project):
        with col:
            st.markdown(
                f"<button class='gradientButton'>{proj}</button>",
                unsafe_allow_html=True,
            )
