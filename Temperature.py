class TemperatureConverter:

    def __init__(self, temperature):
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9 / 5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5 / 9

    def celsius_to_kelvin(self):
        return self.temperature + 273.15

    def kelvin_to_celsius(self):
        return self.temperature - 273.15


def main():
    print("===== Temperature Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice (1-4): ")
    temperature = float(input("Enter temperature: "))

    converter = TemperatureConverter(temperature)

    if choice == "1":
        result = converter.celsius_to_fahrenheit()
        print(f"{temperature}°C = {result:.2f}°F")

    elif choice == "2":
        result = converter.fahrenheit_to_celsius()
        print(f"{temperature}°F = {result:.2f}°C")

    elif choice == "3":
        result = converter.celsius_to_kelvin()
        print(f"{temperature}°C = {result:.2f}K")

    elif choice == "4":
        result = converter.kelvin_to_celsius()
        print(f"{temperature}K = {result:.2f}°C")

    else:
        print("Invalid choice!")


main()