"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""
#Solution

def bmi(w, h):
    bmi = w / h ** 2

    if bmi <= 18.5:
        return "Underweight"

    elif bmi <= 25.0:
        return "Normal"

    elif bmi <= 30.0:
        return "Overweight"

    elif bmi > 30:
        return "Obese"

    else:
        return "Error"
