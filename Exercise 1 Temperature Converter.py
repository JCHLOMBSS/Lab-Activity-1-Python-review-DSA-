Tempt = float(input("Enter the Temperature: ")) # Will be asking the user to input a Temperature


Conversion = input("Please Select your conversion type ( Type 'C' if Celsius to Celsius to Fahrenheit \
or 'F' to convert from Fahrenheit to Celsius: ").upper() # Will ask the user to choose the conversion type

# Will Execute the selected conversion
if Conversion == 'C':
    Converted_Tempt = (Tempt * 9/5) + 32
    print(f"{Tempt}°C is converted to {Converted_Tempt}°F")
elif Conversion == 'F':
    Converted_Tempt = (Tempt - 32) * 5/9
    print(f"{Tempt}°F is converted to {Converted_Tempt}°C")
else:
    print("Invalid conversion! Please only type 'C' or 'F'.")
