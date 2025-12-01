@echo off
echo Starting Backend Server...
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
pause

