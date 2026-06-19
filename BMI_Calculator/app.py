# BMI Calculator - Oasis Infobyte Internship

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("=== BMI CALCULATOR ===")

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = calculate_bmi(weight, height)
category = get_category(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
