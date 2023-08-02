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


def title_header(title):
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
    st.write("---")

    return t
