
# import modules
import csv
import os


# set variables equal to 0
max_monthly_profit = 0
min_monthly_profit = 0
total = 0
month_count = 0
previous_profit = 0

difference = []
# create file path
budget_data_csv = os.path.join("budget_data.csv")
with open(budget_data_csv, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        num = float(row[1])
        
        total += num
        total = round(total)

        month_count += 1
        
        avg_change = sum(ChangesInProfits) / len(ChangesInProfits)

        monthly_profit_change = float(row[1]) - previous_profit
        previous_profit = float(row[1])

        # max & min profits

        if monthly_profit_change > max_monthly_profit:
            max_monthly_profit = monthly_profit_change
            max_month = row[0]
            max_monthly_profit = round(max_monthly_profit)

        if monthly_profit_change < min_monthly_profit:
            min_monthly_profit = monthly_profit_change
            min_month = row[0]
            min_monthly_profit = round(min_monthly_profit)

final_output = (f' PyBank Financial Analysis\newline'
f' --------------------------------\newline'
f' Total months: {month_count}\newline'
f' Total: ${total}\newline'
f' Average Change: ${avg_change}\newline'
f' Max Increase in Profits: {max_month}, (${max_monthly_profit})\newline'
f' Min Increase in Profits: {min_month}, (${min_monthly_profit})\newline')
        
print(final_output)
