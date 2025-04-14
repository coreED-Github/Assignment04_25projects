def main():
    print("Welcome to the Temperature Converter!")

    fahrenheit = float(input("Enter temperature in Fahrenheit: ").strip())

    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit:.1f}°F = {celsius:.2f}°C")

if __name__ == '__main__':
    main()