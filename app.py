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

if "page" not in st.session_state:
    st.session_state.page = "Home"

# Force Group B everywhere
st.session_state.user_name = "Group B"
st.session_state.member_id = "ECO-2026-001"
st.session_state.points = 420

if "news_items" not in st.session_state:
    st.session_state.news_items = [
        {
            "title": "New eco reward challenge launched",
            "date": "23 March 2026",
            "summary": "Users can now earn extra points by completing weekly sustainability challenges."
        },
        {
            "title": "Local partner shops added",
            "date": "21 March 2026",
            "summary": "More local businesses have joined the platform, giving users more ways to earn and use points."
        },
        {
            "title": "Spring leaderboard update",
            "date": "18 March 2026",
            "summary": "The latest leaderboard is now live, showing the top users by reward points earned this month."
        }
    ]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "from": "EcoEarn Team",
            "date": "22 March 2026",
            "text": "Welcome back. Your account is active and ready to use."
        },
        {
            "from": "Local Rewards Partner",
            "date": "20 March 2026",
            "text": "You are close to your next reward level. Keep collecting points."
        }
    ]


# -----------------------------
# Helper functions
# -----------------------------
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
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
        st.session_state.page = "Home"
    else:
        st.session_state.logged_in = False
        st.session_state.login_error = True


def logout():
    st.session_state.logged_in = False
    st.session_state.login_error = False
    st.session_state.page = "Home"


