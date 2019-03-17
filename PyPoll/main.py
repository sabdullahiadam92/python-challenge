# Sumaya Abdullahi
# Data Analytics BootCamp - Cohort 3
# Homework 3 - PyPoll Challenge

#importing pandas and os modules
import os
import pandas as pd

#defining the csv data frame
df = pd.read_csv("pypoll.csv")

#storing calculations in varibales
voter_count = df['Voter ID'].count()
candidate_vote = df['Candidate'].value_counts()
candidate_percentage = (candidate_vote/voter_count)*100
winner = candidate_vote.idxmax()

#printing output
print("Election Results")
print("-------------------------------------------------------------")
print("Total Votes" + ":"  + str(voter_count))
print("-------------------------------------------------------------")
print("Khan:" + " " + str(round(candidate_percentage[0],3)) + "%" +  "("+str(candidate_vote[0])+")")
      
print("Correy:" + " " + str(round(candidate_percentage[1],3)) + "%" + "("+str(candidate_vote[1])+")")
      
print("Li:" + " " + str(round(candidate_percentage[2],3)) + "%" + "("+str(candidate_vote[2])+")")
      
print("O'Tooley:" + " " + str(round(candidate_percentage[3],3)) + "%" + "("+str(candidate_vote[3])+")")

print("--------------------------------------------------------------")
      
print("winner: " + winner)

# writting outputs to text file
file = open('pypoll.txt', 'w')
file.write("Election Results")
file.write("\n-------------------------------------------------------------")
file.write("\nTotal Votes" + ":"  + str(voter_count))
file.write("\n-------------------------------------------------------------")
file.write("\nKhan:" + " " + str(round(candidate_percentage[0],3)) + "%" +  "("+str(candidate_vote[0])+")")
      
file.write("\nCorrey:" + " " + str(round(candidate_percentage[1],3)) + "%" + "("+str(candidate_vote[1])+")")
      
file.write("\nLi:" + " " + str(round(candidate_percentage[2],3)) + "%" + "("+str(candidate_vote[2])+")")
      
file.write("\nO'Tooley:" + " " + str(round(candidate_percentage[3],3)) + "%" + "("+str(candidate_vote[3])+")")

file.write("\n--------------------------------------------------------------")
      
file.write("\nwinner: " + winner)

file.close()
