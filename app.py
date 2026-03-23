import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="EcoEarn Demo", page_icon="🌿", layout="centered")

# -----------------------------
# Fixed demo account
# -----------------------------
APP_USERNAME = "groupb"
APP_PASSWORD = "ecoearn123"

# -----------------------------
# Session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "login_error" not in st.session_state:
    st.session_state.login_error = False

# Force Group B everywhere
st.session_state.user_name = "Group B"
st.session_state.member_id = "ECO-2026-001"
st.session_state.points = 420

if "news_items" not in st.session_state:
    st.session_state.news_items = [
        {"title": "New eco reward challenge launched", "date": "23 March 2026",
         "summary": "Users can now earn extra points by completing weekly sustainability challenges."},
        {"title": "Local partner shops added", "date": "21 March 2026",
         "summary": "More local businesses have joined the platform."},
        {"title": "Spring leaderboard update", "date": "18 March 2026",
         "summary": "Latest leaderboard is now live."}
    ]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"from": "EcoEarn Team", "date": "22 March 2026",
         "text": "Welcome back. Your account is active."},
        {"from": "Rewards Partner", "date": "20 March 2026",
         "text": "You are close to your next reward level."}
    ]

# -----------------------------
# Functions
# -----------------------------
def generate_qr_code(data):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def login(username, password):
    if username == APP_USERNAME and password == APP_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.login_error = False
    else:
        st.session_state.login_error = True

def logout():
    st.session_state.logged_in = False
    st.session_state.login_error = False

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
.block-container {max-width: 430px;}
.card {background: white; padding: 16px; border-radius: 16px;
       margin-bottom: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.05);}
.hero {background: #2f855a; color: white; padding: 18px;
       border-radius: 18px; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOGIN PAGE
# -----------------------------
if not st.session_state.logged_in:

    st.markdown("## EcoEarn")
    st.write("Login to access Group B demo")

    with st.form("login_form"):
        username = st.text_input("User name")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

    if submitted:
        login(username, password)
        st.experimental_rerun()

    if st.session_state.login_error:
        st.error("Incorrect login")

    st.caption("Login: groupb / ecoearn123")

# -----------------------------
# MAIN APP
# -----------------------------
else:

    st.sidebar.title("EcoEarn")
    page = st.sidebar.radio("", ["Home", "Profile", "News", "Messages"])
    st.sidebar.write("Group B")
    st.sidebar.write("Points: 420")

    if st.sidebar.button("Log out"):
        logout()
        st.experimental_rerun()

    # HOME
    if page == "Home":
        st.markdown("## EcoEarn")

        st.markdown(f"""
        <div class="hero">
        Welcome back<br>
        <b>Group B</b><br>
        {st.session_state.points} points
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        col1.metric("Points", st.session_state.points)
        col2.metric("Level", "Green")

        st.markdown('<div class="card">Next milestone: 500 points</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">Check Profile for QR</div>', unsafe_allow_html=True)

    # PROFILE
    elif page == "Profile":
        st.markdown("## Profile")

        st.write("Name: Group B")
        st.write("Member ID:", st.session_state.member_id)
        st.write("Points:", st.session_state.points)

        st.progress(st.session_state.points / 500)

        qr = generate_qr_code(f"Group B | {st.session_state.points}")
        st.image(qr, width=200)

    # NEWS
    elif page == "News":
        st.markdown("## News")

        for n in st.session_state.news_items:
            st.markdown(f"""
            <div class="card">
            <b>{n['title']}</b><br>
            {n['date']}<br>
            {n['summary']}
            </div>
            """, unsafe_allow_html=True)

    # MESSAGES
    elif page == "Messages":
        st.markdown("## Messages")

        for m in st.session_state.messages:
            st.markdown(f"""
            <div class="card">
            <b>{m['from']}</b><br>
            {m['date']}<br>
            {m['text']}
            </div>
            """, unsafe_allow_html=True)
