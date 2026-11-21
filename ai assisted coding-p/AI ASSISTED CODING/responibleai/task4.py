# Task 4: Ethical Scoring System
def evaluate_employee(project_completion_rate, teamwork_score, attendance_rate):
    # Weights: 40% Projects, 20% Teamwork, 40% Attendance
    score = (project_completion_rate * 0.4) + (teamwork_score * 0.2) + (attendance_rate * 0.4)
    return score
# Ethical Analysis:
# The scoring logic above contains unethical weighting. Weighting attendance_rate at 40% is highly problematic as it severely disadvantages employees with chronic illnesses, disabilities, or sudden caregiving responsibilities. Additionally, teamwork_score is subjective and prone to reviewer bias. A more balanced criteria would heavily weight objective outcomes (project_completion_rate) while dynamically adjusting or exempting attendance_rate to account for legally protected medical or family leaves.