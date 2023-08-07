# utils.py
from pathlib import Path
import json

# Define directory paths
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
BASE_DIR = CURRENT_DIR.parent
CSS_FILE = BASE_DIR / "styles" / "main.css"
RESUME_FILE = BASE_DIR / "assets" / "resume.pdf"
logo_folder = BASE_DIR / "assets" / "logos"

PROFILE_PIC = BASE_DIR / "assets" / "profile-pic.png"
resume_file = BASE_DIR / "assets" / "resume.pdf"
portfolio_folder = BASE_DIR / "assets" / "portfolio"
page_icon = BASE_DIR / "assets" / "page_icon.ico"

# Now you can use these paths in other files
import streamlit as st
from st_pages import hide_pages, show_pages_from_config
from PIL import Image


im = Image.open(page_icon)


def load_css():
    hide_pages(["Thanks"])

    with open(CSS_FILE) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    show_pages_from_config()

    return


import os
import webbrowser
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page
import re
import base64


def title_header(title, line=True):
    # st.write("\n")
    if len(title.split(" ")) > 1:
        title_class = "title1"
    else:
        title_class = "title2"
    t = st.markdown(
        f"""
        <div class="{title_class}">{title}</div>
    """,
        unsafe_allow_html=True,
    )
    st.write("###")
    if line:
        st.write("---")

    return t


def skill_score(skill_set):
    skills_score_html = ""
    for skill, score in skill_set.items():
        skills_score_html += (
            f'<div class="skill">\t<p>{skill}</p>\t<div class="bar-container">'
        )

        skills_score_html += '\t\t<div class="bar filled"></div>\n' * score
        skills_score_html += '\t\t<div class="bar unfilled"></div>\n' * (10 - score)
        skills_score_html += "\t</div>\n</div>\n"
    return skills_score_html


def skill_builder(skills, level=None):
    skills_html = "<div class='PortMarker'>"
    if level == "Top Skills":
        skills = skills[level]
        skills_html += f"<h2>Skills</h2>"
        skills_html += "<br><div class='StyledHR'></div><br>"
        skills_html += skill_score(skills)
        skills_html += '<div style="text-align: right;"><a class="click_link" href="https://www.jeroencvlier.com/Skills" target="_self">Details >></a></div>'
        # skills_html += '<p></p><div class="click_link"><a href="https://www.jeroencvlier.com/Skills"Click here for more details >></a></div>'
    elif level == "Languages":
        skills = skills[level]
        skills_html += f"<h2>Languages</h2>"
        skills_html += "<br><div class='StyledHR'></div><br>"
        skills_html += skill_score(skills)
    elif level == "All Skills":
        skills = skills[level]
        for en, skill_section in enumerate(skills):
            if en != 0:
                skills_html += "<br><div class='StyledHR'></div><br>"
            skill_set = skills[skill_section]
            skills_html += f"<h3>{skill_section}</h3>"
            skills_html += skill_score(skill_set)

    return skills_html
