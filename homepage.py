from pages.utils import (
    text_loader,
    v_space,
    load_css,
    skill_builder,
    title_header,
    im,
    resume_file,
    profile_pic,
    portfolio_folder,
    logo_folder,
)
import base64
import streamlit as st
import json


st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Web Portfolio!",
    page_icon=im,
)
load_css()

# --------------------------------------------------------------
# PAGE TITLE
# --------------------------------------------------------------
title_header("Jeroen van Lier", line=True)


# --------------------------------------------------------------
# CONTACT BUTTONS
# -------------------------------------------------------------
with open(resume_file, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    b64_pdf_content = base64.b64encode(pdf_bytes).decode()
    download_pdf_href = f"""<a  href="data:application/pdf;base64,{b64_pdf_content}"  class="PortMarker homepageButton singleButton" download="{resume_file.name}">Download Resume!</a>"""
    st.markdown(download_pdf_href, unsafe_allow_html=True)

with col2:
    # Creating a button with a link using HTML and markdown
    button_html = """<p>
        <a href="https://calendly.com/jeroencvlier/30min" target="_blank">
            <button class='PortMarker homepageButton singleButton'>Virtual Coffee?</button>
        </a></p>
    """

    st.markdown(button_html, unsafe_allow_html=True)

with col3:
    # Creating a button with a link using HTML and markdown
    contact_html = """
        <a href="https://www.jeroencvlier.com/Contact" target="_self">
            <button class='PortMarker homepageButton singleButton'>Get In Touch?</button>
        </a>
    """
    st.markdown(contact_html, unsafe_allow_html=True)
v_space(1)

# --------------------------------------------------------------
# HERO SECTIOM
# --------------------------------------------------------------


def load_pp(profile_pic):
    with open(profile_pic, "rb") as f:
        pp = f.read()
    # Profile picture - > use this hack to center the image on iphone
    pp_bytes = base64.b64encode(pp).decode()
    pp_local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{pp_bytes}" alt="Image" style="width:100%;max-width:250px;"> </p>'
    return pp_local_file


pp_local_file = load_pp(profile_pic)
hero_text = text_loader(portfolio_folder, "hero")


col1, col2 = st.columns([0.325, 0.675], gap="medium")
with col1:
    st.write("\n")
    st.markdown(pp_local_file, unsafe_allow_html=True)

with col2:
    st.markdown(hero_text, unsafe_allow_html=True)

v_space(1)

# --------------------------------------------------------------
# SOCIAL BUTTONS
# --------------------------------------------------------------
# Your social media links
social_media = {
    "LinkedIn": {
        "link": "https://linkedin.com/in/jeroencvlier",
        "logo": f"{logo_folder}/linkedin_logo.png",
    },
    "GitHub": {
        "link": "https://github.com/jeroencvlier",
        "logo": f"{logo_folder}/github_logo.png",
    },
    "WhatsApp": {
        "link": "https://wa.me/message/3CEWOJJYMHLWA1",
        "logo": f"{logo_folder}/whatsapp_logo.png",
    },
}


def load_image(file_path):
    return base64.b64encode(open(file_path, "rb").read()).decode()


def load_logos(social_media):
    linkedin_logo = load_image(social_media["LinkedIn"]["logo"])
    github_logo = load_image(social_media["GitHub"]["logo"])
    whatsapp_logo = load_image(social_media["WhatsApp"]["logo"])
    return linkedin_logo, github_logo, whatsapp_logo


linkedin_logo, github_logo, whatsapp_logo = load_logos(social_media)

style_linkedin = "height:100%; max-height:50px; margin-right:30px;"  # 10px right margin
style_github = "height:100%; max-height:50px; margin-right:30px;"
style_whatsapp = "height:100%; max-height:50px;"

social_links = f"""

<div style="text-align:center">
    <a href="{social_media['LinkedIn']["link"]}"><img src="data:image/png;base64,{linkedin_logo}"  style="{style_linkedin}"/></a>
    <a href="{social_media['GitHub']["link"]}"><img src="data:image/png;base64,{github_logo}" style="{style_github}"/></a>
    <a href="{social_media['WhatsApp']["link"]}"><img src="data:image/png;base64,{whatsapp_logo}" style="{style_whatsapp}"/></a>
    <br></br>
</div>
"""
st.markdown(social_links, unsafe_allow_html=True)

# --------------------------------------------------------------
# Projects
# --------------------------------------------------------------
project_html = """
    <p><a href="https://www.jeroencvlier.com/Projects" target="_self" class='PortMarker homepageButton singleButton'>
        >>>  Check out my projects  <<<
    </a></p>
"""
st.markdown(project_html, unsafe_allow_html=True)

# --------------------------------------------------------------
# ABOUT ME
# --------------------------------------------------------------
aboutme_text = text_loader(portfolio_folder, "aboutme")
with st.container():
    st.markdown(aboutme_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# SKILLS
# --------------------------------------------------------------
def skill_loader(portfolio_folder):
    with open(f"{portfolio_folder}/skills.json", "r") as f:
        skills_json = json.load(f)
    return skills_json


skills_json = skill_loader(portfolio_folder)

with st.container():
    st.markdown(skill_builder(skills_json, level="Top Skills"), unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# EDUCATION
# --------------------------------------------------------------
def education_loader(portfolio_folder):
    with open(f"{portfolio_folder}/education.md", "r") as f:
        education_text = f.read()
    return education_text


# education_text = education_loader(portfolio_folder)
education_text = text_loader(portfolio_folder, "education")

with st.container():
    st.markdown(education_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# Qualifications
# --------------------------------------------------------------
qualifications_text = text_loader(portfolio_folder, "qualifications")


with st.container():
    st.markdown(qualifications_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# WORK HISTORY
# --------------------------------------------------------------
experience_text = text_loader(portfolio_folder, "experience")


with st.container():
    st.markdown(experience_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# Certificates
# --------------------------------------------------------------
certificates_text = text_loader(portfolio_folder, "certificates")

with st.container():
    st.markdown(certificates_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# Languages
# --------------------------------------------------------------
lang = skill_builder(skills_json, level="Languages")

with st.container():
    st.markdown(lang, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)
