import base64
import streamlit as st
from PIL import Image
from pages.utils import *

load_css()


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jeroen van Lier | Digital Portfolio"
PAGE_ICON = ":wave:"
DESCRIPTION = """
Data Scientist with 7 years of experience in extracting actionable insights from data. Strong hands on experience and knowledge in Python and Excel. Good understanding of statistical principles and their respective applications. Excellent team-player and displaying strong sense of initiative on tasks."""
EMAIL = "jeroencvlier@gmail.com"

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

with open(RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --------------------------------------------------------------
# Menu
# --------------------------------------------------------------

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
        height: 60px;
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

for col, text, page in zip(st.columns(2), ["Home", "Project"], ["home", "projects"]):
    with col:
        # st.write("""<div class='myButton'/>""", unsafe_allow_html=True)
        # if st.button(
        #     text,
        #     key=text,
        #     disabled=False,
        #     use_container_width=True,
        # ):
        st.markdown(f"<button class='myButton'>{text}</button>", unsafe_allow_html=True)

        # pass
# --------------------------------------------------------------
# PAGE TITLE
# --------------------------------------------------------------
title_header("Jeroen van Lier")


# --------------------------------------------------------------
# HERO SECTIOM
# --------------------------------------------------------------
# Profile picture - > use this hack to center the image on iphone
with open(PROFILE_PIC, "rb") as f:
    pp = f.read()
pp_bytes = base64.b64encode(pp).decode()
# pp_local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{pp_bytes}" alt="Image" width = 240> </p>'
pp_local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{pp_bytes}" alt="Image" style="width:100%;"> </p>'


col1, col2 = st.columns([0.325, 0.675], gap="large")
with col1:
    # col1.subheader("")
    st.markdown(pp_local_file, unsafe_allow_html=True)
with col2:
    # st.title(NAME)
    st.write("\n" + DESCRIPTION)

# --------------------------------------------------------------
# CONTACT BUTTONS
# --------------------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
    st.download_button(
        label="Pull CV!",
        data=PDFbyte,
        file_name=RESUME_FILE.name,
        mime="application/octet-stream",
        use_container_width=True,
    )

with col2:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
    if st.button("Virtual Coffee?", use_container_width=True):
        webbrowser.open_new_tab("https://calendly.com/jeroencvlier/30min")

with col3:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
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
# Experience & Qualifications
# --------------------------------------------------------------
st.write("""<div class='PortMarker'/>""", unsafe_allow_html=True)
# st.write("\n")
# st.markdown(contact_form, unsafe_allow_html=True)
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

st.markdown(
    """<div class='PortMarker'>
<h3>Experience & Qulifications</h3>
<p>
- ✔️ 7 Years expereince extracting actionable insights from data <br/>
- ✔️ Strong hands on experience and knowledge in Python and Excel <br/>
- ✔️ Good understanding of statistical principles and their respective applications <br/>
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks <br/>
</p>
</div>""",
    unsafe_allow_html=True,
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write("""<div class='PortMarker'/>""", unsafe_allow_html=True)

st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write("\n")
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)

# # --- Projects & Accomplishments ---
# st.write("\n")
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
