# Nutrition Tracker

## Overview
A simple Flask-based web application for tracking daily nutrition intake. Users can log meals with their nutritional information (calories, protein, carbs, fats) and view their meal history.

## Project Architecture
- **Framework**: Flask (Python web framework)
- **Database**: CSV file (data.csv) for persistent storage
- **Frontend**: HTML templates served by Flask
- **Structure**:
  - `app.py` - Main Flask application
  - `templates/` - HTML templates folder
  - `data.csv` - Meal data storage
  - `nutrition-tracker/tracker.py` - CLI version (not used by web app)

## Setup
- Python 3.11
- Flask installed via uv package manager
- Runs on 0.0.0.0:5000 for Replit proxy compatibility

## Deployment
Configured for autoscale deployment using the Flask development server.

## Recent Changes (Nov 6, 2025)
- Moved templates folder from nutrition-tracker/ to project root
- Updated app.py to bind to 0.0.0.0:5000 for Replit compatibility
- Created .gitignore for Python project
- Configured Flask workflow and deployment settings
- Installed Python 3.11 and Flask dependencies
