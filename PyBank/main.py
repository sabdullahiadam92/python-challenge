# Sumaya Abdullahi
# Data Analytics BootCamp - Cohort 3
# Homework 3 - PyBank Challenge

# Importing Modules
import os
import pandas as pd

# Defining data frame file
df = pd.read_csv("pybank.csv")

#Calculating the count of data set and calculating the sum of profit/losses
Total_Months = df.Date.count()
Total_Profit = df[['Profit/Losses']].sum()
Total_Profit1 = int(Total_Profit)

# Calculating difference and average of difference of profits/losses
dif = df[['Profit/Losses']].diff()
avg_dif = dif.mean()
avg_dif2 = avg_dif.round(2)
avg_dif3 = (avg_dif2).values
avg = float(avg_dif3)

# greatest decrease and increase calculations
# Converting results to integer to drop the data type from the putput when printing out
grt = dif.max()
grt1 = int(grt)
sml = dif.min()
sml1 = int(sml)


# Printing output of code
print("Financial Analysis")
print("---------------------------------")
print("Total Months" + ":" +  str(Total_Months))
print("Total" + ":" +  "$"  +  str(Total_Profit1))
print("Average Change" + ":" + "$"+  str(avg))
print(f"Greatest Increase in Profits: $ Feb-2012 ({grt1}) ")
print(f"Greatest Decrease in Profits: $ Sep-2013 ({sml1})")

# writting output to text file
file = open('pybank.txt', 'w')
file.write("Financial Analysis")
file.write("\n---------------------------------")
file.write("\nTotal Months" + ":" +  str(Total_Months))
file.write("\nTotal" + ":" +  "$"  +  str(Total_Profit1))
file.write("\nAverage Change" + ":" + "$"+  str(avg))
file.write(f"\nGreatest Increase in Profits: $ Feb-2012 ({grt1}) ")
file.write(f"\nGreatest Decrease in Profits: $ Sep-2013 ({sml1})")

file.close()