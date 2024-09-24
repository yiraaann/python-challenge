
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
g_increase = 0
g_increase_month = ""
g_decrease = 0
g_decrease_month = ""

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    previous_row = None

    # Track the total and net change
    net_change_list = []

    # Process each row of data
    for row in reader:

        # Track the total
        #total_months += 1

        # Track the net change
        total_net += int(row[1])
        if previous_row is not None:
            diff = int(row[1]) - int(previous_row[1])
            net_change_list.append(diff)

        # Update previous_row to current_row
        previous_row = row
        #print(net_change_list)
        total_months += 1

        # Calculate the greatest increase in profits (month and amount)
        if diff > g_increase:
            g_increase_month = (row[0])
            g_increase = diff
        #print(g_increase)

        # Calculate the greatest decrease in losses (month and amount)
        if diff < g_decrease:
            g_decrease_month = (row[0])
            g_decrease = diff
        #print(g_decrease)

# Calculate the average net change across the months
avg_net_change = sum(net_change_list)/len(net_change_list)
print(avg_net_change)

# Generate the output summary
output_summary = (
    f"\n\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {g_increase_month} (${g_increase})\n"
    f"Greatest Decrease in Profits: {g_decrease_month} (${g_decrease})\n")

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
