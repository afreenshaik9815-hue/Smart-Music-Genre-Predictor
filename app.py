import streamlit as st
import numpy as np

st.title("🎵 Music Genre Classifier")

file = st.file_uploader("Upload Audio File", type=["wav"])

if file is not None:
    st.audio(file)

    # Dummy feature (no librosa)
    features = np.random.rand(10)

    genre = "Pop"

    st.success(f"🎶 Predicted Genre: {genre}")