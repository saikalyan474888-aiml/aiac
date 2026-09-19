# Task 3: Transparency in AI-Based Admission SystemIdentified Transparency Risks:
# A "black box" admission system that outputs only "Selected" or "Rejected" provides no recourse or feedback. Students cannot know if they were rejected due to a low score, a missing document, or an algorithmic error.
# Example of an Unexplained Decision:
# Input: Student ID 1045 (Score: 78, Marks: 82%)
# Output: Status -> Rejected
# Revised Version (Transparent Decision Making):
def evaluate_admission(entrance_score, academic_marks, extracurriculars):
    min_entrance = 80
    min_academic = 75
    
    reasons = []
    if entrance_score < min_entrance:
        reasons.append(f"Entrance score ({entrance_score}) is below the required {min_entrance}.")
    if academic_marks < min_academic:
        reasons.append(f"Academic marks ({academic_marks}%) are below the required {min_academic}%.")
        
    if not reasons:
        return "Decision: Selected\nReason: Applicant meets all baseline academic and exam criteria."
    else:
        return f"Decision: Rejected\nReason(s): {', '.join(reasons)}"

# Example Output showing important factors:
print(evaluate_admission(78, 82, "Debate Club"))
# Output of Revised Version:

# Decision: Rejected
# Reason: Entrance score (78) is below the required 80.