import streamlit as st
import pandas as pd
import os

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Social Media Analytics Manager",
    page_icon="📊",
    layout="wide"
)

FILE_NAME = "data.xlsx"

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

st.subheader("📱 Social Media Statistics")

platforms = ["Twitter", "Instagram", "Facebook", "TikTok"]

record = {
    "Employee Name": employee_name
}

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

    record[f"{platform} Posts"] = posts
    record[f"{platform} Views"] = views

st.divider()

# ----------------------------
# Submit
# ----------------------------
if st.button("📤 Submit Report", use_container_width=True):

    if employee_name.strip() == "":
        st.error("Please enter employee name.")

    else:

        new_df = pd.DataFrame([record])

        if os.path.exists(FILE_NAME):
            old_df = pd.read_excel(FILE_NAME)
            final_df = pd.concat([old_df, new_df], ignore_index=True)
        else:
            final_df = new_df

        final_df.to_excel(FILE_NAME, index=False)

        st.success("✅ Report saved successfully!")

        st.balloons()

        st.dataframe(final_df)
