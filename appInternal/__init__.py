from flask import Flask, render_template, redirect, url_for, request, json, session
from microservice2 import Template, Schedule
import pymysql
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, static_folder='app/static')
app.static_folder = 'static'
app.secret_key = 'session1'

@app.route('/editSchedule')
def editSchedule():
	ms2T = Template()

	return render_template('editSchedule.html', listKodeReport = ms2T.listKodeReport())

@app.route('/prosesViewEditSchedule', methods =['POST','GET'])
def start():
	# ms2T = Template()
	# ms2S = Schedule()
	
	if request.method == 'POST':
		
		kode_laporan = request.form['valKode']
		

		ms2T = Template()
		ms2S = Schedule()

		print(kode_laporan)
		return redirect (url_for('formEditSchedule', kode_laporan=kode_laporan))
		#return render_template('editSchedule.html',kode_laporan=kode_laporan, listKodeReport = ms2T.listKodeReport())
		
	

@app.route('/formEditSchedule')
def formEditSchedule():
	
	ms2T = Template()

	
	return render_template('editSchedule2.html')	


	
	
	








@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/menu')
def menu():
    return render_template('main.html')

@app.route('/editProfile')
def editProfile():
	return render_template('changePass.html')



if __name__ == "__main__":
    app.run(port=5001, debug=True)