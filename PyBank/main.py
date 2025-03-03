
# Dependencies
import csv
import os

# Change directory
# ("C:\Users\yiran\OneDrive\Documents\GitHub\python-challenge\PyBank")
# C:\Users\yiran\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\budget_analysis.txt

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
# file_to_load = r"C:\Users\yiran\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\budget_data.csv"
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path
# file_to_output = r"C:\Users\yiran\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\budget_analysis.txt"

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_change_list = []
month_of_change = []


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # Update previous_row to current_row
        # previous_row = row
        # print(net_change_list)
        # total_months += 1

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # print(greatest_increase)

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        # print(greatest_decrease)

# Calculate the average net change across the months
avg_net_change = sum(net_change_list)/len(net_change_list)
# print(avg_net_change)

# Generate the output summary
output_summary = (
    f"\n\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
