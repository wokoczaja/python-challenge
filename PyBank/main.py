import os
import csv
budgetcsv=os.path.join("Resources","Bank_Budget_Data.csv")
#Create list variables to store data
months=[]
profits=[]
with open(budgetcsv, newline="") as csvfile:
    budgetreader=csv.reader(csvfile,delimiter=",")   

#Skip the header row
    next(budgetreader)
#Read each row into the list
    for row in budgetreader:
        months.append(row[0])
        profits.append(int(row[1]))
#Calculate total number months
total_months=(len(months))

#Calculate net total amount of Profit/Losses
net_total=sum(profits)

#Set-up variables for greatest increase, greatest decrease, and average change
greatinc=0
greatdec=0
total_change=0


#Loop through profit rows-backwards- to find values for greatest increase and decrease and average
for r in range(total_months,1,-1):
    profit_change=profits[r-1]-profits[r-2]
    if profit_change < greatdec:
        greatdec=profit_change
        greatdec_month=months[r-1]
    elif profit_change>greatinc:
        greatinc=profit_change
        greatinc_month=months[r-1]
    total_change=total_change+profit_change
average_change=round(total_change/(total_months-1),2)
   
#Print Financial Summary
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {str(greatinc_month)} (${str(greatinc)})")
print(f"Greatest Decrease in Profits: {str(greatdec_month)} (${str(greatdec)})")

#Export text file with results
financial_analysis=(f'''Financial Analysis
------------------------
Total Months: {str(total_months)}
Total: ${str(net_total)}
Average Change: ${str(average_change)}
Greatest Increase in Profits: {str(greatinc_month)} (${str(greatinc)})
Greatest Decrease in Profits: {str(greatdec_month)} (${str(greatdec)})''')

analysis=open('financial_analysis.txt','w')
analysis.write(financial_analysis)
analysis.close()

