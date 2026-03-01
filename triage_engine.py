def calculate_emergency_priority(symptoms, heart_rate, age):
  
    score = 0
    if "chest pain" in symptoms.lower(): score += 5
    if heart_rate > 110 or heart_rate < 50: score += 3
    if age > 60: score += 2
    
    if score >= 7:
        return "P1: CRITICAL (Immediate Dispatch)"
    elif score >= 4:
        return "P2: STABLE BUT URGENT"
    else:
        return "P3: NON-URGENT"

print(f"Call Triage Result: {calculate_emergency_priority('Chest pain and sweating', 120, 65)}")
