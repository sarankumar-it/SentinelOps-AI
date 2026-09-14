from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import sqlite3
import logging

from app.services.analyzer import analyze_risk

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SentinelOps-AI",
    description="AI-powered intelligent operations platform",
    version="1.0.0"
)

model = joblib.load("models/sentinel_model.pkl")


from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    cpu_usage: float = Field(..., ge=0, le=100)
    memory_usage: float = Field(..., ge=0, le=100)
    response_time: float = Field(..., ge=0)
    error_rate: float = Field(..., ge=0, le=1)
    request_rate: float = Field(..., ge=0)


def save_prediction(data, prediction, risk, explanation):
    connection = sqlite3.connect("data/sentinelops.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO operations (
            cpu_usage,
            memory_usage,
            response_time,
            error_rate,
            request_rate,
            prediction,
            risk,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.cpu_usage,
        data.memory_usage,
        data.response_time,
        data.error_rate,
        data.request_rate,
        prediction,
        risk,
        explanation
    ))

    connection.commit()
    connection.close()


@app.get("/")
def home():
    return {
        "message": "SentinelOps-AI is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/model-status")
def model_status():
    return {
        "model": "Random Forest",
        "status": "loaded"
    }


@app.post("/predict")
def predict(data: PredictionInput):
    features = [[
        data.cpu_usage,
        data.memory_usage,
        data.response_time,
        data.error_rate,
        data.request_rate
    ]]

    prediction = int(model.predict(features)[0])

    analysis = analyze_risk(
        data.cpu_usage,
        data.memory_usage,
        data.response_time,
        data.error_rate
    )

    risk = analysis["risk"]

    if risk == "High":
        explanation = "Operational risk detected: " + ", ".join(analysis["reasons"]) + "."
    else:
        explanation = "System indicators are within normal operating conditions."

    logger.info("Prediction completed: risk=%s, prediction=%s", risk, prediction)

    save_prediction(data, prediction, risk, explanation)

    return {
        "prediction": prediction,
        "risk": risk,
        "explanation": explanation,
        "analysis": analysis,
        "database": "saved"
    }


@app.get("/history")
def history():
    connection = sqlite3.connect("data/sentinelops.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    rows = cursor.execute("""
        SELECT *
        FROM operations
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return [dict(row) for row in rows]


@app.get("/summary")
def summary():
    connection = sqlite3.connect("data/sentinelops.db")
    cursor = connection.cursor()

    total = cursor.execute(
        "SELECT COUNT(*) FROM operations"
    ).fetchone()[0]

    high_risk = cursor.execute(
        "SELECT COUNT(*) FROM operations WHERE risk = 'High'"
    ).fetchone()[0]

    normal = cursor.execute(
        "SELECT COUNT(*) FROM operations WHERE risk = 'Normal'"
    ).fetchone()[0]

    connection.close()

    return {
        "total_predictions": total,
        "high_risk": high_risk,
        "normal": normal
    }




