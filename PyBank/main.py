import os
import csv

# Path to the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    # Create empty lists to store the csv values
    month = []
    profit = []
    change_profit = []

    # Iterate through the rows and add the values to the respective lists
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))

    # Compute the change in profit and store in another list
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

    # Evaluate the maximum and minimum values from the change_profit list
    maximum = max(change_profit)
    minimum = min(change_profit)

    # Retrieve the corresponding months using the index of the maximum and minimum values
    month_increase = change_profit.index(max(change_profit))+1
    month_decrease = change_profit.index(min(change_profit))+1

    # Print the final analysis
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {len(month_count)}")
    print(f"Total: ${sum(profit)}")
    print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    print(f"Greatest Increase in Profits: {month_count[month_increase]} (${maximum})")
    print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${minimum})")
    
