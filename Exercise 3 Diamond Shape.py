def print_diamond(n):
    if n % 2 == 0: # Will check if n is an odd number
        print("Please just provide only an odd integer.")
        return  # Stop the function if n is not odd

    # First part of the diamond (upper part)
    for i in range(n // 2 + 1):  # Loop from 0 to middle of the diamond
        spaces = ' ' * (n // 2 - i)  # Print spaces to center the stars
        stars = '*' * (2 * i + 1)  # Print increasing number of stars
        print(spaces + stars)  # Combine spaces and stars, then print

    # Second part of the diamond (lower part)
    for i in range(n // 2 - 1, -1, -1):  # Loop from middle down to the last row
        spaces = ' ' * (n // 2 - i)  # Print spaces to center the stars
        stars = '*' * (2 * i + 1)  # Print decreasing number of stars
        print(spaces + stars)  # Combine spaces and stars, then print

# Ask the user to input an odd number
n = int(input("Please Enter an odd integer: "))

# Call the function to print the diamond
print_diamond(n)
