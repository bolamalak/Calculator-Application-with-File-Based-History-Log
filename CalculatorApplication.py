from datetime import datetime

LOG_FILE = "calculator_history.txt"


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def save_to_history(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {entry}\n"
    file = open(LOG_FILE, "a")
    file.write(log_line)
    file.close()


def display_history():
    try:
        file = open(LOG_FILE, "r")
        content = file.read()
        file.close()
        if content:
            print("\n--- Calculation History ---")
            print(content)
        else:
            print("\nHistory is empty.")
    except FileNotFoundError:
        print("\nNo history found yet.")

    input("\nPress Enter to continue...")


def main():
    while True:
        print("\n--- CLI Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. View History Log")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = num1 + num2
            entry = f"{num1} + {num2} = {result}"
            print(f"Result: {entry}")
            save_to_history(entry)

        elif choice == "2":
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = num1 - num2
            entry = f"{num1} - {num2} = {result}"
            print(f"Result: {entry}")
            save_to_history(entry)

        elif choice == "3":
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            result = num1 * num2
            entry = f"{num1} * {num2} = {result}"
            print(f"Result: {entry}")
            save_to_history(entry)

        elif choice == "4":
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                entry = f"{num1} / {num2} = {result}"
                print(f"Result: {entry}")
                save_to_history(entry)

        elif choice == "5":
            display_history()

        elif choice == "6":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 6.")


main()