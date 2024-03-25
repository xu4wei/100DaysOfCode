def checkRecord(attendance_record):
    # Check if the student was absent for strictly fewer than 2 days.
    absences = attendance_record.count('A')
    if absences >= 2:
        return False

    # Check if the student was not late for more than 1 day.
    lates = attendance_record.count('L')
    if lates > 2:
        return False

    # If both conditions are met, the student is eligible for the award.
    return True


s1 = "PPALLP"
s2 = "PPALLL"
print(checkRecord(s1))
print(checkRecord(s2))
