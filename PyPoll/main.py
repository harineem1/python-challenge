# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:30:03 2018

@author: harin
"""

import csv
input_file = "Resources/election_data.csv"
output_file = "Resources/election_analysis.txt"
f= open(output_file,"w+")
total_votes = 0

candidates = []
candidate_votes = {}

with open(input_file) as election_data:
      reader = csv.DictReader(election_data)
      
      for row in reader:
          total_votes = total_votes + 1
          #Is this in my list of candidates
          if row["Candidate"] not in candidates:
              candidates.append(row["Candidate"])
              candidate_votes[row["Candidate"]] = 0
          candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1   

print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")

max_votes = 0
for key in candidate_votes:
    print (key,  str(round((100 * candidate_votes[key] / total_votes),3)) + "%("+ str(candidate_votes[key]) +  ")")
    if candidate_votes[key] > max_votes :
        winner = key
        max_votes = candidate_votes[key]
 
print("-------------------------")
print("winner =", winner)
print("-------------------------")
          

f.write("Election Results\n")
f.write("-------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")
for key in candidate_votes:
    f.write((key +  str(round((100 * candidate_votes[key] / total_votes),3)) + "%("+ str(candidate_votes[key]) +  ")\n"))
f.write("-------------------------\n")
f.write("winner = " + winner + "\n")
f.write("-------------------------\n")

          
         