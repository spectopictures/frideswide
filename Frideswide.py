#WELCOME TO Project Frideswide - The AI that learns with you
#Copyright (CC:BY 3) Max Brzezicki, FNS: Oxford Neurological Society

#***IMPORTS***
import random
import math
import numpy as np
import time

#***DATABASE***

#import here all the dabatabse required for this task and dump it into the table#
#main db of questions
questionsMain=[]



#db of possible definitions of what is supposed to be @easy @hard ((@random))
methodDefinitionsDB=[]
#db of possible distributions of E:H:R
methodDistributionDefinitionsDB=[]

#logbook
logBook=[]

#***SETTINGS***
sessionSettings={'Random':'YES'}
numberOfRights=0
numberOfWrongs=0


#***HOUSEKEEPING, UPDATING

def getTime():
	return time.strftime("%c")

def log(entry):
	logBook.append([entry,getTime()])

def generateListOfRanks(questionsMain):
	listOfRanks=[]
	for i in questionsMain:
		listOfRanks.append(i[4])
	return listOfRanks


#***GENERATING PRESENTATION METHODS

def generateMethodDefinition(questionsMain):
		
	listOfRanks=generateListOfRanks(questionsMain)	
	maxE=max(listOfRanks)
	minH=min(listOfRanks)
	randoms=["",""]
	

	#now we're going to prepare definitions of what is @easy @hard and @random
	try:
		randoms[0]=random.randrange(minH,maxE)
		randoms[1]=random.randrange(minH,maxE)
		randoms.sort
		randMethodDefinition = [["E",0,random.randrange(0,maxE)],["H",minH,random.randrange(minH,0)],["R",randoms[0],randoms[1]]]
		return randMethodDefinition
	except:
		#log(randMethodDefinition)
		randMethodDefinition = [["E",0,0],["H",0,0],["R",0,0]]
		return randMethodDefinition

def generateRandMethod():
	#now we're going to prepare a composition of 10 questions, ratio of E:H:R
	
	randMethod=[np.random.multinomial(10, [1/3.]*3, size=1),0]
	log(randMethod)	
	return randMethod
	

#***RANKING 

#EASY/DIFFICULT improvement + GOOD/WRONG composition improvement


#REWARD for Frideswide
def rankEverything():
	
	rewardV=(numberOfRights+numberOfWrongs)/10
	#Giving out prizes
	#(if we're playing with a new one)
	if sessionSettings['Random']=='YES':
		
		currentMethodDefinition[3]+=rewardV
		currentMethod[1]+=rewardV
		#Committing to the DB 
		methodDefinitionsDB.append(currentMethodDefinition)
		methodDistributionDefinitionsDB.append(currentMethod)
	


#THIS IS TODO




#PREPARING QUESTIONS

def prepareQuestions(currentMethodDefinition,currentMethod,questionsMain):
	#Pulling up IDs of @easy @hard and @random questions
	questionIDList=[]
	listofEasyIDs=[]
	listofHardIDs=[]
	listofRandomIDs=[]
	
	for x in questionsMain:
		if x[4]>=currentMethodDefinition[0][1] and x[4]<=currentMethodDefinition[0][2]:
			listofEasyIDs.append(x[0]-1)

	for x in questionsMain:
		if x[4]>=currentMethodDefinition[1][1] and x[4]<=currentMethodDefinition[1][2]:
			listofHardIDs.append(x[0]-1)

	for x in questionsMain:
		if x[4]>=currentMethodDefinition[2][1] and x[4]<=currentMethodDefinition[2][2]:
			listofRandomIDs.append(x[0]-1)

	
		
	log(["List of EasyIDs:", listofEasyIDs])
	log(["List of HardIDs:", listofHardIDs])
	log(["List of RandomIDs:", listofRandomIDs])
	
	#everyday I'm shufflin'

	random.shuffle(listofEasyIDs)
	random.shuffle(listofHardIDs)
	random.shuffle(listofRandomIDs)
	
	#trimmin'

	listofEasyIDs=listofEasyIDs[:(currentMethod[0][0][0])]
	listofHardIDs=listofHardIDs[:(currentMethod[0][0][1])]
	listofRandomIDs=listofRandomIDs[:(currentMethod[0][0][2])]
	
	log(["List of EasyIDs:", listofEasyIDs])
	log(["List of HardIDs:", listofHardIDs])
	log(["List of RandomIDs:", listofRandomIDs])


	#we could make sure that there's always 10 questions, but why? perhaps it's bettrer to leave it like that and let user generate a new session afterwards
	
	questionIDList=listofEasyIDs+listofHardIDs+listofRandomIDs
	log(questionIDList)
	return questionIDList


