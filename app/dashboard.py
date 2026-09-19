import streamlit as st
import requests
from config import API_URL

st.set_page_config(
    page_title="SentinelOps-AI",
    layout="wide"
)

st.title("SentinelOps-AI")
st.markdown("### AI-Powered Intelligent Operations Dashboard")

# API status
with st.sidebar:
    st.title("SentinelOps-AI")
    st.write("AI Operations Monitoring")
    st.divider()
    st.write("System Status")

    try:
        api_check = requests.get(API_URL + "/health", timeout=3)

        if api_check.status_code == 200:
            st.success("API Connected")
        else:
            st.error("API Offline")
    except requests.exceptions.RequestException:
        st.error("API Offline")

    st.write("Model: Random Forest")

# System summary
response = requests.get(API_URL + "/summary")

if response.status_code == 200:
    data = response.json()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Predictions", data["total_predictions"])
    col2.metric("High Risk", data["high_risk"])
    col3.metric("Normal", data["normal"])
else:
    st.error("Unable to connect to SentinelOps-AI API.")

st.divider()

# Prediction form
st.header("System Risk Prediction")

cpu = st.number_input("CPU Usage (%)", 0.0, 100.0, 50.0)
memory = st.number_input("Memory Usage (%)", 0.0, 100.0, 50.0)
response_time = st.number_input("Response Time (ms)", 0.0, 2000.0, 150.0)
error_rate = st.number_input("Error Rate", 0.0, 1.0, 0.02)
request_rate = st.number_input("Request Rate", 0.0, 5000.0, 200.0)

if st.button("Analyze System"):
    payload = {
        "cpu_usage": cpu,
        "memory_usage": memory,
        "response_time": response_time,
        "error_rate": error_rate,
        "request_rate": request_rate
    }

    result = requests.post(
        API_URL + "/predict",
        json=payload
    )

    if result.status_code == 200:
        prediction = result.json()

        st.subheader("AI Analysis")
        st.write("Risk:", prediction["risk"])
        st.write("Explanation:", prediction["explanation"])

        st.subheader("Detected Reasons")

        for reason in prediction["analysis"]["reasons"]:
            st.write("-", reason)
    else:
        st.error("Prediction request failed.")

st.divider()

# Recent operations
st.header("Recent Operations")

history_response = requests.get(API_URL + "/history")

if history_response.status_code == 200:
    history_data = history_response.json()

    if history_data:
        st.dataframe(history_data, use_container_width=True)
    else:
        st.info("No operations recorded yet.")
else:
    st.error("Unable to load operation history.")

st.divider()

# Risk chart
st.header("Risk Overview")

chart_data = {
    "Risk Level": ["High Risk", "Normal"],
    "Count": [data["high_risk"], data["normal"]]
}

st.bar_chart(
    chart_data,
    x="Risk Level",
    y="Count"
)

