while True:
    print("What would you like to calculate?") # Will ask the user what they want to calculate
    print("Instruction: Type 'V' for Voltage, 'C' for Current, or 'R' for Resistance.")
    choice = input("Please select your choice (V, C, or R): ").strip().upper() # Will ask the user to input their choice

    # Will calculation depending to the user's choice
    if choice == 'V':  # For Voltage Calculation
        current = float(input("Please enter the current (C) in amperes: "))
        resistance = float(input("Please enter the resistance (R) in ohms: "))
        voltage = current * resistance
        print(f"The voltage is {voltage:.2f} volts.")

    elif choice == 'C':  # For Current Calculation
        voltage = float(input("Please enter the voltage (V) in volts: "))
        resistance = float(input("Please enter the resistance (R) in ohms: "))
        if resistance != 0:
            current = voltage / resistance
            print(f"The current is {current:.2f} amperes.")
        else:
            print("The Resistance cannot be zero! Division by zero is not applicable.")

    elif choice == 'R':  # For Resistance Calculation
        voltage = float(input("Please enter the voltage (V) in volts: "))
        current = float(input("Please enter the current (I) in amperes: "))
        if current != 0:
            resistance = voltage / current
            print(f"The resistance is {resistance:.2f} ohms.")
        else:
            print("Current cannot be zero! Division by zero is not applicable.")

    else:
        print("Your Choice is Invalid. Please re-enter only 'V', 'C', or 'R'.")

    # Ask if the user wants to perform another calculation
    repeat = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Thank you for using Ohm’s Law Calculator.")
        break