def getWrongAnswers(Qid,questionsMain):
	wrongIDs=[]
	for x in questionsMain:
		if x[0] != Qid:
			wrongIDs.append(x[0])
	random.shuffle(wrongIDs)
	wrongIDs=wrongIDs[:4]
	
	return wrongIDs

def displayQuestions(Qid,questionsMain):
	#question	
	
	try:
		#rightAnswer Qid
		rightAnswer=questionsMain[Qid][2]
		#wrongAnswers
		wrongAnswers=[]
		wrongIDs=getWrongAnswers(Qid,questionsMain)
		for x in wrongIDs:
			wrongAnswers.append(questionsMain[x][2])
		displayPack = [Qid, questionsMain[Qid][1], rightAnswer, wrongAnswers]
		return displayPack
	except:
		print("YEH, GOTCHA!")
		print(Qid)
		print(questionsMain[Qid][2])
		rightAnswer=questionsMain[Qid][2]
		#wrongAnswers
		wrongAnswers=[]
		wrongIDs=getWrongAnswers(Qid,questionsMain)
		for x in wrongIDs:
			wrongAnswers.append(questionsMain[x][2])
		displayPack = [Qid, questionsMain[Qid][1], rightAnswer, wrongAnswers]
		return displayPack
	
#RUNTIME!


def main(questionsMain,settingS):
	logBook.append(["I'm starting a new instance of Frideswide. Hello.", getTime()])
	
	


	#LET'S GET RUNNING, FRIDESWIDE!
	if settingS[0]=='FREEPLAY':
		currentMethodDefinition=generateMethodDefinition(questionsMain)
		currentMethod=generateRandMethod()
		questionIDList=prepareQuestions(currentMethodDefinition,currentMethod,questionsMain)
		print(questionIDList)
		#SUBMIT TO THE USER
		exporT=[]
		for x in questionIDList:
		
			exporT.append((displayQuestions(x,questionsMain)))

		#PROCESS USER OUTPUT
		#SUMMING UP
		#rankEverything(numberOfRights,numberOfWrongs)


		#LOGBOOK
		#for i in logBook:
		#	print(i)
		exportT=[]
		exportT.append(exporT)
		exportT.append(currentMethod)
		exportT.append(currentMethodDefinition)
		return exportT

	elif settingS[0]=='MAX':
		currentMethodDefinition=generateMethodDefinition(questionsMain)
		currentMethod=[[[5, 1, 4]],0]
		print(currentMethod)
		questionIDList=prepareQuestions(currentMethodDefinition,currentMethod,questionsMain)
		print(questionIDList)
		#SUBMIT TO THE USER
		exporT=[]
		for x in questionIDList:
		
			exporT.append((displayQuestions(x,questionsMain)))

		
		


		#LOGBOOK
		#for i in logBook:
		#	print(i)
		exportT=[]
		exportT.append(exporT)
		exportT.append(currentMethod)
		exportT.append(currentMethodDefinition)
		return exportT

	elif settingS[0]=='NORMAL':
		currentMethodDefinition=generateMethodDefinition(questionsMain)
#TODO THISSSSSSS
		currentMethod=[[settingS[1]],0]
		print(currentMethod)
		questionIDList=prepareQuestions(currentMethodDefinition,currentMethod,questionsMain)
		print(questionIDList)
		#SUBMIT TO THE USER
		exporT=[]
		for x in questionIDList:
		
			exporT.append((displayQuestions(x,questionsMain)))

		
		


		#LOGBOOK
		#for i in logBook:
		#	print(i)
		exportT=[]
		exportT.append(exporT)
		exportT.append(currentMethod)
		exportT.append(currentMethodDefinition)
		return exportT

