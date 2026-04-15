# ClientWell Auto-Fill Report Generator

## Files
- `clientwell_generator.py` - cleaned report generation engine
- `streamlit_app.py` - Streamlit interface
- `test_samples.py` - 10 sample combination validation script

## Run locally
```bash
pip install streamlit
streamlit run streamlit_app.py
```

## What it does
- Repairs the generator into a runnable Python file
- Wraps it in a simple Streamlit interface
- Includes 10 sample domain combinations for testing
- Adds section-specific outputs for:
  - assessment
  - medical necessity
  - treatment plan
  - BIRP
  - risk summary
- Adds text export for each section and the full report
