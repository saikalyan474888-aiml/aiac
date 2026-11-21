# # Task 6: Fairness in Loan Approval System
# # Identified Fairness Risks:
# #  If an AI model trains on historical loan data, it may inadvertently learn to deny loans based on age, marital status, or postal codes (which historically correlate with race or religion due to redlining). 
# Examples of Biased Rules:Age Bias: if age > 65: reject() - Discriminates against the elderly.  Proxy Bias: if zip_code == "90210": approve() - Uses location as a proxy for wealth or race, violating fair lending laws. 
#  Revised Version (Financially Grounded Decision): 
def evaluate_loan(income, loan_amount, credit_score, existing_debt):
    # Decision is based purely on financial health metrics (DTI ratio and Credit Score)
    debt_to_income_ratio = (existing_debt + (loan_amount * 0.1)) / income
    
    if credit_score < 620:
        return "Rejected: Credit score below minimum threshold."
    if debt_to_income_ratio > 0.43:
        return "Rejected: Debt-to-income ratio exceeds safe borrowing limits (43%)."
        
    return "Approved: Financial metrics meet lending criteria."

# Explanation of Improvement:
# This revised system improves fairness by strictly evaluating the applicant's Debt-to-Income (DTI) ratio and credit score. By explicitly excluding sensitive attributes like age, gender, and zip code, the algorithm evaluates creditworthiness purely on an individual's mathematical ability to repay the loan, aligning with ethical standards and legal compliance