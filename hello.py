from flask import Flask
from flask import render_template
from flask import request
from flask import g
import sqlite3 as sql
import Frideswide as FW

import urllib.parse as urlparse
from flask import session
from flask import session as SS1


from flask import flash, redirect, url_for
from rauth.service import OAuth2Service

import operator


#TODO
#[X} - Pre-clear the ID for SQL injection, just in case

#end TODO
	



# Flask config

SQLALCHEMY_DATABASE_URI = 'sqlite:///facebook.db'
SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
DEBUG = True
FB_CLIENT_ID = '103327000084425'
FB_CLIENT_SECRET = 'af60f02bfd6f6e6a60e9cfedaaa4b90e'

# Flask setup
app = Flask(__name__)
app.config.from_object(__name__)

# rauth OAuth 2.0 service wrapper
graph_url = 'https://graph.facebook.com/'
facebook = OAuth2Service(name='facebook', authorize_url='https://www.facebook.com/dialog/oauth', access_token_url=graph_url + 'oauth/access_token', client_id=app.config['FB_CLIENT_ID'], client_secret=app.config['FB_CLIENT_SECRET'], base_url=graph_url)


# views
@app.route('/ath')
def index():
	return render_template('login.html')

@app.route('/')
def index_0():
	return render_template('main_m.html')



@app.route('/facebook/login')
def login():
	redirect_uri = url_for('authorized', _external=True)
	params = {'redirect_uri': redirect_uri}
	return redirect(facebook.get_authorize_url(**params))


@app.route('/facebook/authorized')
def authorized():
	# check to make sure the user authorized the request
	if not 'code' in request.args:
		flash('You did not authorize the request')
		return redirect(url_for('index'))

	# make a request for the access token credentials using code
	redirect_uri = url_for('authorized', _external=True)
	data = dict(code=request.args['code'], redirect_uri=redirect_uri)

	session = facebook.get_auth_session(data=data)
	print('NOW!')
	me = session.get('me').json()
	
	SS1['id']=me['id']
	SS1['name']=me['name']
	sname=str.split(me['name'], ' ')
	SS1['firstname']=sname[0]
	baggu=createUser(me['id'],me['name'])
	if baggu=='yeh':
		return redirect(url_for('check'))
	
	else:
		return redirect(url_for('yoyo3'))





@app.route('/check')
def check():
	questionsMain2=updateALL()
	con = sql.connect('FWusers.db')
	con.row_factory = sql.Row   
	cur = con.cursor()
	cur.execute('SELECT * FROM users WHERE id='+SS1['id'])
	rows = cur.fetchall()
	stat2=[]
	for row in rows:
		stat2.append([row[3]])

	con.close()
	stat3=str.split(stat2[0][0], ',')
	
	if SS1['id']:
		statS=[]
		stat1=sorted(questionsMain2, key=operator.itemgetter(4))
		statS.append(stat1[0][1])
		statS.append(stat1[-1][1])
		statS.append(stat1[0][3])
		statS.append(stat1[1][3])
		
		#cheat!!! shouold be best topic
		stat4=(stat1[-4][1])
		stat5=stat1[-1][3]
		if not stat1[-1][3]:
			stat5='Not enough info';
		#end cheat!!!
		
		numberTotal=0
		numberDone=0
		for x in questionsMain2:
			numberTotal+=1
			if x[4]>=4:
				numberDone+=1
		statS.append(round((numberDone/numberTotal)*100,0))
		return render_template('main.html', FBname=SS1['name'], statS=statS, stat3=stat3, stat4=stat4, stat5=stat5)
	else:
		return render_template('loginFB.html')








#GLOBAL QUESTIONS
questionsMain=[]
con = sql.connect('FWdbase.db')
print ("Opened database successfully")
con.row_factory = sql.Row   
cur = con.cursor()
cur.execute('SELECT * FROM questionsALL')
rows = cur.fetchall()
for row in rows:
	questionsMain.append([row[0],row[1],row[2],row[3],row[4]])
con.close()



















#NOW LET'S UPDATE THE DATABASE OF QUESTIONS
def updateALL():
	if SS1['id']:
		print("IM PULLING HERE!!!")
		questionsMain0=[]
		con = sql.connect('FWusersDB.db')
		print ("Updated database successfully")
		con.row_factory = sql.Row   
		cur = con.cursor()
		cur.execute('SELECT * FROM questionsALL'+SS1['id'])
		rows = cur.fetchall()
		for row in rows:
			questionsMain0.append([row[0],row[1],row[2],row[3],row[4]])

		con.close()
		return questionsMain0



