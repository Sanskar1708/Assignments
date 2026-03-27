from Temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin

def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("Select a conversion (1-3): ")
    
    try:
        temp = float(input("Enter the temperature value: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit.convert(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        elif choice == '2':
            result = fahrenheit_to_celsius.convert(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
        elif choice == '3':
            result = celsius_to_kelvin.convert(temp)
            print(f"{temp}°C is equal to {result:.2f}K")
        else:
            print("Invalid selection.")
            
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
