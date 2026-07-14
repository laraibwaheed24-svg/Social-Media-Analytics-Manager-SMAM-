import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Social Media Analytics Manager",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------
st.title("📊 Social Media Analytics Manager (SMAM)")
st.caption("Automating Social Media Reporting & Analytics")

st.divider()

# ----------------------------
# Employee Information
# ----------------------------
st.subheader("👤 Employee Information")

employee_name = st.text_input(
    "Employee Name",
    placeholder="Enter employee name"
)

st.divider()

# ----------------------------
# Social Media Statistics
# ----------------------------
st.subheader("📱 Social Media Statistics")

platforms = ["Twitter", "Instagram", "Facebook", "TikTok"]

data = {}

for platform in platforms:

    st.markdown(f"### {platform}")

    col1, col2 = st.columns(2)

    with col1:
        posts = st.number_input(
            f"{platform} Posts",
            min_value=0,
            step=1,
            key=f"{platform}_posts"
        )

    with col2:
        views = st.number_input(
            f"{platform} Views",
            min_value=0,
            step=1,
            key=f"{platform}_views"
        )

    data[platform] = {
        "Posts": posts,
        "Views": views
    }

st.divider()

# ----------------------------
# Submit Button
# ----------------------------
if st.button("📤 Submit Report", use_container_width=True):

    if employee_name.strip() == "":
        st.error("Please enter the employee name.")

    else:

        st.success("Report submitted successfully!")

        st.write("### Preview")

        st.write(f"**Employee:** {employee_name}")

        st.json(data)
