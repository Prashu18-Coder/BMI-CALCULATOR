def get_gender():
    while True:
        gender = input("Enter your gender (M/F): ").strip().upper()
        if gender in ('M', 'F'):
            return gender
        print("Invalid input. Please enter 'M' or 'F'.")

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 14:
                print("BMI is not calculated for age less than 14 years.")
                return None
            return age
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_height_weight():
    while True:
        try:
            height = float(input("Enter your height (in cm): "))
            weight = float(input("Enter your weight (in kg): "))
            return height, weight
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "🟦 Underweight"
    elif bmi < 25:
        return "🟩 Normal"
    elif bmi < 30:
        return "🟨 Overweight"
    else:
        return "🟧 Obese"

def suggested_weight_range(height):
    return 18.5 * ((height / 100) ** 2), 24.9 * ((height / 100) ** 2)

def health_tips(bmi):
    tips = {
        "🟦 Underweight": "Increase calorie intake with nutrient-rich foods.",
        "🟩 Normal": "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
        "🟨 Overweight": "Reduce intake of processed foods and sugary beverages.",
        "🟧 Obese": "Monitor health metrics like blood pressure and cholesterol levels."
    }
    return tips[bmi_category(bmi)]

def main():
    gender = get_gender()
    print("🤵 Male" if gender == 'M' else "👰 Female")

    age = get_age()
    if age is None:
        return

    height, weight = get_height_weight()
    bmi = calculate_bmi(height, weight)
    
    print("\nYour Current BMI is", format(bmi, '.1f'))
    print(bmi_category(bmi))

    sug_wt_ll, sug_wt_ul = suggested_weight_range(height)
    print("\nAnalysis:")
    print("Height (in cm):", format(height, '.1f'))
    print(f"Suggested Weight (kg): {sug_wt_ll:.1f} ~ {sug_wt_ul:.1f}")
    print("\nHealth tips wrt your BMI:")
    print(health_tips(bmi))

if __name__ == "__main__":
    while True:
        main()
        cont = input("\nDo you want to check another BMI calculation? (Y/N): ").strip().upper()
        if cont != 'Y':
            print("Thank you for using the BMI Calculator!")
            break
