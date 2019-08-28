from flask import Flask, render_template, redirect, url_for, request, json, session
from microservice2 import Template, Schedule
import pymysql
import mysql.connector
from mysql.connector import Error
import datetime

app = Flask(__name__, static_folder='app/static')
app.static_folder = 'static'
app.secret_key = 'session1'


######################################					ADD NEW TEMPLATE
@app.route('/addTemplate')
def addTemplate():
	ms2T = Template()

	return render_template('addNewTemplate.html', listServer = ms2T.listNamaServer(), 
		listOrg = ms2T.listNamaOrganisasi(), listKategori = ms2T.listKategori())
	

@app.route('/prosesAddNewTemplate', methods =['POST','GET'])
def addNewTemplate():
	if request.method == 'POST':
		ms2T = Template()

		kode_laporan 		= request.form['kodeLaporan']
		server_id 			= request.form['server']
		report_judul 		= request.form['namaLaporan']
		report_deskripsi 	= request.form['filter']
		report_header 		= request.form['jmlHeader']
		report_footer 		= request.form['jmlFooter'] 
		report_jmlTampilan 	= request.form['jmlTampilan']
		report_periode 		= request.form['periode']
		report_createDate	= datetime.datetime.now()
		report_userUpdate 	= 'testUser'
		report_lastUpdate 	= datetime.datetime.now()
		report_aktifYN 		= 'Y'
		org_id 				= request.form['organisasi'] 
		ktgri_id 			= request.form['kategori']
		report_printAllYN 	= request.form['printAll']
		report_createdUser  = 'testUser'

		
		ms2T.addNewTemplate(kode_laporan, server_id, report_judul, report_deskripsi,
						report_header, report_footer, report_jmlTampilan,
						report_periode, report_createDate, report_userUpdate, 
		                report_lastUpdate, report_aktifYN, org_id, ktgri_id,
		                report_printAllYN, report_createdUser)

		return redirect(url_for('menu'))



######################################					ADD NEW SCHEDULE
@app.route('/addSchedule')
def addSchedule():
	ms2T = Template()
	ms2S = Schedule()

	return render_template('addNewSchedule.html', listKodeReport = ms2T.listKodeReport(),
		listPIC = ms2S.namaPIC(), listPen = ms2S.namaPenerima())

@app.route('/prosesAddNewSchedule', methods=['POST','GET'])
def addNewSchedule():
	print( "===============/prosesAddNewSchedule===============")
	if request.method =='POST':
		ms2S = Schedule()

		kode_laporan = request.form['valKode']
		header = request.form['header']
		keterangan = request.form['keterangan']
		note = request.form['note']
		reportPIC = ''
		reportPenerima = ''
		grouping = request.form['grouping']
		jadwalBln = ''
		jadwalHari = ''
		jadwalTgl = ''
		queryId = ''
		org = ms2S.getOrgLaporan(kode_laporan)
		kategori = ms2S.getKategoriLaporan(kode_laporan)
		aktifYN = ''
		lastUpdate = ''

		for checkHari in ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']:
			if request.form.get(checkHari) is not None:
				if jadwalHari == '':
					jadwalHari += request.form.get(checkHari)
				else:
					jadwalHari +=  ", "+request.form.get(checkHari)
		print("Hari ",jadwalHari)

		for checkBulan in ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']:
			if request.form.get(checkBulan) is not None:
				if jadwalBln == '':
					jadwalBln += request.form.get(checkBulan)
				else:
					jadwalBln +=  ", "+request.form.get(checkBulan)
		print ("Bulan ",jadwalBln) 

		for checkTgl in ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27', 't28', 't29', 't30', 't31']:
			if request.form.get(checkTgl) is not None:
				if jadwalTgl == '':
					jadwalTgl += request.form.get(checkTgl)
				else:
					jadwalTgl +=  ", "+request.form.get(checkTgl)
		print ("Tanggal ",jadwalTgl)

		for checkPIC in ms2S.namaPIC():
			#print(checkPIC[0])
			if request.form.get(checkPIC[0]) is not None:
				if reportPIC == '':
					reportPIC += checkPIC[2]
				else:
					reportPIC += ", "+checkPIC[2]
		print ("PIC ",reportPIC)

		for checkPen in ms2S.namaPenerima():
			#print(checkPen[2])
			if request.form.get(checkPen[2]) is not None:
			    if reportPenerima == '':
			        reportPenerima += checkPen[2]
			    else:
			        reportPenerima += ", "+checkPen[2]
		print ("Penerima ", reportPenerima)      
		
		ms2S.addSchedule( kode_laporan, header, keterangan, note, reportPIC, reportPenerima, 
			grouping, jadwalBln, jadwalHari, jadwalTgl, org, kategori)

		return redirect(url_for('menu'))      





######################################					EDIT SCHEDULE
@app.route('/editSchedule', methods=['POST', 'GET'])
def formEditSchedule():
	
	ms2T = Template()
	ms2S = Schedule()

	if request.method == 'POST':

		# kode_laporan = request.form['valKode']

		# ms2T = Template()
		# ms2S = Schedule()

		# print(kode_laporan)
		return render_template('editSchedule.html', detailSchedule = ms2S.showDetailSchedule(kode_laporan))
		#return redirect (url_for('editSchedule', kode_laporan=kode_laporan,
							# detailSchedule = ms2S.showDetailSchedule()))

	
	return render_template('editSchedule.html', listKodeReport = ms2T.listKodeReport())	

@app.route('/prosesViewEditSchedule', methods =['POST','GET'])
def start():
	print( "===============/prosesViewEditSchedule===============")
	ms2T = Template()
	ms2S = Schedule()
	
	if request.method == 'POST':
		
		kode_laporan = request.form['valKode']

		ms2T = Template()
		ms2S = Schedule()
		ms2S.listMaker(kode_laporan)

		#return redirect (url_for('formEditSchedule', kode_laporan=kode_laporan))
		# return redirect (url_for('editSchedule', kode_laporan=kode_laporan,
		# 					detailSchedule = ms2S.showDetailSchedule(kode_laporan)))
		return render_template('editSchedule.html', kode_laporan=kode_laporan,
							detailSchedule = ms2S.showDetailSchedule(kode_laporan),
							listPIC = ms2S.namaPIC(), listPen = ms2S.namaPenerima())
	




	
	
	








@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/menu')
def menu():
    return render_template('home.html')

@app.route('/editProfile')
def editProfile():
	return render_template('changePass.html')



if __name__ == "__main__":
    app.run(debug=True)