import streamlit as st
import pandas as pd
import cv2
from PIL import Image
import numpy as np

st.set_page_config(page_title="AI Color Recognizer", layout="centered")

st.title("🎨 AI Color Recognizer for Kids")
st.write("Upload an image and click to see the closest color name!")

# Upload image
uploaded_file = st.file_uploader("wallhaven-jx632y.jpg", type=["jpg", "jpeg", "png"])

# Color dataset
colors = pd.DataFrame({
    'color_name': ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Gray', 'Orange', 'Purple'],
    'R': [255, 0, 0, 255, 0, 255, 128, 255, 128],
    'G': [0, 255, 0, 255, 0, 255, 128, 165, 0],
    'B': [0, 0, 255, 0, 0, 255, 128, 0, 128]
})

# Match color function
def get_color_name(R, G, B):
    min_diff = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - colors.loc[i, "R"]) + abs(G - colors.loc[i, "G"]) + abs(B - colors.loc[i, "B"])
        if d < min_diff:
            min_diff = d
            cname = colors.loc[i, "color_name"]
    return cname

if uploaded_file:
    # Load image
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    st.image(img_array, caption="Click below to select a pixel.", use_column_width=True)

    st.markdown("### 🔍 Pick a pixel coordinate")

    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input("X (horizontal)", min_value=0, max_value=img_array.shape[1]-1, value=50)
    with col2:
        y = st.number_input("Y (vertical)", min_value=0, max_value=img_array.shape[0]-1, value=50)

    if st.button("Detect Color"):
        r, g, b = img_array[int(y), int(x)][:3]
        color_name = get_color_name(r, g, b)

        st.markdown(f"### 🎯 Result at ({x}, {y})")
        st.markdown(f"**Color name:** {color_name}")
        st.markdown(f"**RGB:** ({r}, {g}, {b})")

        st.markdown(
            f"<div style='width:100px;height:50px;background-color:rgb({r},{g},{b});border:1px solid black;'></div>",
            unsafe_allow_html=True
        )
