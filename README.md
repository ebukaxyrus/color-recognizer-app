# AI Color Recognizer for Kids

[![Live Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://color-recognizer-app.streamlit.app/) [![Portfolio](https://img.shields.io/badge/Portfolio-Xyrus-0B7786)](https://xyrusportfolio.netlify.app/)

> An interactive colour-learning application that lets a user upload an image, click a pixel, and see the nearest named colour from a local RGB colour dataset.

**Live demo:** https://color-recognizer-app.streamlit.app/  
**Project documentation and source:** https://github.com/ebukaxyrus/color-recognizer-app  
**Maintainer:** Dimakunne Chukwuebuka Francis

## At a glance

| Area | Details |
| --- | --- |
| Category | Image Processing / Education |
| Application framework | Streamlit |
| Entry point | `colorprojectapp.py` |
| Deployment | [Open live application](https://color-recognizer-app.streamlit.app/) |

## Application preview

[**Launch the live interactive application**](https://color-recognizer-app.streamlit.app/) to view its actual interface.

> Screenshot pending: No verified application screenshot file was available for documentation. Add an actual captured image at `docs/screenshots/app-preview.png` and replace this note with `![Application preview](docs/screenshots/app-preview.png)` after confirming it reflects the deployed interface. Do not use a mockup presented as a real screenshot.

## The problem and approach

An interactive colour-learning application that lets a user upload an image, click a pixel, and see the nearest named colour from a local RGB colour dataset.

The selected RGB vector `(R,G,B)` is compared with each colour-row RGB vector `(r,g,b)` in the CSV. The minimum of `sqrt((R-r)^2+(G-g)^2+(B-b)^2)` determines the displayed label. This is **nearest-reference colour matching**, not a trained ML classifier.

## Features

- Upload JPG, JPEG or PNG images.
- Resize images wider than 400 pixels before interaction.
- Click an image to read the selected pixel's RGB values.
- Match the pixel to a name in `cleaned_color.csv` using minimum Euclidean RGB distance.
- Show a visual colour swatch and a browser-powered **Speak Color** button.

## Technology stack

- Python
- Streamlit
- Pillow (PIL)
- Pandas
- NumPy
- streamlit-image-coordinates
- Browser Speech Synthesis API

## Repository structure

- `colorprojectapp.py` — Streamlit UI, pixel selection, matching logic and speech button.
- `cleaned_color.csv` — local reference table containing RGB entries and colour names.
- `requirements.txt` — Python dependencies.
- `colorapp.ipynb` — related notebook; inspect separately before relying on its results.

## Run locally

Prerequisites: Python 3.10+ is a reasonable starting environment, but no fixed compatibility matrix has been independently tested. Check the dependency versions actually available for your environment.

```bash
git clone https://github.com/ebukaxyrus/color-recognizer-app.git
cd color-recognizer-app
python -m venv .venv
```

Activate the environment:

```bash
# macOS or Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\\Scripts\\Activate.ps1
```

Install packages and start the app:

```bash
python -m pip install -r requirements.txt
streamlit run colorprojectapp.py
```

Run from the repository root so the app can find its local data/assets. Where the app uses text-to-speech or browser capabilities, allow the relevant permissions.

## How to use

1. Open the application.
2. Upload a supported image.
3. Click a point on the displayed picture.
4. Read its RGB triplet, matched colour label and colour swatch.
5. Optionally use **Speak Color**, subject to browser audio support.

## Limitations and responsible use

- Recognized names depend entirely on the reference dataset and RGB lighting/colour conditions.
- The original image may be resized; displayed coordinate values relate to the resized image.
- The speech button relies on the user's browser speech-synthesis support.
- A screenshot is intentionally not embedded because no verified local screenshot asset is available in the repository.
- Review accessibility, error handling for non-RGB images, and performance on large datasets.

## Quality and future improvements

- [ ] Test a clean installation and pin compatible dependency versions.
- [ ] Add real screenshots, alt text and demonstration media.
- [ ] Add automated tests for primary use cases and invalid input.
- [ ] Review accessibility, error handling and mobile usability.
- [ ] Verify datasets, licenses, user privacy, and live deployment behavior.

## Maintainer and links

**Dimakunne Chukwuebuka Francis**  
Head of Data & Artificial Intelligence, Schoolville ICT Hub  
Founder, XY AI Solution

- [Professional portfolio](https://xyrusportfolio.netlify.app/)
- [GitHub profile](https://github.com/ebukaxyrus)
- [XY AI Solution](https://xyaisolution.online/)

**Documentation scope:** Written from repository source inspection; successful clean-environment installation and end-to-end live application behavior have not been independently verified.
