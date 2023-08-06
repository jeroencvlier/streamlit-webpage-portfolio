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
st.write("##")

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
# CONTACT BUTTONS
# -------------------------------------------------------------

col1, col2, col3 = st.columns(3)
with col1:
    with open(RESUME_FILE, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Pull CV!",
        data=PDFbyte,
        file_name=RESUME_FILE.name,
        mime="application/octet-stream",
        use_container_width=True,
    )

with col2:
    if st.button("Virtual Coffee?", use_container_width=True):
        webbrowser.open_new_tab("https://calendly.com/jeroencvlier/30min")

with col3:
    if st.button(
        "Get In Touch!",
        disabled=False,
        use_container_width=True,
    ):
        switch_page("contact")
        pass


# --------------------------------------------------------------
# SKILLS
# --------------------------------------------------------------


with open(f"{portfolio_folder}/skills.json", "r") as f:
    skills_json = json.load(f)

with st.container():
    st.markdown(skill_builder(skills_json, level="Top Skills"), unsafe_allow_html=True)
st.write("##")

# --------------------------------------------------------------
# EDUCATION
# --------------------------------------------------------------
with open(f"{portfolio_folder}/education.md", "r") as f:
    education_text = f.read()

with st.container():
    st.markdown(education_text, unsafe_allow_html=True)


st.write("##")

# --------------------------------------------------------------
# Qualifications
# --------------------------------------------------------------
with open(f"{portfolio_folder}/qualifications.md", "r") as f:
    qualifications_text = f.read()

with st.container():
    st.markdown(qualifications_text, unsafe_allow_html=True)
st.write("##")

# --------------------------------------------------------------
# Certificates
# --------------------------------------------------------------
with open(f"{portfolio_folder}/certificates.md", "r") as f:
    certificates_text = f.read()

with st.container():
    st.markdown(certificates_text, unsafe_allow_html=True)
st.write("##")

# --------------------------------------------------------------
# WORK HISTORY
# --------------------------------------------------------------

with open(f"{portfolio_folder}/experience.md", "r") as f:
    experience_text = f.read()

with st.container():
    st.markdown(experience_text, unsafe_allow_html=True)
st.write("##")

# --------------------------------------------------------------
# Languages
# --------------------------------------------------------------

with st.container():
    st.markdown(skill_builder(skills_json, level="Languages"), unsafe_allow_html=True)
st.write("##")
