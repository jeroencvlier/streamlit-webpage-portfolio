from pages.utils import *

load_css()


title_header("Contact Form")
domain = "https://www.jeroencvlier.com/Thanks"


# ---- CONTACT ----
with st.container():
    st.markdown(
        "<h1 style='text-align: center; color: white;'>Get In Touch With Me!</h1>",
        unsafe_allow_html=True,
    )
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

    left_column, email_column, right_column = st.columns([0.1, 0.8, 0.1])
    with email_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        st.empty()
    with right_column:
        st.empty()