def deployALL(userID):
	questionsMain1=[]
	con = sql.connect('FWdbase.db')
	print ("Connected to the users database successfully")
	con.row_factory = sql.Row   
	cur = con.cursor()
	cur.execute('SELECT * FROM questionsALL')
	rows = cur.fetchall()
	for row in rows:
		questionsMain1.append([row[0],row[1],row[2],row[3],row[4]])

	con.close()
	con1 = sql.connect('FWusersDB.db')
	for row in questionsMain1:
		con1.execute('insert into questionsALL'+userID+' values (?, ?, ?, ?, ?)', [row[0], row[1], row[2], row[3], row[4]])	
	con1.execute("INSERT INTO methodALL"+userID+" VALUES('0','[[8 1 1]]','0')")
	con1.execute("INSERT INTO methodDefinitionsALL"+userID+" VALUES('0','[[E, 0, 0], [H, 0, 0], [R, 0, 0]]','0')")	
	con1.commit()
	
	

def createUser(FBid,FBuser):
	#Let's check that there's no-one like that first:
	con = sql.connect('FWusers.db')
	print ("Users database opened successfully")
	con.row_factory = sql.Row   
	cur = con.cursor()
	cur.execute('SELECT * FROM users WHERE id = ?', (FBid,))
	rows = cur.fetchall()
	if rows:
		#there's that person!
		return 'yeh'	
	else:
		con.execute('insert into users values (?, ?, ?, ?)', [FBid, FBuser, 'sg'+FBid, '0,0,0'])
		con.commit()
		con1 = sql.connect('FWusersDB.db')
		methodName='methodALL'+FBid
		methodName2='methodDefinitionsALL'+FBid
		methodName3='questionsALL'+FBid

		con1.execute('CREATE TABLE '+methodName+' (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `method` TEXT, `rankGlobal` INTEGER)')
		con1.execute('CREATE TABLE '+methodName2+' (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `method` TEXT, `rankGlobal` INTEGER)')
		con1.execute('CREATE TABLE '+methodName3+' (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `question` TEXT, `answer` TEXT, `genre` TEXT, `rate` INTEGER)')
	
		con1.commit()
		con1.close()
		deployALL(FBid)
	con.close()
	



def addGem():
	FBid=SS1['id']
	con = sql.connect('FWusers.db')
	print ("Users database opened successfully")
	con.row_factory = sql.Row   
	cur = con.cursor()
	cur.execute('SELECT * FROM users WHERE id = ?', (FBid,))
	rows = cur.fetchall()
	if rows:
		#there's that person!
		print("gemsy")
		print(rows[0][0])
		gem=int(rows[0][3][0])+1
		flag=int(rows[0][3][2])
		con.execute("UPDATE users SET personal='"+str(gem)+","+str(flag)+",0' WHERE id="+FBid)
		con.commit()
	

def addFlag():
	FBid=SS1['id']
	con = sql.connect('FWusers.db')
	print ("Users database opened successfully")
	con.row_factory = sql.Row   
	cur = con.cursor()
	cur.execute('SELECT * FROM users WHERE id = ?', (FBid,))
	rows = cur.fetchall()
	if rows:
		#there's that person!
		gem=int(rows[0][3][0])
		flag=int(rows[0][3][2])+1
		con.execute("UPDATE users SET personal='"+str(gem)+","+str(flag)+",0' WHERE id="+FBid)
		con.commit()

