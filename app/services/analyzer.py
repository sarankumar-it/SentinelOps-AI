def analyze_risk(cpu_usage, memory_usage, response_time, error_rate):
    reasons = []

    if cpu_usage > 75:
        reasons.append("High CPU usage")

    if memory_usage > 80:
        reasons.append("High memory usage")

    if response_time > 350:
        reasons.append("High response time")

    if error_rate > 0.10:
        reasons.append("High error rate")

    if reasons:
        return {
            "risk": "High",
            "reasons": reasons
        }

    return {
        "risk": "Normal",
        "reasons": ["System indicators are within normal range"]
    }
