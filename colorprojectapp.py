import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_image_coordinates import streamlit_image_coordinates


GA_MEASUREMENT_ID = "G-JRZNTB02YQ"


st.components.v1.html(f"""
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>
""", height=0, width=0)

# Page style
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
    h1, h2, h3, h4, h5, h6, p, div, label, span {
        color: black !important;
        font-weight: bold;
    }
    div[data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 2rem;
        border-radius: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .stFileUploader > label > div {
        color: white !important;
        font-weight: bold;
    }
    .stFileUploader div[data-testid="stFileDropzone"] {
        background-color: rgba(0, 0, 0, 0.6);
        border: 2px dashed #ffffff;
        border-radius: 12px;
        padding: 1rem;
        color: white !important;
    }
    .stFileUploader div[data-testid="stFileDropzone"] * {
        color: white !important;
        font-weight: bold;
    }
    .stFileUploader button {
        color: black !important;
        background-color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page settings
st.set_page_config(page_title="AI Color Recognizer", layout="centered")
st.title("🎨 AI Color Recognizer for Kids")

# Load color dataset
colors = pd.read_csv("cleaned_color.csv")

# Color matching function
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
    max_width = 400
    if img.width > max_width:
        scale = max_width / img.width
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size)

    img_array = np.array(img)

    st.markdown("### 👇 Click on the image below:")
    coords = streamlit_image_coordinates(img, key="click")

    if coords is not None:
        x, y = coords["x"], coords["y"]
        st.write(f"You clicked at: ({x}, {y})")

        if y < img_array.shape[0] and x < img_array.shape[1]:
            pixel = img_array[y, x]
            r, g, b = pixel[:3]
            cname = get_color_name(r, g, b)

            st.markdown(f"### 🎯 Color Name: {cname}")
            st.markdown(f"**RGB:** ({r}, {g}, {b})")

            # Color display box
            st.markdown(
                f"<div style='width:100px;height:50px;background-color:rgb({r},{g},{b});border:1px solid black;'></div>",
                unsafe_allow_html=True
            )

            # Speak button
            import streamlit.components.v1 as components
            components.html(
                f"""
    		<button onclick="speakColor()" style="padding:10px 20px; font-size:16px; border-radius:8px;">🔊 Speak Color</button>
    		<script>
    		function speakColor() {{
        	    const msg = new SpeechSynthesisUtterance("{cname}");
        	    msg.lang = "en-US";
                    msg.pitch = 1.1;
                    msg.rate = 1;
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(msg);
    		}}
    		</script>
    		""",
    		height=100,
	    )

        else:
            st.warning("Click inside the image bounds.")
