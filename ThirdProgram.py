# If applicant has high income AND good credit
# Eligible for loan

# AND operation
# AND:both

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# OR operation
# OR: at least one

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# If applicant has good AND doesn't have a criminal record

has_high_income = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")





