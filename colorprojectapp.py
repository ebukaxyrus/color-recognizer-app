import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Color Recognizer", layout="centered")

st.title("🎨 AI Color Recognizer for Kids")
st.write("Upload an image and click to get the closest color name!")

# Upload image
uploaded_file = st.file_uploader("wallhaven-jx632y.jpg", type=["jpg", "jpeg", "png"])

# Color dataset
colors = pd.DataFrame({
    'color_name': ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Gray', 'Orange', 'Purple'],
    'R': [255, 0, 0, 255, 0, 255, 128, 255, 128],
    'G': [0, 255, 0, 255, 0, 255, 128, 165, 0],
    'B': [0, 0, 255, 0, 0, 255, 128, 0, 128]
})

# Function to find closest color
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
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    st.image(img, caption="Uploaded Image", use_column_width=True)

    st.markdown("### 🔍 Pick a pixel coordinate to detect the color:")

    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input("X (horizontal)", min_value=0, max_value=img.width - 1, value=50)
    with col2:
        y = st.number_input("Y (vertical)", min_value=0, max_value=img.height - 1, value=50)

    if st.button("Detect Color"):
        pixel = img_array[int(y), int(x)]
        if len(pixel) == 4:  # RGBA image
            r, g, b, _ = pixel
        else:
            r, g, b = pixel
        cname = get_color_name(r, g, b)

        st.markdown(f"### 🎯 Coordinates: ({x}, {y})")
        st.markdown(f"**Detected Color:** {cname}")
        st.markdown(f"**RGB:** ({r}, {g}, {b})")

        st.markdown(
            f"<div style='width:100px;height:50px;background-color:rgb({r},{g},{b});border:1px solid black;'></div>",
            unsafe_allow_html=True
        )
