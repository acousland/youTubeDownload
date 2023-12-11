import streamlit as st
from YTdownload import download_video

st.title("YouTube Video Downloader")

# Input box for URL
url = st.text_input("Enter the URL of the video to download")

# Button to trigger download
if st.button("Download"):
    download_video(url)
    st.success("Video downloaded successfully!")
