# 🎓 AI Student Report System

An AI-powered, interactive web application built with **Flask** to analyze student performance data. Upload student grades, instantly generate visual dashboards with interactive charts, rank students, and download processed CSV reports.

---

## 🚀 Key Features

- **📁 Easy Upload**: Drag and drop or browse to upload your student dataset in CSV format.
- **📊 Interactive Dashboard**: Visualizes class performance trends instantly using **Chart.js** (Bar & Pie charts).
- **🏆 Live Leaderboard**: Displays the top 10 outstanding students dynamically with custom rank badges.
- **📈 Automated Analysis**: Categorizes performance levels (`Excellent`, `Average`, `Needs Improvement`) and assigns ranks.
- **📥 Instant Export**: Download the fully processed CSV containing performance categories and rankings with a single click.
- **☁️ Cloud Deployable**: Pre-configured for hosting platforms like **Render**, **Railway**, or **Heroku** (includes `Procfile` and `runtime.txt`).

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Data Analysis**: Pandas, NumPy
- **Visualizations**: Chart.js (via CDN)
- **Frontend**: HTML5, CSS3, Bootstrap 5 (Darkly Bootswatch Theme for sleek aesthetics)
- **Production Server**: Gunicorn

---

## 📂 Project Structure

```text
AI-Student-Report-System-main/
│
├── ml_models/
│   ├── __init__.py
│   └── analysis.py          # Core logic for ranking and performance grading
│
├── static/
│   ├── css/
│   │   └── style.css        # Custom styles and animations
│   └── js/                  # Directory for additional frontend scripts
│
├── templates/
│   ├── layout.html          # Base layout template
│   ├── welcome.html         # Landing page / welcome screen
│   ├── index.html           # File upload screen
│   ├── upload.html          # Backup upload component
│   └── dashboard.html       # Analytics dashboard & leaderboard
│
├── uploads/                 # Directory where uploaded and processed CSVs are stored
├── .gitignore               # Configured Git ignores (caches, virtual env, uploads)
├── app.py                   # Main Flask application entrypoint
├── procfile                 # Heroku/Render process configuration
├── pyproject.toml           # PEP 518 project specification
├── requirements.txt         # Python package dependencies
├── runtime.txt              # Target Python runtime version
└── report.csv               # Sample student performance dataset
```

---

## ⚙️ Quick Start Guide

### Prerequisites
Make sure you have **Python 3.11+** installed on your system.

### 1. Clone & Navigate to Project
```bash
git clone <your-repository-url>
cd AI-Student-Report-System-main
```

### 2. Setup Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries specified in the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000` to access the application.

---

## 📊 Sample CSV Format

To test the application, you can upload `report.csv` included in the root folder, or create a CSV matching this schema:

```csv
Name,Marks
Alice,90
Bob,70
Charlie,50
```

> [!TIP]
> The system automatically searches for columns named `marks`, `score`, or `total` (case-insensitive) to perform rankings.

---

## 🚀 Deployment

The project is ready to be deployed on **Render** or **Railway**:
1. Connect your GitHub repository to Render/Railway.
2. Select **Python** environment.
3. Use the following start command:
   ```bash
   gunicorn app:app
   ```
4. Set the Build Command (if prompted) to:
   ```bash
   pip install -r requirements.txt
   ```
