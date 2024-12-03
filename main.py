import streamlit as st
from moviepy.editor import VideoFileClip

def extract_audio(video_file):
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(video_file.read())
        temp_file_path = temp_file.name
    video = VideoFileClip(temp_file_path)
    audio = video.audio
    audio_file = "extracted_audio.mp3"
    audio.write_audiofile(audio_file)
    return audio_file

st.title("Video to Audio Extractor")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file:
    st.video(uploaded_file)

if uploaded_file:
    with st.spinner('Extracting audio...'):
        audio_file = extract_audio(uploaded_file)
        st.success('Audio extracted successfully!')
        st.audio(audio_file)
        with open(audio_file, "rb") as file:
            btn = st.download_button(
                label="Download Audio",
                data=file,
                file_name=audio_file,
                mime="audio/mp3"
            )