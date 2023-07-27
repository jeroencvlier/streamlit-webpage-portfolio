import base64
from pathlib import Path
from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image
from st_pages import Page, add_page_title, show_pages

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
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",
    initial_sidebar_state="expanded",
)
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
page = option_menu(
    menu_title=None,  # required
    options=["Home", "Contact", "Projects"],  # required
    icons=["house", "book", "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

show_pages(
    [
        Page("homepage.py", name=None, icon="🏠"),
        Page("pages/contact.py", name="Contact", icon="🏠"),
        Page(
            "pages/thanks.py",
            name=None,
            icon="",
            # is_section=True,
            # in_section=False,
            # use_relative_hash=True,
        ),
    ]
)

add_page_title()  # Optional method to add title and icon to current page


profile_pic = current_dir / "assets" / "profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

linkedin_logo = Image.open(current_dir / "assets" / "linkedin.png")

# Profile picture - > use this hack to center the image on iphone
with open(profile_pic, "rb") as f:
    image = f.read()
image_bytes = base64.b64encode(image).decode()
local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width = 260> </p>'


# --- HERO SECTION ---
col1, col2 = st.columns([0.9, 1.1], gap="small")
with col1:
    col1.subheader("")
    st.markdown(local_file, unsafe_allow_html=True)
    # st.image(profile_pic, width=260)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)
# st.button(label="Schedule a meeting",link="https://calendly.com/jeroencvlier/30min")

# https://calendly.com/jeroencvlier/30min
st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].image(linkedin_logo, width=30)
    cols[index].write(f":wave:[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
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

# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
