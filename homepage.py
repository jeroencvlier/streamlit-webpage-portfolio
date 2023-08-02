import base64
import streamlit as st
from PIL import Image
from pages.utils import *

load_css()


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jeroen van Lier | Digital Portfolio"
PAGE_ICON = ":wave:"
EMAIL = "jeroencvlier@gmail.com"


with open(RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --------------------------------------------------------------
# Menu
# --------------------------------------------------------------

# st.markdown(
#     """
#     <style>
#     div.stButton > Button:first-child  {
#         border-radius: 20px;
#         display: inline-block;
#         position: relative;
#         padding: 10px 20px;
#         border: 2px solid rgb(70,70,70);  /* Initial border */
#         font-size: 1em;
#         text-decoration: none; /* Removes underline */
#         height: 110px;
#         width: 100%;  /* Set width to 100% */
#         background-color: rgb(211,211,211);
#         overflow: hidden; /* Ensure the content doesn't overflow the border */
#     }

#     div.stButton > Button:first-child:hover {
#         background-size: 150% auto;
#         animation: Gradient 4s ease infinite;
#         background-image: linear-gradient(135deg, rgba(176,107,199,0.7), rgba(83,180,200,0.7));
#     }

#     @keyframes Gradient {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


for col, text, page in zip(st.columns(2), ["Home", "Project"], ["home", "projects"]):
    with col:
        if st.button(
            text,
            key=page,
            disabled=False,
            use_container_width=True,
        ):
            switch_page(page)
            pass


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
# with st.container():
col1, col2 = st.columns([0.325, 0.675], gap="large")
with col1:
    st.write("\n")
    st.markdown(pp_local_file, unsafe_allow_html=True)
with col2:
    st.markdown(hero_text, unsafe_allow_html=True)

st.write("##")
# --------------------------------------------------------------
# CONTACT BUTTONS
# --------------------------------------------------------------

col1, col2, col3 = st.columns(3)
with col1:
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
# SOCIAL BUTTONS
# --------------------------------------------------------------
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/jeroencvlier",
    "GitHub": "https://github.com/jeroencvlier",
}
SOCIAL_MEDIA_LOGOS = {"LinkedIn": LINKEDIN_LOGO, "GitHub": LINKEDIN_LOGO}

linkedin_logo = Image.open(LINKEDIN_LOGO)
linkedin_logo = base64.b64encode(
    open(LINKEDIN_LOGO, "rb").read()
).decode()  # you will have to import base64 for this

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
        if st.button(
            platform,
            disabled=False,
            use_container_width=True,
        ):
            webbrowser.open_new_tab(link)

# --------------------------------------------------------------
# Container STYLE
# --------------------------------------------------------------
st.markdown(
    """
    <style>
    .PortMarker {
        background-color: #313636;  /* Background color of the box same as the page background */
        
        box-shadow: 10px 10px 15px 1px rgba(0, 0, 0, 0.3);

        border: 1px solid #7a7c7c;  /* Border around the box - light gray color */
        border-radius: 15px;
        padding: 5% 5% 5% 10%;
    }
    .StyledHR {
        width: 25%; /* Change this to the width you want */
        height:5px;
        border:none;
        background: linear-gradient(270deg, rgba(176,107,199,0.7), rgba(83,180,200,0.7));
        background-size: 200% 200%;
        animation: Gradient 6s ease infinite;
        border-radius: 15px;
    }  
    @keyframes Gradient {
        0% {background-position: 100% 0%;}
        50% {background-position: 0% 100%;}
        100% {background-position: 100% 0%;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------
# SKILLS
# --------------------------------------------------------------
with open(f"{portfolio_folder}/skills.md", "r") as f:
    skills_text = f.read()

with st.container():
    st.markdown(skills_text, unsafe_allow_html=True)
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


# # --- Projects & Accomplishments ---
# st.write("\n")
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
