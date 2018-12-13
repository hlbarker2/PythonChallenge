import csv

#Define variables and create dictionaries to store candidate data
totalvotes = 0
winnervotes = 0
candidates = {}
candidatepercent = {}

#Open file with absolute path
file = '/Users/hannah/Desktop/BootCamp/Homework/pythonchallenge/PyPoll/election_data.csv'

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    #The total number of votes cast
    for row in csvreader:
        totalvotes = totalvotes + 1

#A complete list of candidates who received votes, and the total number of votes each candidate won
#Continue to loop through each row of the file to locate each candidate and count respective votes
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1

#The percentage of votes each candidate won
#Loop through candidates dictionary key, value pairs, and store information in candidatepercent dictionary
for candidate, votes in candidates.items():
    candidatepercent[candidate] = (votes/totalvotes) * 100
    candidatepercent[candidate] = '{:.4f}'.format(candidatepercent[candidate])

#The winner of the election based on popular vote
#Loop through keys in candidates dictionary
for candidate in candidates:
    if candidates[candidate] > winnervotes:
        winner = candidate
        winnervotes = candidates[candidate]
 
#Open in text file and terminal
outputfile = '/Users/hannah/Desktop/BootCamp/Homework/pythonchallenge/PyPoll/output.txt'

with open(outputfile, 'w') as writefile:
    writefile.writelines('Election Results\n')
    writefile.writelines('------------------\n')
    writefile.writelines(f'Total Votes: {totalvotes} \n')
    writefile.writelines('------------------\n')
    for candidate, votes in candidates.items():
        writefile.writelines(f'{candidate}: {candidatepercent[candidate]}% ({votes}) \n')
    writefile.writelines('------------------\n')
    writefile.writelines(f'Winner: {winner} \n')
    writefile.writelines('------------------\n')

with open(outputfile, 'r') as readfile:
    print(readfile.read())