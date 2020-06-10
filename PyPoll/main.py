import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

votes = []
candidates = []
each_candidate = []
votes_p_candidate = []
percentage_votes = []

t_votes = 0

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(int(row[0]))
        t_votes = len(votes)
        candidates.append(row[2])
    
    for each in set(candidates):
        each_candidate.append(each)
       
        votes_per = candidates.count(each)

        votes_p_candidate.append(votes_per)

        voting = (votes_per/t_votes)*100

        percentage_votes.append(voting)
        
    votes_for_winner = max(votes_p_candidate)
    winner = each_candidate[votes_p_candidate.index(votes_for_winner)]
   
#print(t_votes)
#print(each_candidate)
#print(winner)
#print(votes_for_winner)

print("Election Results")
print("----------------------------")
print("Total Votes :" + str(t_votes))
print("----------------------------")
for x in range(len(each_candidate)):
    print(each_candidate[x] + ": " + str(round(percentage_votes[x], 3)) +"% (" + str(votes_p_candidate[x])+ ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")

results = open('results.txt', 'w')
results.write("Election Results\n")
results.write("----------------------------\n")
results.write("Total Votes :" + str(t_votes) + "\n")
results.write("----------------------------\n")
for x in range(len(each_candidate)):
    results.write(each_candidate[x] + ": " + str(round(percentage_votes[x], 3)) +"% (" + str(votes_p_candidate[x])+ ")" + "\n")
results.write("----------------------------\n")
results.write("Winner: " + winner + "\n")
results.write("----------------------------\n")