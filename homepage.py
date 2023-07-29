import base64
import streamlit as st
from PIL import Image
from pages.utils import *

load_css()

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jeroen van Lier | Digital Portfolio"
PAGE_ICON = ":wave:"
NAME = "Jeroen van Lier"
DESCRIPTION = """
Data Scientist with 7 years of experience in extracting actionable insights from data. Strong hands on experience and knowledge in Python and Excel. Good understanding of statistical principles and their respective applications. Excellent team-player and displaying strong sense of initiative on tasks."""
EMAIL = "jeroencvlier@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/jeroencvlier",
    "GitHub": "https://github.com/jeroencvlier",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}




with open(RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    

# Profile picture - > use this hack to center the image on iphone
with open(PROFILE_PIC, "rb") as f:
    pp = f.read()
pp_bytes = base64.b64encode(pp).decode()
pp_local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{pp_bytes}" alt="Image" width = 260> </p>'

# --------------------------------------------------------------
# HERO SECTIOM
# --------------------------------------------------------------
col1, col2 = st.columns([0.9, 1.1], gap="small")
with col1:
    col1.subheader("")
    st.markdown(pp_local_file, unsafe_allow_html=True)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

# --------------------------------------------------------------
# BUTTONS
# --------------------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=RESUME_FILE.name,
        mime="application/octet-stream",
        use_container_width=True
    )

with col2:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
    if st.button('Book some time with me', use_container_width=True):
        webbrowser.open_new_tab("https://calendly.com/jeroencvlier/30min")

with col3:
    st.write("""<div class='ButtonWidth'/>""", unsafe_allow_html=True)
    if st.button('Email me', disabled=True, use_container_width=True,):
        pass
                
    
    
# --------------------------------------------------------------
# Social Section
# --------------------------------------------------------------
linkedin_logo = Image.open(LINKEDIN_LOGO)

# st.write("\n")
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].image(linkedin_logo, width=30)
#     cols[index].write(f":wave:[{platform}]({link})")


# --------------------------------------------------------------
# Experience & Qualifications
# --------------------------------------------------------------
st.write("\n")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
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
