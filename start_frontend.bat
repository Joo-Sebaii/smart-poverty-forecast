@echo off
echo Starting Frontend Application...
cd frontend
python -m pip install -r requirements.txt
streamlit run app.py
pause

