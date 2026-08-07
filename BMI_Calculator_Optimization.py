# Week 2 - Activity 1.2
# Optimized BMI Calculator


# Check whether the input is a valid number
def isfloat(value):
    try:
        return float(value)
    except ValueError:
        return None


# Keep asking until the user enters a valid number
def inputfloat(message):
    while True:
        number = isfloat(input(message))
        if number is not None:
            return number
        print("Please enter a valid number.")


class BMICalculator:

    # Get user input
    def getdata(self):
        self.weight = inputfloat("Enter your weight (kg): ")
        self.height = inputfloat("Enter your height (cm): ") / 100

    # Calculate BMI
    def calculate(self):
        return round(self.weight / (self.height ** 2), 2)

    # Display BMI category
    def category(self):
        bmi = self.calculate()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"


def main():

    print("=" * 40)
    print("      BMI Calculator")
    print("=" * 40)

    calculator = BMICalculator()

    calculator.getdata()

    bmi = calculator.calculate()

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {calculator.category()}")

    print("=" * 40)


if __name__ == "__main__":
    main()