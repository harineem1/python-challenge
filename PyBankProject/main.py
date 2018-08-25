# to read CSV files
import csv

# Files to Load
files_to_load = "Resources/budget_data.csv"
files_to_output = "Resources/Financial_analysis.txt"
f= open(files_to_output,"w+")

# things to caluculate
total_months = 0
total_profits = 0

prev_profits = 0
profits_change = 0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

profits_changes = []
print ("total_months", "PL", "total_profits", "profits_change", "prev_profits", "greatest_increase", "greatest_decrease")
print (total_months, " ", total_profits, profits_change, prev_profits, greatest_increase[1], greatest_decrease[1])
        
# to read budget_data.csv files 
with open(files_to_load) as budget_data:
    reader = csv.DictReader(budget_data)
    
# By using condition and looping through the rows to find totalmonths, total profits, average change,greatest increase and greatest decrease
    for row in reader:
        
        # to find total months
        total_months = total_months + 1
        total_profits = total_profits + int(row["Profit/Losses"])
        #print(roe)
        
        # to find changes in profits
        profits_change = int(row["Profit/Losses"]) - prev_profits
        
        # reset the value of prev_profits to the next row 
        prev_profits = int(row["Profit/Losses"])
        

        # to find the greatest increase
        if (profits_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profits_change
            
        # to find  the greatest decrease
        if (profits_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]  
            greatest_decrease[1] = profits_change
            
        # Add to the profits_changes list
        profits_changes.append(profits_change)
        print (total_months, " ", total_profits, profits_change, prev_profits, greatest_increase[1], greatest_decrease[1])
      

    # Set the profits average
    profits_avg = (sum(profits_changes) - profits_changes[0] )/ (total_months-1)
      
      # Show Output
    print("\n\n\n\n")
 
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months: " + str(total_months))
    print("Total profits: " + "$" + str(total_profits))
    print("Average Change: " + "$" + str(round(profits_avg,2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
      
    f.write ("Financial Analysis\n")
    f.write("-----------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    
    f.write("Total profits: " + "$" + str(total_profits) + "\n")
    f.write("Average Change: " + "$" + str(round(profits_avg,2)) + "\n")
    f.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")\n")
    f.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")\n")
      
    f.close()

#