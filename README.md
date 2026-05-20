# Flask Web Application

A production-ready Flask web application with best practices for folder structure and configuration management.

## Project Structure

```
.
├── app/                    # Main Flask application package
│   ├── __init__.py        # Flask app initialization
│   ├── routes/            # URL routes (blueprints)
│   │   ├── __init__.py
│   │   └── main.py        # Main application routes
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, images)
│   └── utils/             # Helper functions & utilities
├── config/                # Configuration module
│   ├── __init__.py
│   └── config.py          # Environment-based configuration
├── tests/                 # Test suite
├── docs/                  # Documentation
├── main.tf                # Terraform infrastructure configuration
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore rules
├── README.md              # This file
└── run.py                 # Application entry point
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv env
source env/Scripts/activate  # On Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run the Application
```bash
python run.py
```

The application will be available at `http://0.0.0.0:5000`

## Environment Variables

- `FLASK_ENV`: Flask environment (development, production, testing)
- `FLASK_APP`: Flask application entry point
- `SECRET_KEY`: Flask secret key for sessions
- `SERVER_HOST`: Server host (default: 0.0.0.0)
- `SERVER_PORT`: Server port (default: 5000)

## Running Tests
```bash
pytest
```

## Deployment

This project includes Terraform configuration in `main.tf` for infrastructure deployment.
