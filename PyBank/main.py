import os
import csv

# Path to the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_profit_loss = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
months = []
previous_profit_loss = None
total_change = 0

# Open the CSV file and read the data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net profit/loss
        net_profit_loss += int(row[1])

        # Calculate the change in profit/loss since the previous month
        current_profit_loss = int(row[1])
        if previous_profit_loss is not None:
            current_change = current_profit_loss - previous_profit_loss
            total_change += current_change
            # Check if the current change is the greatest increase or decrease
            if current_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = current_change
            elif current_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = current_change
        previous_profit_loss = current_profit_loss

# Calculate the average change in profit/loss
average_change = round(total_change / (total_months - 1), 2)

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
