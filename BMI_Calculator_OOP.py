# BMI Calculator using OOP

class BMICalculator:

    # Method to calculate BMI
    def calculate_bmi(self, weight, height):
        bmi = weight / (height * height)
        return bmi

    # Method to display BMI category
    def show_category(self, bmi):

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")


def main():

    print("BMI Calculator")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Create object
    bmi = BMICalculator()

    # Call method
    result = bmi.calculate_bmi(weight, height)

    print("Your BMI is:", round(result, 2))

    bmi.show_category(result)


if __name__ == "__main__":
    main()