def is_eligible_for_loan(credit_score, annual_income):
    if credit_score > 700 and annual_income > 50000:
        return True
    else:
        return False

print(is_eligible_for_loan(740, 60000))
print(is_eligible_for_loan(720, 40000))
