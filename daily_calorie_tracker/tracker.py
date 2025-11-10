# ---------------------------------------------------------
# Name: Surya Rao
# Date: 10 November 2025
# Project Title: Daily Calorie Tracker
# ---------------------------------------------------------

print("Welcome to the Daily Calorie Tracker!")
print("This program helps you record your meals and track your calorie intake.\n")

# Task 2: Input and Data Collection
meal_names = []
calorie_values = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    meal = input(f"Enter meal name {i + 1}: ")
    calories = float(input("Enter calories for this meal: "))
    meal_names.append(meal)
    calorie_values.append(calories)

# Task 3: Calorie Calculations
total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    print("\nYou have exceeded your daily calorie limit!")
else:
    print("\nYou are within your daily calorie limit.")

# Task 5: Neatly Formatted Output
print("\nMeal Name\tCalories")
print("----------------------------")
for i in range(num_meals):
    print(f"{meal_names[i]}\t\t{calorie_values[i]}")
print("----------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories}")

# Task 6 (Bonus): Save Session Log to File
save = input("\nDo you want to save the report to a file? (yes/no): ")

if save.lower() == "yes":
    file = open("calorie_log.txt", "w")
    file.write("Daily Calorie Tracker Report\n")
    file.write("----------------------------\n")
    for i in range(num_meals):
        file.write(f"{meal_names[i]}\t\t{calorie_values[i]}\n")
    file.write("----------------------------\n")
    file.write(f"Total:\t\t{total_calories}\n")
    file.write(f"Average:\t{average_calories}\n")
    if total_calories > daily_limit:
        file.write("You have exceeded your daily calorie limit!\n")
    else:
        file.write("You are within your daily calorie limit.\n")
    file.close()
    print("Report saved successfully to 'calorie_log.txt'.")
