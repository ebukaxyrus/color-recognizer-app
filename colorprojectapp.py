import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import ImageOps

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.gifer.com/13yx.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }

    /* Force all text to black for visibility */
    h1, h2, h3, h4, h5, h6, p, div, label, span {
        color: black !important;
        font-weight: bold;
    }

    /* Wrap main container in a readable card */
    div[data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.set_page_config(page_title="AI Color Recognizer", layout="centered")
st.title("🎨 AI Color Recognizer for Kids")
#st.write("Click on the image to find the name of the color!")

# Color dataset
# Load full color dataset

# Load and clean CSV
colors = pd.read_csv("cleaned_color.csv")

# Function to get closest color
def get_color_name(R, G, B):
    min_diff = float('inf')
    cname = ""
    for i in range(len(colors)):
        r_c, g_c, b_c = colors.loc[i, ["r", "g", "b"]]
        d = ((R - r_c) ** 2 + (G - g_c) ** 2 + (B - b_c) ** 2) ** 0.5
        if d < min_diff:
            min_diff = d
            cname = colors.loc[i, "color_name"]
    return cname


# Upload image
uploaded_file = st.file_uploader("UPLOAD YOUR FILE", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)

# Resize image if it's too big
    max_width = 400  # You can change this to 500, 400, etc.
    if img.width > max_width:
        scale = max_width / img.width
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size)

    img_array = np.array(img)
    
   
    # Display clickable image
    st.markdown("### 👇 Click on the image below:")
    coords = streamlit_image_coordinates(img, key="click")

    if coords is not None:
        x, y = coords["x"], coords["y"]
        st.write(f"You clicked at: ({x}, {y})")

        if y < img_array.shape[0] and x < img_array.shape[1]:
            pixel = img_array[y, x]
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel
            cname = get_color_name(r, g, b)

            st.markdown(f"### 🎯 Color Name: {cname}")
            st.markdown(f"**RGB:** ({r}, {g}, {b})")
            st.markdown(
                f"<div style='width:100px;height:50px;background-color:rgb({r},{g},{b});border:1px solid black;'></div>",
                unsafe_allow_html=True
            )
        else:
            st.warning("Click inside the image bounds.")
