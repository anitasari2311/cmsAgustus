from flask import Flask, render_template, redirect, url_for, request, json, session
from microservice2 import Template
import pymysql
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, static_folder='app/static')
app.static_folder = 'static'
app.secret_key = 'session1'

##########################                  LOGIN                          ############################

@app.route('/editSchedule')
def start():
	ms2 = Template()
	if request.method == 'POST':
		
		ms2 = Template()
		# report_id = request.form['kodeReport']
		# server_id = ms2.listNamaOrganisasi()
		return redirect(url_for("editSchedule2"))
	return render_template('editSchedule.html', listKodeReport = ms2.listKodeReport())
	

@app.route('/editSchedule2')
def editSchedule():
	if request.method == 'POST':
		report_id = request.form['valKode']

		ms2 = Template()

		return render_template('editSchedule.html', listKodeReport = ms2.listKodeReport(), listOrg = listNamaOrganisasi(report_id))
	
	


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




if __name__ == "__main__":
    app.run(debug=True)