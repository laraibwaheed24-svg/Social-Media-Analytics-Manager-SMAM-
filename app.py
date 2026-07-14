import streamlit as st
import pandas as pd
import os

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="SocialTrack Pro",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "",
    [
        "📝 Data Entry",
        "📊 Dashboard",
        "🏆 Employee Leaderboard"
    ]
)

FILE_NAME = "data.xlsx"

# ----------------------------
# Data Entry Page
# ----------------------------

if page == "📝 Data Entry":

    st.title("📊 SocialTrack Pro")
    st.caption("### Automating Social Media Reporting & Analytics")

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



elif page == "📊 Dashboard":

    st.title("📊 Dashboard")
    st.caption("Overview of Social Media Performance")

    if os.path.exists(FILE_NAME):

        df = pd.read_excel(FILE_NAME)

    

    if os.path.exists(FILE_NAME):

        df = pd.read_excel(FILE_NAME)

        twitter_posts = df["Twitter Posts"].sum()
        twitter_views = df["Twitter Views"].sum()

        instagram_posts = df["Instagram Posts"].sum()
        instagram_views = df["Instagram Views"].sum()

        facebook_posts = df["Facebook Posts"].sum()
        facebook_views = df["Facebook Views"].sum()

        tiktok_posts = df["TikTok Posts"].sum()
        tiktok_views = df["TikTok Views"].sum()

        total_posts = (
            twitter_posts +
            instagram_posts +
            facebook_posts +
            tiktok_posts
        )

        total_views = (
            twitter_views +
            instagram_views +
            facebook_views +
            tiktok_views
        )

        platform_views = {
            "Twitter": twitter_views,
            "Instagram": instagram_views,
            "Facebook": facebook_views,
            "TikTok": tiktok_views
        }

        best_platform = max(platform_views, key=platform_views.get)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📝 Total Posts", total_posts)

        with col2:
            st.metric("👁️ Total Views", f"{total_views:,}")

        with col3:
            st.metric("👥 Employees", len(df))

        with col4:
            st.metric("🏆 Best Platform", best_platform)

        st.divider()

        summary = pd.DataFrame({

            "Platform": [
                "Twitter",
                "Instagram",
                "Facebook",
                "TikTok"
            ],

            "Posts": [
                twitter_posts,
                instagram_posts,
                facebook_posts,
                tiktok_posts
            ],

           "Views": [
               twitter_views,
               instagram_views,
               facebook_views,
               tiktok_views
            ]
        })

        st.subheader("📊 Platform Summary")

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("📋 Employee Records")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

 elif page == "🏆 Employee Leaderboard":

        st.title("🏆 Employee Leaderboard")
        st.caption("Top Performing Employees")

    if os.path.exists(FILE_NAME):

        df = pd.read_excel(FILE_NAME)

    else:

        st.warning("No employee records found.")
        st.stop()

    df["Total Posts"] = (
        df["Twitter Posts"] +
        df["Instagram Posts"] +
        df["Facebook Posts"] +
        df["TikTok Posts"]
    )

    df["Total Views"] = (
        df["Twitter Views"] +
        df["Instagram Views"] +
        df["Facebook Views"] +
        df["TikTok Views"]
    )
    leaderboard = df.sort_values(
        by="Total Views",
        ascending=False
    ).reset_index(drop=True)
    
    st.subheader("🏅 Top Performers")

    medals = ["🥇", "🥈", "🥉"]

    for i, row in leaderboard.iterrows():

        if i < 3:
            medal = medals[i]
        else:
            medal = f"#{i+1}"

        st.markdown(f"## {medal} {row['Employee Name']}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📝 Total Posts", int(row["Total Posts"]))

        with col2:
            st.metric("👁️ Total Views", f"{int(row['Total Views']):,}")

        st.divider()
    

    else:

        st.warning("No reports found.")
