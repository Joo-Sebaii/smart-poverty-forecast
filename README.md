# Smart Poverty Forecast

A machine learning-based application for predicting poverty levels using historical data.

## Project Structure

```
smart-poverty-forecast/
├── backend/          # FastAPI backend server
│   ├── main.py       # API endpoints
│   ├── *.pkl         # Trained ML models
│   └── requirements.txt
├── frontend/         # Streamlit frontend application
│   ├── app.py        # Web interface
│   └── requirements.txt
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.7+ installed
- pip package manager

### Installation

1. **Install Backend Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Install Frontend Dependencies:**
   ```bash
   cd frontend
   pip install -r requirements.txt
   ```

## Running the Project

### Option 1: Using Batch Scripts (Windows)
- Run `start_backend.bat` to start the backend server
- Run `start_frontend.bat` to start the frontend application (in a separate terminal)

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
uvicorn main:app --reload
```
Backend will be available at: http://127.0.0.1:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
streamlit run app.py
```
Frontend will be available at: http://localhost:8501

## API Endpoints

- `GET /` - Health check endpoint
- `POST /predict` - Predict poverty levels
  - Parameters:
    - `income`: Current median household income
    - `poverty_last_year`: Poverty percentage last year
    - `income_last_year`: Income from last year
    - `avg_3yr`: 3-year poverty average

## Usage

1. Start the backend server first
2. Start the frontend application
3. Open your browser to the Streamlit URL (usually http://localhost:8501)
4. Enter the required values and click "Predict Poverty Levels"

## Notes

- The backend server must be running before using the frontend
- Models are loaded automatically when the backend starts
- Use `--reload` flag for development (automatic restart on code changes)
