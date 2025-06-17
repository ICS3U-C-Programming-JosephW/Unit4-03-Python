#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 30, 2025
# This program calculates the
# squared numbers up to the
# user's desired whole number
# with a for loop and checks.


# Define the main function.
def main():
    # Get the whole number from the user as a string.
    user_whole_number_str = input("\nEnter a whole number: ")

    # Try to check the validity of the user input.
    try:
        # Attempt to convert the entered string into an integer.
        user_whole_number_int = int(user_whole_number_str)

        # Check if the entered number is a whole number.
        if user_whole_number_int >= 0:
            # Display a newline for spacing.
            print()
            # Use a for loop to loop until the user's whole number.
            # Increment the end by one to include the excluded whole.
            for counter in range(user_whole_number_int + 1):
                # Determine the square result by squaring the counter.
                square_result = counter**2
                # Display the squared expression.
                print(f"{counter}^2 = {square_result}.")
        # Otherwise, the entered number is not specifically whole.
        else:
            # Display that the entered number is not a whole number.
            print(f"\n{user_whole_number_int} is not a whole number.")

    # Runs if int() could not convert the
    # user's string input into an integer.
    except ValueError:
        # Display to the user that they
        # did not enter a whole number.
        print(f"\n{user_whole_number_str} is not a whole number.")

    # Finally, run the exit message.
    finally:
        # Thank the user for using this program.
        print("\nThanks for using this program!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
