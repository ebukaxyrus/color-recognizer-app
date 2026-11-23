# Interactive Image Color Recognizer

An educational color-recognition web app that matches image pixels with named colors.

## Technology stack
- Python
- Streamlit
- Pillow
- Pandas
- NumPy
- streamlit-image-coordinates

## Confirmed functionality
- Uploads an image
- selects pixel coordinates
- matches RGB values to cleaned_color.csv using Euclidean distance.

## Repository entry point

- `colorprojectapp.py`: primary inspected Streamlit application.

## Run locally

```bash
git clone https://github.com/ebukaxyrus/color-recognizer-app.git
cd color-recognizer-app
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run colorprojectapp.py
```


## Limitations and responsible use

This is reference-dataset-based nearest-color matching, not a trained ML classifier.

## Documentation and quality checklist

- [ ] Verify clean-environment installation.
- [ ] Add authentic screenshots and demonstration links.
- [ ] Add input/error-handling tests.
- [ ] Check data provenance, licensing and accessibility.

## Author

**Dimakunne Chukwuebuka Francis** · [GitHub](https://github.com/ebukaxyrus) · [Portfolio](https://xyrusportfolio.netlify.app/) · [XY AI Solution](https://xyaisolution.online/)

*Source-reviewed documentation. End-to-end deployment has not been independently verified.*
