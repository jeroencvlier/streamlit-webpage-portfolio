# utils.py
from pathlib import Path
import json

# Define directory paths
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
BASE_DIR = CURRENT_DIR.parent
CSS_FILE = BASE_DIR / "styles" / "main.css"

# Now you can use these paths in other files
import streamlit as st
from st_pages import hide_pages, show_pages_from_config

st.set_page_config(initial_sidebar_state="collapsed")


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


RESUME_FILE = BASE_DIR / "assets" / "resume.pdf"
LINKEDIN_LOGO = BASE_DIR / "assets" / "linkedin.png"
PROFILE_PIC = BASE_DIR / "assets" / "profile-pic.png"
RESUME_FILE = BASE_DIR / "assets" / "resume.pdf"
portfolio_folder = BASE_DIR / "assets" / "portfolio"


import cssutils

# Define the path to your CSS file
css_file_path = "styles/main.css"

# Read the CSS file
with open(css_file_path, "r") as file:
    css = file.read()

# Parse the CSS
sheet = cssutils.parseString(css)

# Iterate over the rules in the CSS
for rule in sheet:
    # We're only interested in style rules
    if isinstance(rule, cssutils.css.CSSStyleRule):
        # Check if the rule's selector is *
        if rule.selectorText == "*":
            # Iterate over the properties in the rule
            for property in rule.style:
                # We're only interested in the font-family property
                if property.name == "font-family":
                    FONT_FAMILY_1 = str(property.value)


def title_header(title, line=True):
    st.write("\n")
    if len(title.split(" ")) > 1:
        lh = "1.0"
    else:
        lh = "1.127"
    t = st.markdown(
        f"""
        <style>
            .title {{
                font-size:80px;
                text-align:center;
                color: black; 
                line-height: {lh};
                background: -webkit-linear-gradient(315deg, rgba(176,107,199,1) 30%, rgba(83,180,200,1) 70%); 
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family={FONT_FAMILY_1};
            }}
        </style>
        <div class="title">{title}</div>
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
        skills_html += "<div class='StyledHR'></div><br>"
        skills_html += skill_score(skills)

    elif level == "All Skills":
        skills = skills[level]
        for skill_section in skills:
            skills_html += "<br><div class='StyledHR'></div><br>"
            skill_set = skills[skill_section]
            skills_html += f"<h3>{skill_section}</h3>"
            skills_html += skill_score(skill_set)

    return skills_html


######### to delete

# st.markdown(
#     """
#     <style>
#     .PortMarker {
#         background-color: #313636;  /* Background color of the box same as the page background */

#         box-shadow: 10px 10px 15px 1px rgba(0, 0, 0, 0.3);

#         border: 1px solid #7a7c7c;  /* Border around the box - light gray color */
#         border-radius: 15px;
#         padding: 5% 5% 5% 10%;
#             }

#     .skill {
#         display: flex;
#         align-items: center;
#         margin-bottom: 0.5em;
#     }

#     .skill p {
#         margin: 0px;
#         width: 260px;
#     }

#     .bar-container {
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         width: 100%;
#     }

#     .bar {
#         width: 8%;
#         height: 10px;
#         margin-right: 2px;
#         border-radius: 5px;
#     }

#     .bar.filled:nth-child(1) { background-color: rgba(176,107,199,0.7); }
#     .bar.filled:nth-child(2) { background-color: rgba(168,113,198,0.7); }
#     .bar.filled:nth-child(3) { background-color: rgba(160,119,197,0.7); }
#     .bar.filled:nth-child(4) { background-color: rgba(152,125,196,0.7); }
#     .bar.filled:nth-child(5) { background-color: rgba(144,131,195,0.7); }
#     .bar.filled:nth-child(6) { background-color: rgba(136,137,194,0.7); }
#     .bar.filled:nth-child(7) { background-color: rgba(128,143,193,0.7); }
#     .bar.filled:nth-child(8) { background-color: rgba(120,149,192,0.7); }
#     .bar.filled:nth-child(9) { background-color: rgba(112,155,191,0.7); }
#     .bar.filled:nth-child(10) { background-color: rgba(83,180,200,0.7); }

#     .bar.unfilled { background-color: #ccc; }


#     .StyledHR {
#         width: 25%; /* Change this to the width you want */
#         height:5px;
#         border:none;
#         background: linear-gradient(270deg, rgba(176,107,199,0.7), rgba(83,180,200,0.7));
#         background-size: 200% 200%;
#         animation: Gradient 6s ease infinite;
#         border-radius: 15px;
#     }
#     @keyframes Gradient {
#         0% {background-position: 100% 0%;}
#         50% {background-position: 0% 100%;}
#         100% {background-position: 100% 0%;}
#     }

#     </style>
#     """,
#     unsafe_allow_html=True,
# )
