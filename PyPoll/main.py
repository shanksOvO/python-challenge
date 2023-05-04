import os
import csv

# Path to the CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""

# Open the CSV file and read the data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # If candidate is not in dictionary, add them and set votes to 1
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1
        
# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = round(votes/total_votes * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    if winner == "" or votes > candidate_votes[winner]:
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
