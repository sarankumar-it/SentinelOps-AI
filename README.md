# SentinelOps-AI

AI-powered intelligent operations monitoring and risk prediction platform.

## Overview

SentinelOps-AI is an AI/ML-based operations monitoring platform that analyzes system performance metrics and predicts potential operational risks.

The platform combines machine learning, REST APIs, database storage, and an interactive dashboard to provide a complete monitoring workflow.

## Key Features

- AI-based operational risk prediction
- Random Forest machine learning model
- FastAPI REST API
- Streamlit monitoring dashboard
- SQLite operation history
- Risk explanations
- System health monitoring
- Docker container support
- Pytest API testing
- GitHub version control

## System Metrics

SentinelOps-AI analyzes the following operational metrics:

- CPU usage
- Memory usage
- Response time
- Error rate
- Request rate

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Machine learning |
| Pandas | Data processing |
| FastAPI | REST API |
| Streamlit | Monitoring dashboard |
| SQLite | Data storage |
| Docker | Containerization |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |

## Project Architecture

```text
SentinelOps-AI/
│
├── app/
│   ├── ml/
│   │   ├── model.py
│   │   └── train.py
│   │
│   ├── services/
│   │   └── analyzer.py
│   │
│   ├── main.py
│   ├── dashboard.py
│   └── config.py
│
├── data/
│   ├── database.py
│   ├── generate_data.py
│   ├── ingest.py
│   └── operations_data.csv
│
├── models/
│   └── sentinel_model.pkl
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
## How It Works

1. Operational data is generated or collected.
2. The machine learning model analyzes system metrics.
3. SentinelOps-AI predicts whether the system is at high risk or operating normally.
4. The analyzer identifies the main operational reasons for the detected risk.
5. Prediction results are stored in SQLite.
6. FastAPI provides the backend services.
7. Streamlit provides an interactive monitoring dashboard.
8. Docker can be used to run the API in a containerized environment.

## Risk Analysis

The system evaluates operational indicators such as:

- High CPU usage
- High memory usage
- High response time
- High error rate

Based on these indicators and the trained machine learning model, the system produces a risk prediction and explanation.

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Application status |
| `/health` | GET | API health check |
| `/model-status` | GET | Machine learning model status |
| `/predict` | POST | Predict operational risk |
| `/history` | GET | View prediction history |
| `/summary` | GET | View risk summary |

## Running Locally

### 1. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1

## Running with Docker

### Build the Docker image

```powershell
docker build -t sentinelops-ai .

## Testing

Run the automated test suite from the VS Code Terminal:

```powershell
pytest

## Machine Learning

SentinelOps-AI uses a Random Forest classifier to predict operational risk from system performance metrics.

The trained model is stored at:

`models/sentinel_model.pkl`

The model is trained using operational data containing CPU usage, memory usage, response time, error rate, and request rate.

## Future Improvements

- Cloud deployment
- Automated risk alerts
- Advanced anomaly detection
- Real-time monitoring
- Authentication and authorization
- Production-grade database integration
- Cloud-native observability

## Project Goal

The goal of SentinelOps-AI is to demonstrate how AI and cloud technologies can be combined to build an intelligent operations monitoring and risk prediction platform.

## Author

**SARANKUMAR**