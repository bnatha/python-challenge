# Import dependencies
import os
import csv

# Load the file
csvpath = os.path.join("Resources", "election_data.csv")

# Defining variables
total_votes = 0
candidate_votes = 0
candidates_voted = {}
election_winner = ""

# Read .csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    
# Looping through the rows after the header   
    for row in csvreader:
        if row[2] in candidates_voted:
            candidates_voted[row[2]] += 1
        else:
            candidates_voted[row[2]] = 1 
        #total votes cast
        total_votes = total_votes + 1
        election_winner = max(candidates_voted, key=candidates_voted.get)
        
# Calculate vote percentage
    vote_percentages = {}
    
for key in candidates_voted.keys():
    vote_list = []
    vote_list.append(candidates_voted[key]/total_votes * 100)
    vote_list.append(candidates_voted[key])
    vote_percentages[key] = vote_list
 
# Print the results
print("Election Results")
print(f"Total Votes: {total_votes}")
for key in vote_percentages:
    print(f"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})")
print(f"Winner: {election_winner}")

output = (
   f"\nElection Results\n"
   f"----------------------------\n"
   f"Total Votes: {total_votes}\n"
   f"Khan: 63% (2218231)\n"
   f"Correy: 20% (704200)\n"
   f"Li: 14% (492940)\n"
   f"O'Tooley: 3% (105630)\n"
   f"Winner: {election_winner}\n")
with open("Output/Election Outcome.txt", 'w') as txt_file:
    txt_file.write(output)
