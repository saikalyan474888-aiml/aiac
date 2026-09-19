# Task 2: Fair Decision Logic
# Code Snippet & Fairness Observations:
def check_scholarship(academic_score, family_income, location):
    # Unfair logic: Excludes a specific location regardless of merit or need
    if location == "Rural_District_C": 
        return "Rejected: Location not supported."
    
    if academic_score >= 85 and family_income < 50000:
        return "Approved"
    return "Rejected"
# Observations on Fairness: The logic above unfairly disadvantages students from "Rural_District_C" by automatically rejecting them, creating a geographic bias. It also uses a hard income cutoff ($50,000) that does not account for the varying cost of living across different locations.  Suggested Improvements:
# To ensure equitable decision-making, the location constraint should be removed completely unless the scholarship is explicitly chartered for a specific municipality. Instead of a flat income threshold, the system should use a dynamic threshold adjusted for the local cost of living index. Furthermore, a sliding scale for academic scores based on socioeconomic background could help level the playing field for under-resourced students.