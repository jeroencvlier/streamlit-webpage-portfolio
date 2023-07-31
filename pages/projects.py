from pages.utils import *

load_css()

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
        background-color: rgb(169,169,169);  /* Darker background color on hover */
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
