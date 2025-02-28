import streamlit as st
import os
import random
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def classify_image():
    return random.choice(["Fresh", "Slightly Rotten", "Rotten"])

def get_usage_tips(category):
    info = {
        "Fresh": "✅ Perfect for eating raw, cooking, or preserving. High in nutrients!",
        "Slightly Rotten": "⚠️ Can be used in smoothies, jams, or baking. Remove spoiled parts before use. Helps reduce food waste!",
        "Rotten": "❌ Unsafe for consumption. Consider composting, using for biofuel, or animal feed to support environmental sustainability."
    }
    return info.get(category, "No information available.")

# Set background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('img/background.png');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍎 Food Freshness Classifier 🥦")

uploaded_files = st.file_uploader("Upload Images or Folders", type=["jpg", "png", "jpeg", "webp"], accept_multiple_files=True, label_visibility='visible', help='You can upload multiple images or an entire folder.')

classification_counts = {"Fresh": 0, "Slightly Rotten": 0, "Rotten": 0}

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        classification = classify_image()
        classification_counts[classification] += 1
        usage_tips = get_usage_tips(classification)
        results.append((uploaded_file.name, classification, usage_tips, image))
    
    for file_name, classification, usage_tips, image in results:
        st.image(image, caption=f"{file_name} - Classified as {classification}", use_container_width=True)
        st.write(f"**Usage Tips:** {usage_tips}")
        st.markdown("---")

    # Visualization - Pie Chart
    st.sidebar.header("Food Classification Distribution")
    fig, ax = plt.subplots()
    labels = classification_counts.keys()
    sizes = classification_counts.values()
    colors = ['green', 'orange', 'red']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.sidebar.pyplot(fig)

    # Bar Graph - Uploaded Images Distribution
    st.header("📊 Image Classification Summary")
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(labels, sizes, color=colors)
    ax_bar.set_xlabel("Classification")
    ax_bar.set_ylabel("Number of Images")
    ax_bar.set_title("Food Classification Bar Chart")
    st.pyplot(fig_bar)

st.sidebar.header("About the Classification")
st.sidebar.write("This classification is randomly generated and provides general tips on how to handle fresh, slightly rotten, and rotten food items. Future improvements may include an AI-based classifier.")
