# Simple Command-Line BMI Calculator for Beginners

def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in meters."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    print("================================\n")
    
    while True:
        try:
            # Get weight input
            weight_input = input("Enter your weight in kilograms (e.g., 70): ")
            weight = float(weight_input)
            
            if weight <= 0:
                print("Error: Weight must be greater than 0. Please try again.\n")
                continue
            
            if weight > 500:  # Reasonable upper limit
                print("Warning: Weight seems unusually high. Please check your input.\n")
                continue
            
            # Get height input
            height_input = input("Enter your height in meters (e.g., 1.75): ")
            height = float(height_input)
            
            if height <= 0:
                print("Error: Height must be greater than 0. Please try again.\n")
                continue
            
            if height > 2.5:  # Reasonable upper limit for humans
                print("Warning: Height seems unusually high. Please check your input.\n")
                continue
            
            if height < 1.0:
                print("Note: Height is quite low, but we'll proceed with calculation.\n")
            
            # Calculate and display results
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            
            print("\n=== Your BMI Result ===")
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {category}")
            print("========================\n")
            
            # Ask if user wants to calculate again
            again = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
            if again != "yes" and again != "y":
                print("Thank you for using the BMI Calculator. Stay healthy!")
                break
                
        except ValueError:
            print("Error: Please enter valid numbers only (e.g., 70 or 1.75). Try again.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

# Run the program
if __name__ == "__main__":
    main()