#importing all the modules
import random
from flask import Flask, render_template, request
import pandas as pd
import numericalAssignment as nd
import pickle

#flage variables
ageGlobal = -1
religionGlobal = -1
communityGlobal = -1
professionGlobal = -1
incomeGlobal = -1
genderGlobal = -1
globalPrediction = -1
schemeEntered = False

# bot responses
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "heyy", "hey", "hye", "welcome", "helllo", "helluuu", "hellu", "what's going" "whats going", "hallo", "ola", "vanakam", "namasthe", "vanthanam", "namaskaram", " ", "", "undefined"]

GREETING_RESPONSES = ["hi...welcome to Schemebot service", "hey iam SchemeBot", "Heyyy", "hi there","hello...frd", "I am glad! You are talking to me", "Vanakam.....I am SchemeBot", "Namasthe bhaiyaa"]

SCHEME_INPUTS = ("scheme", "schemes", "scheme query")

SCHEME_RESPONSES = ["Finish the survey for available shcemes....Enter your age?","Answer the questions for prediciton of available schemes...How old are you?", "Answer the following for prediction? \nWhich is your age category?", "Finish the survey for available shcemes....Mention your age first?"]

RELIGION_QUERY = ["Select your religion?", "What is your religion?",
    "Name the religion that you belongs to?", "Which is your religion that you follow?"]

COMMUNITY_QUERY = ["What is your community?", "Select your community?",
    "Select your community below", "What is the community that you belongs to ?"]

INCOME_QUERY = ["What is your income?", "How much do you earn?",
    "What's your annual salary?", "Mention your salary ?"]

PROFESSION_QUERY = ["What is your current status?", "Select your current profession?", "Currently what are you doing?" ,"Enter your current profession?"]

GENDER_QUERY = ["What is your gender ?", "Enter your gender?", "The gender you belongs to", "Type your gender"]
#bot responses ended


# greeting function
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

#scheme details checking function
def schemeDetails(sentence):
    for word in sentence.split():
        if word.lower() in SCHEME_INPUTS:
            return random.choice(SCHEME_RESPONSES)

#Predicting the schemes with DecisionTree algorithm
def predicting(lst):
    loadedModel = pickle.load(open('mlModel','rb'))
    dF = pd.DataFrame(lst)
    dT =  dF.transpose()
    output = loadedModel.predict(dT)
    return output

#initializing the flask application
app = Flask(__name__)

# binding the index function to template
@app.route('/')
def index():
	return render_template('index.html')

# Function used to get the bot responses
@app.route('/get')
def get_bot_response():
	message = request.args.get('msg')
	message.lower()
	#to tell the interpreter about the global declaration
	global ageGlobal
	global religionGlobal
	global communityGlobal
	global incomeGlobal
	global genderGlobal
	global professionGlobal
	global globalPrediction
	global age
	global religion
	global community
	global profession
	global income
	global gender
	global schemeEntered
	global Sgender
	if(greeting(message) != None):
		response = random.choice(GREETING_RESPONSES)
		ageGlobal = -1
		religionGlobal = -1
		communityGlobal = -1
		professionGlobal = -1
		incomeGlobal = -1
		genderGlobal = -1
		globalPrediction = -1
		
	elif(schemeDetails(message) != None):
		schemeEntered = True  #flag variable
		response = random.choice(SCHEME_RESPONSES)
		ageGlobal = -1
		religionGlobal = -1
		communityGlobal = -1
		professionGlobal = -1
		incomeGlobal = -1
		genderGlobal = -1
		globalPrediction = -1
	elif ageGlobal == -1 and schemeEntered:
		age = message
		age = int(age)
		if age > 140:
			response = "What is this....please enter a valid age"
			return response
		else:
			print(age)
			print(type(age))
			ageGlobal += 1
			response = random.choice(RELIGION_QUERY) + """
				\n1.Hindu
				\n2.Muslim
				\n3.Christian
				\n4.Any Other
				Enter the choice: 
			"""
	elif religionGlobal == -1 and schemeEntered:
		religion = message
		religion = int(religion)
		if religion > 4:
			response = "Not the valid choice"
			return response
		else:
			religion = nd.assignNumberReligion(religion)
			print(religion)
			response = random.choice(COMMUNITY_QUERY) + """
				1.BC  
				2.Minority Class
				3.Tribal
				4.Adi dravidar
				5.Anyother
				Enter the choice: 
			"""
			religionGlobal += 1

	elif communityGlobal == -1 and schemeEntered:
		community = message
		community = int(community)
		if community > 5:
			response = "Not a valid choice"
			return response
		else:
			community = nd.assignNumberCommunity(community)
			print(community)
			response = random.choice(INCOME_QUERY) + """
				(eg. 72000, 71000, like this)
			"""
			communityGlobal += 1

	elif incomeGlobal == -1 and schemeEntered:
		income = message
		try:
			income = int(income)
		except:
			response = "Enter without any special characters"
			return response

		response = random.choice(GENDER_QUERY) + "\n1.Male\n2.Female\n3.Any Other Gender"
		incomeGlobal += 1

	elif genderGlobal == -1 and schemeEntered:
		Sgender = message
		Sgender = int(Sgender)
		if Sgender > 3:
			response = "Not a valid choice"
			return response
		else:
			gender = nd.assignNumberGender(Sgender)
			if Sgender == 2:
				response = """
				1.Student at school or college(Govt/Aided) 
				2.Woman tailor
				3.Deserted Woman
				4.Destitue Woman
				5.Widow
				6.Unmarried woman
				7.Divorced woman
				8.Pregnant woman
				9.Retired Government Employee
				10.Government Employee
				11.Unemployed
				12.Any Other
			"""
			else:
				response = """
				1.Student at school or college(Govt/Aided)
				2.Tribal with free house site pattas
				3.Junior lawyer
				4.Farmer
				5.Folk artist
				6.Co-operative Society Employees
				7.Retired Government Employee
				8.Citizen
				9.Government Employee
				10.son/daughter of folk artist
				11.Rancher
				12.Unemployed
				13.Any Other
				"""
			genderGlobal += 1


	elif professionGlobal == -1 and schemeEntered:
		profession = message
		profession  = int(profession)
		if profession > 12 and Sgender == 2:
			response = "Not a valid choice"
			return response
		elif (Sgender == 1 or Sgender == 3) and profession > 13:
			response = "Not a valid choice"
		else:
			if(Sgender == 2):
				profession = nd.assignFemaleProfession(profession)
			else:
				profession = nd.assignFemaleProfession(profession)
			print(profession)
			professionGlobal += 1
			response = "Thank you for answering...type '0k' to finish......and wait for 10 seconds" 	
	elif globalPrediction == -1 and schemeEntered:
		msg = message
		prediction = predicting([age, religion, community, income, profession, gender])
		print(prediction)
		response = "Available scheme =\t\t " + prediction[0] 
		globalPrediction += 1

	else:
		ageGlobal = -1
		religionGlobal = -1
		communityGlobal = -1
		professionGlobal = -1
		incomeGlobal = -1
		genderGlobal = -1
		globalPrediction = -1

		response = "Type 'scheme' to start the survey....."

	return str(response)


#main function to start the flask application
if __name__ == "__main__":
	app.run()
