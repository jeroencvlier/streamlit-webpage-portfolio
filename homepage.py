from pages.utils import *

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Web Portfolio!",
    page_icon=im,
)


load_css()

# --------------------------------------------------------------
# PAGE TITLE
# --------------------------------------------------------------
title_header("Jeroen van Lier")


# --------------------------------------------------------------
# CONTACT BUTTONS
# -------------------------------------------------------------


with open(resume_file, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

col2, col3, col4 = st.columns([4, 4, 4])

with col2:
    b64_pdf_content = base64.b64encode(pdf_bytes).decode()
    download_pdf_href = f"""<a  href="data:application/pdf;base64,{b64_pdf_content}"  class="PortMarker homepageButton" download="{resume_file}">Download Resume!</a>"""
    st.markdown(download_pdf_href, unsafe_allow_html=True)

with col3:
    # Creating a button with a link using HTML and markdown
    button_html = """<p>
        <a href="https://calendly.com/jeroencvlier/30min" target="_blank">
            <button class='PortMarker homepageButton'>Virtual Coffee?</button>
        </a></p>
    """
    st.markdown(button_html, unsafe_allow_html=True)

with col4:
    # Creating a button with a link using HTML and markdown
    contact_html = """
        <a href="https://jeroencvlier.com/Contact">
            <button class='PortMarker homepageButton'>Get In Touch?</button>
        </a>
    """
    st.markdown(contact_html, unsafe_allow_html=True)

st.write("\n")
# --------------------------------------------------------------
# HERO SECTIOM
# --------------------------------------------------------------
# Profile picture - > use this hack to center the image on iphone
with open(PROFILE_PIC, "rb") as f:
    pp = f.read()
with open(f"{portfolio_folder}/hero.md", "r") as f:
    hero_text = f.read()

pp_bytes = base64.b64encode(pp).decode()
pp_local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{pp_bytes}" alt="Image" style="width:100%;max-width:250px;"> </p>'

col1, col2 = st.columns([0.325, 0.675], gap="large")
with col1:
    st.write("\n")
    st.markdown(pp_local_file, unsafe_allow_html=True)

with col2:
    st.markdown(hero_text, unsafe_allow_html=True)

st.write("##")

# --------------------------------------------------------------
# SOCIAL BUTTONS
# --------------------------------------------------------------
# Your social media links
solical_media = {
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

# Generate base64 encodings of the logos
linkedin_logo = base64.b64encode(
    open(solical_media["LinkedIn"]["logo"], "rb").read()
).decode()
github_logo = base64.b64encode(
    open(solical_media["GitHub"]["logo"], "rb").read()
).decode()
whatsapp_logo = base64.b64encode(
    open(solical_media["WhatsApp"]["logo"], "rb").read()
).decode()

# Prepare the social links HTML

style_linkedin = "height:100%; max-height:50px; margin-right:30px;"  # 10px right margin
style_github = "height:100%; max-height:50px; margin-right:30px;"
style_whatsapp = "height:100%; max-height:50px;"

social_links = f"""

<div style="text-align:center">
    <a href="{solical_media['LinkedIn']["link"]}"><img src="data:image/png;base64,{linkedin_logo}"  style="{style_linkedin}"/></a>
    <a href="{solical_media['GitHub']["link"]}"><img src="data:image/png;base64,{github_logo}" style="{style_github}"/></a>
    <a href="{solical_media['WhatsApp']["link"]}"><img src="data:image/png;base64,{whatsapp_logo}" style="{style_whatsapp}"/></a>
    <br></br>
</div>
"""
st.markdown(social_links, unsafe_allow_html=True)

# --------------------------------------------------------------
# Projects
# --------------------------------------------------------------

project_html = """
    <p><a href="https://jeroencvlier.com/Projects">
        <button class='PortMarker homepageButton'> >>>  Check out my projects  <<< </button>
    </a></p>
"""
st.markdown(project_html, unsafe_allow_html=True)


# --------------------------------------------------------------
# SKILLS
# --------------------------------------------------------------

with open(f"{portfolio_folder}/skills.json", "r") as f:
    skills_json = json.load(f)

with st.container():
    st.markdown(skill_builder(skills_json, level="Top Skills"), unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)

# --------------------------------------------------------------
# EDUCATION
# --------------------------------------------------------------
with open(f"{portfolio_folder}/education.md", "r") as f:
    education_text = f.read()

with st.container():
    st.markdown(education_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)


# --------------------------------------------------------------
# Qualifications
# --------------------------------------------------------------
with open(f"{portfolio_folder}/qualifications.md", "r") as f:
    qualifications_text = f.read()

with st.container():
    st.markdown(qualifications_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)

# --------------------------------------------------------------
# Certificates
# --------------------------------------------------------------
with open(f"{portfolio_folder}/certificates.md", "r") as f:
    certificates_text = f.read()

with st.container():
    st.markdown(certificates_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)

# --------------------------------------------------------------
# WORK HISTORY
# --------------------------------------------------------------

with open(f"{portfolio_folder}/experience.md", "r") as f:
    experience_text = f.read()

with st.container():
    st.markdown(experience_text, unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)

# --------------------------------------------------------------
# Languages
# --------------------------------------------------------------

with st.container():
    st.markdown(skill_builder(skills_json, level="Languages"), unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)
