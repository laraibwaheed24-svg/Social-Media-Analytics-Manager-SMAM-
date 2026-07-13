import streamlit as st

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="SocialTrack Pro",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# Header
# -------------------------
st.title("📊 SocialTrack Pro")
st.subheader("Social Media Reporting & Analytics System")

st.markdown("---")

st.write("""
Welcome to **SocialTrack Pro**.

This application allows employees to submit their social media performance data while automatically generating reports and analytics for management.

### Supported Platforms
- Twitter (X)
- Instagram
- Facebook
- TikTok

### Coming Soon
- Employee Data Entry
- Excel Report Generation
- Dashboard Analytics
- AI Performance Insights
- Charts & Visual Reports
""")

st.success("🚀 Project initialized successfully!")
