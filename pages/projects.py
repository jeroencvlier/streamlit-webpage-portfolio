from pages.utils import *

load_css()
title_header("Projects")

st.markdown(
    """
    <style>
    .myButton {
        border-radius: 20px;
        display: inline-block;
        position: relative;
        padding: 10px 20px;
        border: 2px solid rgb(70,70,70);  /* Initial border */
        font-size: 1em;
        text-decoration: none; /* Removes underline */
        height: 110px;
        width: 100%;  /* Set width to 100% */
        background-color: rgb(211,211,211);
        overflow: hidden; /* Ensure the content doesn't overflow the border */
    }

    .myButton:hover {
        background-size: 150% auto;
        animation: Gradient 4s ease infinite;
        background-image: linear-gradient(135deg, rgba(176,107,199,0.7), rgba(83,180,200,0.7));
    }

    @keyframes Gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


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
                f"<button class='myButton'>{proj}</button>", unsafe_allow_html=True
            )
