import streamlit as st
from pathlib import Path

current_directory = Path(__file__).parent if "__file__" in locals() else Path.cwd()
base_directory = current_directory.parent
css_file = base_directory / "styles" / "main.css"
logo_folder = base_directory / "assets" / "logos"
profile_pic = base_directory / "assets" / "profile-pic_2.png"
resume_file = base_directory / "assets" / "jeroen-resume.pdf"
portfolio_folder = base_directory / "assets" / "portfolio"
page_icon = base_directory / "assets" / "page_icon.ico"
project_folder = base_directory / "projects"


def cache_page_icon(page_icon):
    from PIL import Image

    return Image.open(page_icon)


im = cache_page_icon(page_icon)


def cache_css(css_file):
    with open(css_file) as f:
        return f.read()


def load_css():
    from st_pages import hide_pages, show_pages_from_config

    # hide_pages(["Thanks"])
    css_loaded = cache_css(css_file)
    st.markdown("<style>{}</style>".format(css_loaded), unsafe_allow_html=True)
    show_pages_from_config()
    return


def v_space(height):
    st.markdown(f"<div style='padding: {height}px;'></div>", unsafe_allow_html=True)
    # for _ in range(lines):
    # st.write("&nbsp;")


def text_loader(portfolio_folder, filename):
    with open(f"{portfolio_folder}/{filename}.md", "r") as f:
        loaded_text = f.read()
    return loaded_text


def title_header(title, title_class="title1", line=True):
    t = st.markdown(
        f"""
        <div class="{title_class}">{title}</div>
    """,
        unsafe_allow_html=True,
    )
    v_space(1)
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
        skills_html += "<div class='StyledHR StyledHRProjects'></div>"
        skills_html += "<br>"

        # skills_html += "<div class='StyledHR'></div>"
        skills_html += skill_score(skills)
        skills_html += '<div style="text-align: right;"><a class="click_link" href="https://www.jeroencvlier.com/Skills" target="_self">Click here for more details >></a></div>'
    elif level == "Languages":
        skills = skills[level]
        skills_html += f"<h2>Languages</h2>"
        skills_html += "<div class='StyledHR StyledHRProjects'></div>"
        skills_html += "<br>"
        # skills_html += "<div class='StyledHR'></div>"
        skills_html += skill_score(skills)
    elif level == "All Skills":
        skills = skills[level]
        for en, skill_section in enumerate(skills):
            if en != 0:
                skills_html += "<div class='StyledHR'></div>"
            skill_set = skills[skill_section]
            skills_html += f"<h3>{skill_section}</h3>"
            skills_html += skill_score(skill_set)
    return skills_html


def load_mp4(video_file_path):
    # Open the file
    import base64

    video_file = open(video_file_path, "rb")
    video_bytes = video_file.read()

    video_url = f"data:video/mp4;base64,{base64.b64encode(video_bytes).decode()}"

    html_code = f"""
    <video autoplay playsinline muted loop class="PortMarker gifContainer">
    <source src="{video_url}" type="video/mp4">
    </video>
    """
    return html_code


def load_png(image_file_path):
    # Open the image file
    import base64

    image_file = open(image_file_path, "rb")
    image_bytes = image_file.read()

    image_url = f"data:image/png;base64,{base64.b64encode(image_bytes).decode()}"

    html_code = f"""
    <img src="{image_url}" class="PortMarker pngContainer" />
    """
    return html_code


def project_buttons(project_link):
    """Add back button and code link button to the project page"""
    v_space(1)
    back_button = """
        <p><a href="https://www.jeroencvlier.com/Projects" target="_self">
            <button class='PortMarker homepageButton singleButton'><<< Back to project page</button>
        </a></p>
    """

    github_button = f"""
        <p><a href="{project_link}" target="_blank">
            <button class='PortMarker homepageButton singleButton'>Check out the code >>></button>
        </a></p>
    """

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(back_button, unsafe_allow_html=True)
    with col2:
        st.markdown(github_button, unsafe_allow_html=True)


def back_button(previous_page):
    """Provide a back button to the previous page"""
    if "home" in previous_page.lower():
        previous_page = ""
    previous_page = previous_page.capitalize()
    previous_page = previous_page.replace(" ", "%20")
    project_html = f"""
        <p><a href="https://www.jeroencvlier.com/{previous_page}" target="_self">
            <button class='PortMarker homepageButton singleButton'><<< Back to main page</button>
        </a></p>
    """
    st.markdown(project_html, unsafe_allow_html=True)
