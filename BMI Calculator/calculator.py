def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))

        if weight <= 0 or height <= 0:
            print("Please enter valid positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
