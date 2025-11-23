print("Welcome to the Study Time Tracker!")
print("This program calculates your weekly study hours. \n")
daily_hours = input("How many hours do you study daily? ")
try:
    daily_hours = float(daily_hours)
    # Calculation
    weekly_hours = daily_hours * 7 
    monthly_hours = daily_hours * 30 
    print("\n" + "="*50)
    print(" Study Time Summary ")
    print("="*50)
    print(f"Daily Study Hours: {daily_hours} hours")
    print(f"Projected weekly total : {weekly_hours} hours")
    print(f"Projected monthly total: {monthly_hours} hours")
    print("="*50)

    if weekly_hours >= 20:
        print("Great job! You're dedicating a good amount of time to studying.")
    elif weekly_hours >= 10:
        print("Good effort! Consider increasing your study time for better results.")
    else:
        print("Try to allocate more time for studying to improve your learning outcomes.")
except ValueError:
    print("Error: Please enter a valid number for daily study hours.")
    print("Restart the program and try again.")
    exit()

# Final message
print("\nThank you for using the Study Time Tracker")