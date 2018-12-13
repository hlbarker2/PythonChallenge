import csv

#Create lists to store month and revenue data
months=[]
revenue=[]
oldrevenue = 0
revenuechanges = []

#Open file with absolute path
file = '/Users/hannah/Desktop/BootCamp/Homework/pythonchallenge/PyBank/budget_data.csv'

with open(file) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')

    next(csvreader)

    #Add month and revenue data to lists
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

        #Calculate average change with loop
        revenuechange = int(row[1]) - oldrevenue
        oldrevenue = int(row[1])

        revenuechanges.append(revenuechange)

    revenueavg = round(sum(revenuechanges)/len(revenuechanges),2)

#The total number of months included in the dataset
    totalmonths = len(months)

#The total net amount of "Profit/Losses" over the entire period
    totalrevenue = sum(revenue)

#The greatest increase in profits and decrease in losses (date and amount) over the entire period
greatestincrease = revenuechanges[0]
greatestdecrease = revenuechanges[0]

#Loop through indices to determine values for greatest increase and decrease
for item in range(len(revenuechanges)):
    if revenuechanges[item] >= greatestincrease:
        greatestincrease = revenuechanges[item]
        greatestincreasemonth = months[item]
    elif revenuechanges[item] <= greatestdecrease:
        greatestdecrease = revenuechanges[item]
        greatestdecreasemonth = months[item]

#Open in text file and terminal
outputfile = '/Users/hannah/Desktop/BootCamp/Homework/pythonchallenge/PyBank/output.txt'

with open(outputfile, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('------------------\n')
    writefile.writelines(f'Total Months: {totalmonths} \n')
    writefile.writelines(f'Total Revenue: ${totalrevenue} \n')
    writefile.writelines(f'Average Change: ${revenueavg} \n')
    writefile.writelines(f'Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease}) \n')
    writefile.writelines(f'Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease}) \n')

with open(outputfile, 'r') as readfile:
    print(readfile.read())