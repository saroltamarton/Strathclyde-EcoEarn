import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="EcoEarn Demo", page_icon="🌿", layout="centered")

# -----------------------------
# Force fixed user details
# -----------------------------
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
# QR code generator
# -----------------------------
def generate_qr_code(data: str):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


# -----------------------------
# App styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #eef7f1 0%, #ffffff 35%);
    }

    .block-container {
        max-width: 430px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #163a2f;
    }

    .app-title {
        font-size: 2rem;
        font-weight: 700;
        color: #163a2f;
        margin-bottom: 0.2rem;
    }

    .app-subtitle {
        color: #4f6f64;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }

    .card {
        background: white;
        border-radius: 18px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border: 1px solid #edf2ef;
    }

    .hero-card {
        background: linear-gradient(135deg, #1f7a5a 0%, #38a169 100%);
        color: white;
        border-radius: 22px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 18px rgba(31,122,90,0.18);
    }

    .hero-small {
        font-size: 0.9rem;
        opacity: 0.95;
        margin-bottom: 0.35rem;
    }

    .hero-points {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .label {
        font-size: 0.82rem;
        color: #6c7f77;
        margin-bottom: 0.15rem;
    }

    .value {
        font-size: 1.05rem;
        color: #163a2f;
        font-weight: 600;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        color: #163a2f;
        margin-top: 0.5rem;
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
        margin-bottom: 0.55rem;
    }

    .news-text {
        font-size: 0.95rem;
        color: #2c433a;
        line-height: 1.5;
    }

    .pill {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: #e8f6ee;
        color: #1f7a5a;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.45rem;
    }

    div[data-testid="stSidebar"] {
        background: #f5fbf7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.markdown("## EcoEarn")
page = st.sidebar.radio("", ["Home", "Profile", "News", "Messages"])
st.sidebar.markdown("---")
st.sidebar.write("Signed in as: Group B")
st.sidebar.write("Points: 420")


# -----------------------------
# Home page
# -----------------------------
if page == "Home":
    st.markdown('<div class="app-title">EcoEarn</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">A simple rewards app demo for Group B</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-small">Welcome back</div>
            <div style="font-size:1.2rem; font-weight:600;">Group B</div>
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
                <div class="pill">Active member</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="label">QR access</div>
                <div class="value">Ready to scan</div>
                <div class="pill">Profile page</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Quick overview</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <div class="label">Latest update</div>
            <div class="value">New eco challenge available</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <div class="label">Next milestone</div>
            <div class="value">500 points reward target</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <div class="label">What to check next</div>
            <div class="value">Visit your Profile and News pages</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Profile page
# -----------------------------
elif page == "Profile":
    st.markdown('<div class="app-title">Your Profile</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Personal account details for Group B</div>',
        unsafe_allow_html=True
    )

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
    st.image(qr_image, width=230)
    st.caption("Scan this QR code to view member details")
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# News page
# -----------------------------
elif page == "News":
    st.markdown('<div class="app-title">Latest News</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Recent updates from EcoEarn</div>',
        unsafe_allow_html=True
    )

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


# -----------------------------
# Messages page
# -----------------------------
elif page == "Messages":
    st.markdown('<div class="app-title">Messages</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Account messages for Group B</div>',
        unsafe_allow_html=True
    )

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
