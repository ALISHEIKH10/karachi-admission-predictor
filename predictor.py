"""
Admission Prediction Logic
Calculates merit scores and predicts admission chances
"""

from universities_data import KARACHI_UNIVERSITIES, MERIT_WEIGHTS


def calculate_percentage(obtained, total):
    """Calculate percentage"""
    if total == 0:
        return 0
    return (obtained / total) * 100


def calculate_merit_score(uni_key, matric_pct, inter_pct, test_pct, interview_pct=70):
    """Calculate merit score based on university formula"""
    weights = MERIT_WEIGHTS.get(uni_key, {"matric": 0, "inter": 0.50, "test": 0.50})
    
    score = 0
    score += weights.get("matric", 0) * matric_pct
    score += weights.get("inter", 0) * inter_pct
    score += weights.get("test", 0) * test_pct
    score += weights.get("interview", 0) * interview_pct
    
    return round(score, 2)


def predict_admission(uni_key, program, merit_score, inter_pct):
    """Predict admission chance for a specific program"""
    uni = KARACHI_UNIVERSITIES[uni_key]
    
    # Check minimum inter requirement
    if inter_pct < uni["min_inter_marks"]:
        return {
            "chance": "Not Eligible",
            "percentage": 0,
            "reason": f"Minimum {uni['min_inter_marks']}% Inter marks required",
            "color": "red"
        }
    
    # Get last merit for this program
    last_merit = uni["merit_2024"].get(program, 65)
    
    # Calculate difference
    diff = merit_score - last_merit
    
    if diff >= 10:
        chance = "Almost Certain ✅"
        pct = 95
        color = "green"
    elif diff >= 5:
        chance = "Very High Chance ✅"
        pct = 85
        color = "green"
    elif diff >= 0:
        chance = "Good Chance 🟡"
        pct = 70
        color = "orange"
    elif diff >= -3:
        chance = "Borderline Case 🟡"
        pct = 45
        color = "orange"
    elif diff >= -7:
        chance = "Low Chance ⚠️"
        pct = 20
        color = "red"
    else:
        chance = "Very Low Chance ❌"
        pct = 5
        color = "red"
    
    return {
        "chance": chance,
        "percentage": pct,
        "merit_score": merit_score,
        "last_merit": last_merit,
        "difference": diff,
        "color": color
    }


def get_all_predictions(student_data):
    """Get predictions for all universities student applied to"""
    results = []
    
    matric_pct = calculate_percentage(
        student_data["matric_obtained"], 
        student_data["matric_total"]
    )
    
    inter_pct = calculate_percentage(
        student_data["inter_obtained"],
        student_data["inter_total"]
    )
    
    for uni_test in student_data["tests"]:
        uni_key = uni_test["uni_key"]
        program = uni_test["program"]
        test_obtained = uni_test["test_obtained"]
        test_total = uni_test["test_total"]
        
        test_pct = calculate_percentage(test_obtained, test_total)
        
        merit_score = calculate_merit_score(
            uni_key, matric_pct, inter_pct, test_pct
        )
        
        prediction = predict_admission(uni_key, program, merit_score, inter_pct)
        
        uni_info = KARACHI_UNIVERSITIES[uni_key]
        
        results.append({
            "uni_key": uni_key,
            "uni_name": uni_info["full_name"],
            "program": program,
            "matric_pct": matric_pct,
            "inter_pct": inter_pct,
            "test_pct": test_pct,
            "merit_score": merit_score,
            "prediction": prediction,
            "uni_info": uni_info,
            "annual_fee": uni_info["annual_fee"],
            "rating": uni_info["rating"],
            "type": uni_info["type"],
        })
    
    # Sort by chance percentage (highest first)
    results.sort(key=lambda x: x["prediction"]["percentage"], reverse=True)
    
    return results, matric_pct, inter_pct


def get_best_recommendation(results):
    """Get AI recommendation for best university"""
    eligible = [r for r in results if r["prediction"]["percentage"] > 40]
    
    if not eligible:
        return None
    
    # Score each university based on multiple factors
    scored = []
    for r in eligible:
        score = 0
        
        # Admission chance (40% weight)
        score += r["prediction"]["percentage"] * 0.40
        
        # University rating (30% weight)
        score += r["rating"] * 10 * 0.30
        
        # Job placement bonus
        placement = r["uni_info"]["job_placement"]
        if placement == "Excellent":
            score += 15
        elif placement == "Very Good":
            score += 10
        elif placement == "Good":
            score += 5
        
        # Public university bonus (affordability)
        if r["type"] == "Public":
            score += 10
        
        scored.append((r, score))
    
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0] if scored else eligible[0]
