numberofScores = 0
score = 0
total= 0
scoreCount= 0
average= 0.0


numberofScores= int(input ("Please enter the number of scores you want to average: "))

#Add a while loop to make this code repeat until scoreCount = numberofScores

while (scoreCount < numberofScores):
    score= int(input ("Please enter a score:"))
    total= total + score
    scoreCount = scoreCount + 1 

#Average is needed to be casted as a string 
average= total / numberofScores
print ("The average of all tests scores is:" + str(average))


           
