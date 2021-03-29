#9

"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

attendance_percentage = int(input()[:-1])
having_medical_report = input()
is_eligible_for_final_exams = attendance_percentage >= 75 or having_medical_report == "Y"
if is_eligible_for_final_exams:
    print("Allowed to write exam")
else:
    print("Cannot write exam")
