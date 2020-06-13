# Import dependencies
import os
import csv

# Load the files
csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Output", "budget_outcome.txt")

# Open the csv file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Define variables
total_months = 0
total_revenue = 0
revenue_change = 0

revenue_change_list = []
month_of_change = []

greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

# Start loop
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months = total_months + 1
    total_revenue = total_revenue + int(first_row[1])
    previous_revenue = int(first_row[1])
    
    for row in csvreader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(first_row[1])
        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# Test summary
monthly_revenue_average = sum(revenue_change_list)/len(revenue_change_list)
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${monthly_revenue_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Create output file
output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_revenue}\n"
   f"Average  Change: ${monthly_revenue_average}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
with open("budget_outcome.txt", 'w') as txt_file:
    txt_file.write(output)
    
 