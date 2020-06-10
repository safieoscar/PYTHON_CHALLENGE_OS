import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = []
change = []
p_change = []

avg_change = 0
profit_change = 0
monthcount = 0
profit = 0


with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    cvs_header = next(csvreader)

    for row in csvreader:
        monthcount += 1
        profit += int((row[1]))
        change.append(int(row[1]))
        months.append(row[0])
    
    for i in range(len(change)-1):
        current = (change[i+1] - change[i])
        profit_change += (change[i+1] - change[i])
        p_change.append(current)
        
    avg_change = profit_change/(len(p_change))

    g_increase = max(p_change)
    m_increase = months[p_change.index(g_increase) + 1] 

    g_decrease = min(p_change)
    m_decrease = months[p_change.index(g_decrease) + 1]
  

#print(monthcount)
#print(profit)
#print(avg_change)

#print(g_increase)
#print(g_decrease)
#print(m_increase)
#print(m_decrease)

print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(profit))  
print("Average Change: $" + str(round(avg_change, 2)))
print("Greatest Increase in Profit: " + m_increase + "($" + str(g_increase) + ")")
print("Greatest Decrease in Profit: " + m_decrease + "($" + str(g_decrease) + ")")

analysis = open('financial_analysis.txt', 'w')
analysis.write("Financial Analysis\n")
analysis.write("------------------------------\n")
analysis.write("Total Months: " + str(monthcount) + "\n")
analysis.write("Total: $" + str(profit) + "\n")  
analysis.write("Average Change: $" + str(round(avg_change, 2)) + "\n")
analysis.write("Greatest Increase in Profit: " + m_increase + "($" + str(g_increase) + ")" +"\n")
analysis.write("Greatest Decrease in Profit: " + m_decrease + "($" + str(g_decrease) + ")" + "\n")




    





