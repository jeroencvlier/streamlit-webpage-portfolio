# utils.py
from pathlib import Path

# Define directory paths
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
BASE_DIR = CURRENT_DIR.parent
CSS_FILE = BASE_DIR / "styles" / "main.css"

# Now you can use these paths in other files
import streamlit as st
from st_pages import hide_pages, show_pages_from_config 

def load_css():
    hide_pages(["Thanks"])
    with open(CSS_FILE) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
    show_pages_from_config()
    return

import os
import webbrowser
from st_pages import add_page_title

RESUME_FILE = BASE_DIR / "assets" / "resume.pdf"
LINKEDIN_LOGO = BASE_DIR / "assets" / "linkedin.png"
PROFILE_PIC = BASE_DIR / "assets" / "profile-pic.png"
RESUME_FILE = BASE_DIR / "assets" / "resume.pdf"


    
    
