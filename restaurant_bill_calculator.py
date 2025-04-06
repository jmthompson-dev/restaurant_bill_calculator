from collections import namedtuple

# Define a named tuple to store the breakdown of meal costs
MealBreakdown = namedtuple('MealBreakdown', ['food_charge', 'tip', 'tax', 'total'])

# Ask the user for the cost of the meal
food_charge = float(input("Enter the cost of your meal: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Store all values in a namedtuple instance
meal = MealBreakdown(food_charge, tip, tax, total)

# Prepare the lines for the bill
lines = [
    f"Food:   ${meal.food_charge:.2f}",
    f"Tip:    ${meal.tip:.2f}",
    f"Tax:    ${meal.tax:.2f}",
    f"Total:  ${meal.total:.2f}"]

# Determine the width of the box based on the longest line
max_line_length = max(len(line) for line in lines)
box_width = max_line_length + 4 # padding for borders and spaces

# Build the top of the box
print(" " + "_" * (box_width - 2) + " ")
print("|" + " MEAL BILL ".center(box_width - 2) + "|")
print("|" + "-" * (box_width - 2) + "|")

# Print each line centered inside the box
for line in lines:
    print("| " + line.ljust(box_width - 3) + "|")

# Bottom of the box
print("|" + "_" * (box_width - 2) + "|")