#GET ME THE BEST METHOD!!!
def getBestMethod(whicH):
	bestMethod=[]
	exitMethod=[]
	
	if SS1['id']:
		con = sql.connect('FWusersDB.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		print("GET ME HERE1")
		cur.execute('SELECT * FROM methodALL'+SS1['id']+' ORDER BY rankGlobal DESC')
		
	else:
		con = sql.connect('FWdbase.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		cur.execute('SELECT * FROM methodALL ORDER BY rankGlobal DESC')
	
	rows = cur.fetchall()
	
	bestMethod.append(rows[whicH][1])
	exitMethod.append(int(bestMethod[0][2]))
	exitMethod.append(int(bestMethod[0][4]))
	exitMethod.append(int(bestMethod[0][6]))
	con.close()
	
	return exitMethod


def updateMethod(Qid):
	updateMethod=[]
	if SS1['id']:
		con = sql.connect('FWusersDB.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		print("GET ME HERE2")

		cur.execute('SELECT * FROM methodALL'+SS1['id']+' WHERE method=?',[Qid])

	else:
		con = sql.connect('FWdbase.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		cur.execute('SELECT * FROM methodALL WHERE method=?',[Qid])
	rows = cur.fetchall()
	
	updateMethod.append(rows[0][2])
	con.close()
	return updateMethod

def updateMethodDefinitions(Qid):
	updateMethod0=[]
	if SS1['id']:
		con = sql.connect('FWusersDB.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		print("GET ME HERE3")
		cur.execute('SELECT * FROM methodDefinitionsALL'+SS1['id']+' WHERE method=?',[Qid])	
	else:	
		con = sql.connect('FWdbase.db')
		con.row_factory = sql.Row   
		cur = con.cursor()
		cur.execute('SELECT * FROM methodDefinitionsALL WHERE method=?',[Qid])
	
	rows = cur.fetchall()	
	updateMethod0.append(rows[0][2])
	con.close()
	return updateMethod0


def questionRank(Qid,rank):
	
	con = sql.connect('FWdbase.db')
	con.execute('UPDATE questionsALL SET rate = ? WHERE id=?', [rank,Qid])
	con.commit()
	con.close()
	if SS1['id']:
		con1 = sql.connect('FWusersDB.db')
		con1.execute('UPDATE questionsALL'+SS1['id']+' SET rate = ? WHERE id=?', [rank,Qid])
		con1.commit()
		con1.close()
	

def questionMethod(Qid,rank):
	
	con = sql.connect('FWdbase.db')
	con.execute('UPDATE methodALL SET rankGlobal = ? WHERE method=?', [rank,Qid])
	con.commit()
	con.close()
	if SS1['id']:
		con1 = sql.connect('FWusersDB.db')
		con1.execute('UPDATE methodALL'+SS1['id']+' SET rankGlobal = ? WHERE method=?', [rank,Qid])
		con1.commit()
		con1.close()
	
def questionMethodDefinition(Qid,rank):
	
	con = sql.connect('FWdbase.db')
	con.execute('UPDATE methodDefinitionsALL SET rankGlobal = ? WHERE method=?', [rank,Qid])
	con.commit()
	con.close()
	if SS1['id']:
		con1 = sql.connect('FWusersDB.db')
		con1.execute('UPDATE methodDefinitionsALL'+SS1['id']+' SET rankGlobal = ? WHERE method=?', [rank,Qid])
		con1.commit()
		con1.close()
	



def methodsRecord(table, toInsert):
		
	if SS1['id']:
		con = sql.connect('FWusersDB.db')
		print ("Opened database successfully again!")  
		cur = con.cursor() 
		cur.execute('SELECT * FROM methodALL'+SS1['id']+' WHERE method=?', [str(toInsert[0])])
	
		rows = cur.fetchall()
		if not rows:
			print("EEE")
			NULL= None
			con.execute('insert into methodALL'+SS1['id']+' values (?, ?, ?)', [NULL, str(toInsert[0]), 0])
			con.commit()
			
		con.close()	
	else:
		con = sql.connect('FWdbase.db')
		print ("Opened database successfully again!")  
		cur = con.cursor() 
		cur.execute('SELECT * FROM methodALL WHERE method=?', [str(toInsert[0])])
		
		rows = cur.fetchall()
		if not rows:
			print("EEE")
			NULL= None
			con.execute('insert into methodALL values (?, ?, ?)', [NULL, str(toInsert[0]), 0])
			
			con.commit()
	
		con.close()



def methodsDefinitionsRecord(table, toInsert):
	if SS1['id']:	
		con = sql.connect('FWusersDB.db')
		print ("Opened database successfully again!")  
		cur = con.cursor() 
		cur.execute('SELECT * FROM methodDefinitionsALL'+SS1['id']+' WHERE method=?', [str(toInsert)])
	
		rows = cur.fetchall()
		if not rows:
			print("EEE")
			NULL= None
			con.execute('insert into methodDefinitionsALL'+SS1['id']+' values (?, ?, ?)', [NULL, str(toInsert), 0])
			con.commit()
	
		con.close()
	else:
		con = sql.connect('FWdbase.db')
		print ("Opened database successfully again!")  
		cur = con.cursor() 
		cur.execute('SELECT * FROM methodDefinitionsALL WHERE method=?', [str(toInsert)])
	
		rows = cur.fetchall()
		if not rows:
			print("EEE")
			NULL= None
			con.execute('insert into methodDefinitionsALL values (?, ?, ?)', [NULL, str(toInsert), 0])
			con.commit()
	
		con.close()




@app.route('/quiz', methods=['GET'])

def quiz():
	if 1:
		if SS1:
			updateALL()
			#settings -> will be somewhere else
			quizData=[]
			quizData.append("MSK/CVS")
			quizData.append(120)
			quizData.append(13)
			quizData.append("mountan")
			
			#settingS=['FREEPLAY', getBestMethod(0)]
			settingS=['FREEPLAY', ' ']
			#getting FW to give us stuff
			exportT=FW.main(questionsMain,settingS)
			#questions from FW
		
			names0=exportT[0]
			
			#methods from FW
			methods0=exportT[1]
			methodsRecord("methodALL",methods0)
			#methodsDefinitions
			methodsDefinitions0=exportT[2]
			methodsDefinitionsRecord("methodDefinitionsALL",methodsDefinitions0)
			#counting how many questions
			numbers=0
			for x in names0:
				numbers+=1
			
			return render_template('hello.html', names=names0, numbers=numbers, quizData=quizData, methods0=methods0, methodsDefinitions0=methodsDefinitions0, SS1=SS1)
		else:
			return redirect(url_for('index_0'))
	#except:
		#return redirect(url_for('index_0'))
		#return 0


@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if 1:
		if SS1:
			questionsMain0=updateALL()
		
			print("ALLO")
			food=request.form['FWFoodContent']
			methods0=request.form['methods0']
			methodsDefinitions0=request.form['methodsDefinitions0']
			#Let's decipher the Qids
			listofQids=food.split(',')
			listofQids3=[]
			summaryB=0
			summaryA=0.000000000001
			for x in listofQids:
				listofQids2=x.split('!')
				listofQids3.append(listofQids2)
			for z in listofQids3:		
				try:
					print(z)
					summaryB+=int(z[1])
					summaryA+=1
					b=int(questionsMain0[int(z[0][3:])-1][4])+int(z[1])
					print('y2')
					questionRank(z[0][3:],b)
				except:
					print('now')
		
			#Let's decipher the method
			zzz=updateMethod(methods0)
			summaryTotal=summaryB/summaryA
			questionMethod(methods0,zzz[0]+summaryTotal)
		
			#Let's decipher the definitions
			yyy=updateMethodDefinitions(methodsDefinitions0)
			questionMethodDefinition(methodsDefinitions0,yyy[0]+summaryTotal)
			#listofQids3.sort(None,) ['ans90', '-1'], ['ans44', '1'], ['ans60', '-1'], ['ans43', '0'], ['ans35', '0'], ['ans61', '0'], ['']]
			listofQids3r=[]
			for x in listofQids3:	
				try:
					if x[1]:
						listofQids3r.append([int(x[1]),x[0]])
				except:
					0
			listofQids3r=sorted(listofQids3r)
			try:
				food=questionsMain[int(listofQids3r[0][1][3:])-1][1]
				food1=questionsMain[int(listofQids3r[-1][1][3:])-1][1]
			except:
				food="Too little info";		
				food1="Too little info";		
			addGem()
			addFlag()
			return render_template('hello2.html', food=food, food1=food1, methods0=methods0, score=round(summaryTotal,2), methodsDefinitions0=methodsDefinitions0, SS1=SS1 )
		else:
			return redirect(url_for('index_0'))
			
	#except:
		#return render_template('hello2.html', food=food, food1=food1, methods0=methods0, score=round(summaryTotal,2), methodsDefinitions0=methodsDefinitions0, SS1=SS1 )
		#return redirect(url_for('index_0'))
		

@app.route('/main')
def main0():
	return render_template('main.html')

@app.route('/start')
def main1():
	return render_template('yoyo.html')


@app.route('/yoyo2', methods=['GET'] )
def main2():
	
	try:
		methoda=request.args.get('METH')
		session['method']=methoda
	
		return render_template('yoyo2.html')
		
	except:	
		return render_template('yoyo2.html')



@app.route('/yoyo3')
def yoyo3():
	
	#print(SS1['id'])
	return render_template('yoyo4.html')



@app.route('/yoyo1')
def yoyo1():
	return render_template('yoyo3.html')








if __name__ == "__main__":
	app.run(debug=True)


	