def go_to(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()


# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: linear-gradient(180deg, #eef7f1 0%, #ffffff 40%);
    }

    .block-container {
        max-width: 440px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    .phone-shell {
        background: #ffffff;
        border-radius: 28px;
        padding: 16px 16px 20px 16px;
        box-shadow: 0 10px 28px rgba(0,0,0,0.08);
        border: 1px solid #ebf2ee;
    }

    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }

    .brand {
        font-size: 1.6rem;
        font-weight: 700;
        color: #163a2f;
        margin: 0;
    }

    .brand-sub {
        color: #678076;
        font-size: 0.9rem;
        margin-top: 2px;
        margin-bottom: 0;
    }

    .hero-card {
        background: linear-gradient(135deg, #1f7a5a 0%, #38a169 100%);
        color: white;
        border-radius: 22px;
        padding: 20px;
        margin-top: 8px;
        margin-bottom: 14px;
        box-shadow: 0 8px 18px rgba(31,122,90,0.16);
    }

    .hero-small {
        font-size: 0.9rem;
        opacity: 0.95;
        margin-bottom: 0.2rem;
    }

    .hero-name {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .hero-points {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .card {
        background: white;
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        border: 1px solid #edf2ef;
    }

    .label {
        font-size: 0.82rem;
        color: #6d7f77;
        margin-bottom: 0.15rem;
    }

    .value {
        font-size: 1.02rem;
        color: #163a2f;
        font-weight: 600;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        color: #163a2f;
        margin-top: 0.3rem;
        margin-bottom: 0.7rem;
    }

    .news-title {
        font-size: 1rem;
        font-weight: 700;
        color: #163a2f;
        margin-bottom: 0.2rem;
    }

    .news-date {
        font-size: 0.8rem;
        color: #6f7d76;
        margin-bottom: 0.5rem;
    }

    .news-text {
        font-size: 0.94rem;
        color: #2d433b;
        line-height: 1.5;
    }

    .login-wrap {
        background: white;
        border-radius: 28px;
        padding: 28px 22px;
        margin-top: 40px;
        box-shadow: 0 10px 26px rgba(0,0,0,0.08);
        border: 1px solid #ebf2ee;
    }

    .login-title {
        font-size: 2rem;
        font-weight: 700;
        color: #163a2f;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    .login-subtitle {
        color: #5f756c;
        text-align: center;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }

    .helper-text {
        text-align: center;
        color: #71847b;
        font-size: 0.85rem;
        margin-top: 0.8rem;
    }

    .stButton > button {
        border-radius: 14px;
        height: 2.8rem;
    }

    .nav-space {
        margin-top: 0.3rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Login page
# -----------------------------
if not st.session_state.logged_in:
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">EcoEarn</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="login-subtitle">Sign in to access the Group B demo account</div>',
        unsafe_allow_html=True
    )

    with st.form("login_form"):
        username = st.text_input("User name")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

    if submitted:
        login(username, password)
        st.experimental_rerun()

    if st.session_state.login_error:
        st.error("Incorrect user name or password")

    st.markdown(
        '<div class="helper-text">Demo login: groupb / ecoearn123</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Main app
# -----------------------------
else:
    st.markdown('<div class="phone-shell">', unsafe_allow_html=True)

    top_left, top_right = st.columns([3, 1])
    with top_left:
        st.markdown('<div class="brand">EcoEarn</div>', unsafe_allow_html=True)
        st.markdown('<p class="brand-sub">Rewards app demo for Group B</p>', unsafe_allow_html=True)
    with top_right:
        if st.button("Log out"):
            logout()
            st.experimental_rerun()

    st.markdown('<div class="nav-space"></div>', unsafe_allow_html=True)
    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:
        if st.button("Home"):
            go_to("Home")
    with nav2:
        if st.button("Profile"):
            go_to("Profile")
    with nav3:
        if st.button("News"):
            go_to("News")
    with nav4:
        if st.button("Messages"):
            go_to("Messages")

    page = st.session_state.page

    if page == "Home":
        st.markdown(
            f"""
            <div class="hero-card">
                <div class="hero-small">Welcome back</div>
                <div class="hero-name">Group B</div>
                <p class="hero-points">{st.session_state.points} points</p>
                <div class="hero-small">Your account is active and ready to use</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="card">
                    <div class="label">Member level</div>
                    <div class="value">Green</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="card">
                    <div class="label">Next target</div>
                    <div class="value">500 points</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="section-title">Quick overview</div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="card">
                <div class="label">QR access</div>
                <div class="value">Ready on the Profile page</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <div class="label">Latest update</div>
                <div class="value">New eco reward challenge available</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <div class="label">Messages</div>
                <div class="value">2 unread demo messages</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif page == "Profile":
        st.markdown('<div class="section-title">Your Profile</div>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="card">
                <div class="label">Name</div>
                <div class="value">Group B</div>
                <br>
                <div class="label">Member ID</div>
                <div class="value">{st.session_state.member_id}</div>
                <br>
                <div class="label">Points earned</div>
                <div class="value">{st.session_state.points}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">Reward progress</div>', unsafe_allow_html=True)
        st.progress(min(st.session_state.points / 500, 1.0))
        st.caption("Progress towards 500 points")

        qr_data = (
            f"Name: Group B\n"
            f"Member ID: {st.session_state.member_id}\n"
            f"Points: {st.session_state.points}"
        )
        qr_image = generate_qr_code(qr_data)

        st.markdown('<div class="section-title">Personal QR code</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(qr_image, width=220)
        st.caption("Scan this QR code to view member details")
        st.markdown('</div>', unsafe_allow_html=True)

    elif page == "News":
        st.markdown('<div class="section-title">Latest News</div>', unsafe_allow_html=True)

        for item in st.session_state.news_items:
            st.markdown(
                f"""
                <div class="card">
                    <div class="news-title">{item["title"]}</div>
                    <div class="news-date">{item["date"]}</div>
                    <div class="news-text">{item["summary"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    elif page == "Messages":
        st.markdown('<div class="section-title">Messages</div>', unsafe_allow_html=True)

        for msg in st.session_state.messages:
            st.markdown(
                f"""
                <div class="card">
                    <div class="news-title">{msg["from"]}</div>
                    <div class="news-date">{msg["date"]}</div>
                    <div class="news-text">{msg["text"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
