#Ethan Camacho Match-Maker
from abc import abstractclassmethod


INTRODUCTION = '''
******************************************************
                    Matchmaker 3.0
          Helping you find luv since 2021
                    Cupidsoft, Inc.
******************************************************

This program figures out if you and I are meant to be.
You will answer 5 questions. To each question, answer 5
if you strongly agree, 4 if you agree, 3 if you neither
agree nor disagree, 2 if you disagree, and 1 if you
strongly disagree.

'''
QUESTION = [ 
'Do you like watching basketball?',
'Do you enjoy watching Anime?',
'Do you like running?',
'Do you enjoy playing sports?',
'Do you like Dogs?',
]
DESIRED_RESPONSE = [ 
    5, #strongly agree
    2, # disagree
    1, #Strongly disagree
    5,#strongly agree
    1  #strongly disagree
]
MAX_SCORE = 5 * len(QUESTION)
 
print(INTRODUCTION)

#Ask all questions
response = []
compatibility = []

for i in range(len(QUESTION)):     
 userResponse = int(input(QUESTION[i]))

response.append(userResponse)

questionCompatibility = 20 - abs(userResponse - DESIRED_RESPONSE[i])
compatibility.append(questionCompatibility)

# String FOrmatting with parameters and placeholders.
print ('Total %d Score: %d\n' % (i+1, questionCompatibility) )

#userResponse1 = int(input(QUESTION[0]))
   # compatability1 = 5 - abs(userResponse1 - DESIRED_RESPONSE[0])
   # print("Question 1 compatability:" + str(compatability1)) 


totalCompatibility = 0
for c in compatibility:
        totalCompatibility += c
        totalCompatibility *= 100 / MAX_SCORE
        print("80 and higher is the one I've been trying to find: %d\n\n" % (totalCompatibility))
        print("70 and lower we can be friends: %d\n\n" % (totalCompatibility))





       
           







#userResponse1 = int(input(QUESTIONS[0]))
#userresponse1 = int(input(QUESTION[0]))
#compatability1 = 5 - abs(userresponse1 - DESIRED_RESPONSE[0])
#print("Calculating " + str(compatability1))


#compatability2 = 5 - abs(userresponse2 - DESIRED_RESPONSE[1])
#print("Calculating " + str(compatability2))


#userresponse3 = int(input(QUESTION[2]))
#compatability3 = 5 - abs(userresponse3 - DESIRED_RESPONSE[2])
#print("Calculating " + str(compatability3))


#userresponse4 = int(input(QUESTION[3]))
#compatability4 = 5 - abs(userresponse4 - DESIRED_RESPONSE[3])
#print("Calculating " + str(compatability4))


#userresponse5 = int(input(QUESTION[4]))
#compatability5 = 5 - abs(userresponse5 - DESIRED_RESPONSE[4])
#print("Calculating " + str(compatability5))

#totalCompatability = (compatability1 + compatability2 + compatability3 + compatability4 + compatability5 ) * 10
#print("Total compatability:" + str(totalCompatability)