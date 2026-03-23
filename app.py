import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="EcoEarn Demo", page_icon="🌿", layout="centered")

# -----------------------------------
# Demo user data
# -----------------------------------
if "user_name" not in st.session_state:
    st.session_state.user_name = "Gizella Marton"

if "member_id" not in st.session_state:
    st.session_state.member_id = "ECO-2026-001"

if "points" not in st.session_state:
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

# -----------------------------------
# QR code generator
# -----------------------------------
def generate_qr_code(data: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# -----------------------------------
# Sidebar navigation
# -----------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Profile", "News"])

st.sidebar.markdown("---")
st.sidebar.write(f"Signed in as: {st.session_state.user_name}")
st.sidebar.write(f"Points: {st.session_state.points}")

# -----------------------------------
# Home page
# -----------------------------------
if page == "Home":
    st.title("EcoEarn")
    st.subheader("Welcome back")

    st.write(
        "EcoEarn is a simple rewards app demo. Users can track their points, view their personal QR code, "
        "and check the latest news and updates."
    )

    col1, col2 = st.columns(2)
    col1.metric("Points earned", st.session_state.points)
    col2.metric("Member level", "Green")

    st.markdown("---")
    st.write("Quick overview")

    with st.container():
        st.info("You have earned 420 points so far.")
        st.success("Your profile QR code is ready to scan on the Profile page.")
        st.write("Visit the News page to see the latest updates.")

# -----------------------------------
# Profile page
# -----------------------------------
elif page == "Profile":
    st.title("Your Profile")

    st.write(f"Name: {st.session_state.user_name}")
    st.write(f"Member ID: {st.session_state.member_id}")
    st.write(f"Points earned: {st.session_state.points}")

    st.progress(min(st.session_state.points / 500, 1.0))
    st.caption("Progress towards 500 points")

    qr_data = (
        f"Name: {st.session_state.user_name}\n"
        f"Member ID: {st.session_state.member_id}\n"
        f"Points: {st.session_state.points}"
    )
    qr_image = generate_qr_code(qr_data)

    st.markdown("---")
    st.subheader("Personal QR code")
    st.image(qr_image, caption="Scan this QR code to view member details", width=250)

# -----------------------------------
# News page
# -----------------------------------
elif page == "News":
    st.title("Latest News")

    for item in st.session_state.news_items:
        with st.container():
            st.subheader(item["title"])
            st.caption(item["date"])
            st.write(item["summary"])
            st.markdown("---")
