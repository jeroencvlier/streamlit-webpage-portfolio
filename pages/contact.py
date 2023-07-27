import streamlit as st
from pathlib import Path
from st_pages import (
    show_pages_from_config,
    add_page_title,
    hide_pages,
    Page,
    show_pages,
)

show_pages_from_config()
hide_pages(["thanks"])

domain = "https://www.jeroencvlier.com/thanks"


st.title("Contact Form")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
parent_dir = current_dir.parent
css_file = parent_dir / "styles" / "main.css"


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/
    contact_form = f"""
    <form action="https://formsubmit.co/jurists-plywood-0b@icloud.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        <input type="hidden" name="_next" value="{domain}">
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
