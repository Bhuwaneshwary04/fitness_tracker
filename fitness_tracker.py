daily_data = {"workouts": [],"water_liters": 0,"sleep_hours": 0,"bmi": None}


#WORKOUT TRACKER
def log_workout():
    print("\n-- Log Workout --")
    workout = input("Enter workout name (e.g., Pushups, Running): ")
    duration = input("Enter duration in minutes: ")

    # Save workout entry
    daily_data["workouts"].append({"name": workout, "duration": duration})
    print(" Workout added successfully!")
    
#BMI CALCULATOR 
def calculate_bmi():
    print("\n BMI Calculator ")
    height = float(input("Enter height in meters (e.g., 1.65): "))
    weight = float(input("Enter weight in kg: "))

    bmi = weight / (height ** 2)
    daily_data["bmi"] = round(bmi, 2)

    # Classifying BMI type
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 24.9:
        status = "Normal Weight"
    elif bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    print(f"Your BMI is {daily_data['bmi']} ({status})")

#WATER INTAKE TRACKER 
def track_water():
    print("\n-- Water Intake Tracker --")
    water = float(input("Enter water intake in liters today: "))

    daily_data["water_liters"] += water
    print(f"Water updated! Total today: {daily_data['water_liters']} liters")

# SLEEP TRACKER 
def track_sleep():
    print("\n-- Sleep Tracker --")
    sleep = float(input("Enter your sleep hours (e.g., 7.5): "))

    daily_data["sleep_hours"] = sleep
    print(f"Sleep updated! You slept {sleep} hours")

# DAILY SUMMARY
def view_summary():
    print("\n================ DAILY SUMMARY ================")
    print("WORKOUTS:")
    if len(daily_data["workouts"]) == 0:
        print("  No workouts logged yet.")
    else:
        for w in daily_data["workouts"]:
            print(f" {w['name']} - {w['duration']} minutes")

    print(f"\nBMI: {daily_data['bmi'] if daily_data['bmi'] else 'Not calculated yet'}")
    print(f"Water Intake: {daily_data['water_liters']} liters")
    print(f"Sleep: {daily_data['sleep_hours']} hours")
    print("================================================")

# MAIN MENU 
def main():
    while True:
        print("\n================ FITNESS TRACKER ================")
        print("1. Log Workout")
        print("2. Calculate BMI")
        print("3. Add Water Intake")
        print("4. Add Sleep Hours")
        print("5. View Daily Summary")
        print("6. Exit")
        print("=================================================")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            calculate_bmi()
        elif choice == "3":
            track_water()
        elif choice == "4":
            track_sleep()
        elif choice == "5":
            view_summary()
        elif choice == "6":
            print("Exiting Fitness Tracker. Stay healthy!")
            break
        else:
            print("Invalid choice. Please choose between 1-6.")

# START PROGRAM 
main()
