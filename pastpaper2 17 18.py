# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:37:44 2020

@author: lisa_
"""
#2

file = open("password.txt","r")

UserIDInput = input("Please enter an ID: ")
PasswordInput = input("Please enter a password: ")

UserIDFound = False
PasswordValid = False

for i in file.readlines():
    MyList = i.split()
    if UserIDInput == MyList[0] and PasswordInput == MyList[1]:
        UserIDFound = True
    
if UserIDFound == True:
    PasswordValid = True

#3

def StringClean(InString):
    OutString = ""
    for n in range(len(InString)):
        NextChar = InString[n]
        NextChar = NextChar.lower()
        if "a" <= NextChar <= "z":
            OutString = OutString + NextChar
    return OutString

#5c

def SearchFile():
    ArrayRow = 0
    file = open("Loginfile.txt", "r")
    SearchID = input("Please enter an ID: ")
    for i in file.readlines():
        if SearchID == i[:4]:
            LoginEvents[ArrayRow, 0] = i[5:9]
            LoginEvents[ArrayRow, 1] = i[-14:]
            ArrayRow += 1
    file.close()

#6b

def ValidatePassword(InString):
    flag = True
    LCaseChar = 0
    UCaseChar = 0
    NumChar = 0
    for i in range(0, len(InString)):
        NextChar = InString[i]
        if "a" <= NextChar <= "z":
            LCaseChar += 1
        elif "A" <= NextChar <= "Z":
            UCaseChar += 1
        else:
            if "0" <= NextChar <= "9":
                NumChar += 1
            else:
                flag = False
    if not (LCaseChar >= 2 and UCaseChar >= 2 and NumChar >= 3):
        flag = False

#5

def AddNewScores():
    ScoreData = input("Input the data: ")
    file = open("ScoreDetails.txt", "a")
    MembershipNumber = input("Input the membership number: ")
    while not MembershipNumber =="":
        Score = input("Input the score: ")
        while int(Score)<50 or int(Score)>99:
            Score = input("Input a valid score from 50 to 99: ")
        FileData = MembershipNumber + ScoreData + Score
        file.write(FileData)
        MembershipNumber = input("Input the membership number:")
    file.close()
'''  
#6

'''
def Lighten():
    BurnFlag = False
    for i in range(8):
        for j in range(8):
            OldPixelValue = Picture[i,j]
            PixelTemp = OldPixelValue * 1.1
            NewPixelValue = int(PixelTemp)
            if NewPixelValue >= 255:
                NewPixelValue = 255
                BurnFlag = True
            Picture[i,j] = NewPixelValue

#7

def ProcessMark(Mark):
    Total = 0
    Highest = Mark[0]
    Position = 0
    for i in range(20):
        Total += Mark[i]
        if Mark[i] > Highest:
            Highest = Mark[i]
            Position = 1
    Average = Total / 20
    print("The average mark is ", Average, " and the highest mark is ", Highest)
    return Position
