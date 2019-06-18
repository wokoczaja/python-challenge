import os
import csv
electioncsv=os.path.join("Resources","Election_data.csv")
#Create list variables to store data
voter_count=[]
candidate=[]
percentage=[]


#Open file and read values into lists
with open(electioncsv,newline='') as csvfile:
    electionreader=csv.reader(csvfile,delimiter=',')

#Skip the header row
    next(electionreader)
#For each row in the list
    for row in electionreader:
        voter_count.append(row[0])
        candidate.append(row[2])

print("Election Results")
print("----------------------")

#Find total number of votes
total_votes=len(voter_count)
print("Total Votes: " + str(total_votes))
print("----------------------")

#Find complete list of candidates and number of votes per candidate
word_count={}.fromkeys(candidate,0)
for word in candidate:
    word_count[word]+=1
#print(word_count)

#Set-up write file for export
analysis=open('election_results.txt','w')
analysis.write('Election Results')
analysis.write('\n----------------------')
analysis.write('\nTotal Votes: '+str(total_votes))
analysis.write('\n----------------------')

#Find votes and percentage of votes per candidate using count
for key, value in word_count.items():
    percentage=[(value/total_votes)*100]
    roundedpercentage=[round(x,2) for x in percentage]
#    print(f"{key}:{value} {list(percentage)}") this works!
#    print(f"{key}: {value} {list(roundedpercentage)}%")
    print(f"{key}: {list(roundedpercentage)}%  ({value})")
    analysis.write(f"'\n{key}: {list(roundedpercentage)}%  ({value})")
print("----------------------")
analysis.write('\n----------------------')

#To find the candidate with the most votes
winner=max(word_count,key=word_count.get)
print('Winner:  '+str(winner))
print("----------------------")
analysis.write('\nWinner: '+str(winner))
analysis.write('\n----------------------')
analysis.close()










  
