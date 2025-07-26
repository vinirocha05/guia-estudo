import os
from dotenv import load_dotenv
import streamlit as st


def get_secret(key):
    """
    Get a secret from Streamlit or fallback to .env for local development.

    This allows the app to run both on Streamlit Cloud and locally.
    """
    try:
        return st.secrets[key]
    except Exception:
        load_dotenv()
        return os.getenv(key)


from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    video_id = video_url.split("v=")[1].split("&")[0]

    ytt_api = YouTubeTranscriptApi()
    s = ytt_api.fetch(video_id, languages=['pt','en'])
    text = ''
    for frase in s:
        text +=frase.text
    return text