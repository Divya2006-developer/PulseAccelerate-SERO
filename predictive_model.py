import numpy as np
import pandas as pd


def predict_emergency_hotspots(traffic_data, weather_condition, time_of_day):
  
    risk_score = (traffic_data * 0.6) + (weather_condition * 0.2) + (time_of_day * 0.2)
    
    if risk_score > 7.5:
        return "HIGH RISK: Dispatching Pre-positioned Ambulance"
    else:
        return "NORMAL: Monitoring Zone"

print("SERO Analysis for Sector 5:")
result = predict_emergency_hotspots(9, 8, 9)
print(result)
