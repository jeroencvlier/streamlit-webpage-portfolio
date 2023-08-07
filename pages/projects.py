from pages.utils import *

load_css()
title_header("Projects")

projects13 = ["project1", "project2", "project3"]
projects46 = ["project4", "project5", "project6"]
projects79 = ["project7", "project8"]

# for project in [projects13, projects46, projects79]:
#     if len(project) == 1:
#         _, col, _ = st.columns([0.33, 0.33, 0.33])
#         columns = [col]
#     if len(project) == 2:
#         _, left, right, _ = st.columns([0.17, 0.33, 0.33, 0.17])
#         columns = [left, right]
#     if len(project) == 3:
#         columns = st.columns(3)

#     for col, proj in zip(columns, project):
#         with col:
#             st.markdown(
#                 f"<button class='PortMarker homepageButton projectButton'>{proj}</button>",
#                 unsafe_allow_html=True,
#             )
for project in [projects13, projects46, projects79]:
    # Calculate the number of empty columns required on each side
    num_empty_columns = (3 - len(project)) // 2

    # Create a layout with equally spaced empty columns
    layout = (
        [0.33] * num_empty_columns + [0.33] * len(project) + [0.33] * num_empty_columns
    )

    # Create the columns using the layout
    columns = st.columns(layout)

    # Only work with the middle columns that will contain the buttons
    button_columns = columns[num_empty_columns : num_empty_columns + len(project)]

    for col, proj in zip(button_columns, project):
        with col:
            st.markdown(
                f"<button class='PortMarker homepageButton projectButton'>{proj}</button>",
                unsafe_allow_html=True,
            )
