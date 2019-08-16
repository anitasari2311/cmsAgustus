from flask import Flask, render_template, redirect, url_for, request, json, session, flash
import auth
from microservice1 import RequestLaporan
from templatelaporan import TemplateLaporan
import pymysql
import mysql.connector
from mysql.connector import Error


app = Flask(__name__, static_folder='app/static')
app.static_folder = 'static'
app.secret_key = 'session1'

##########################                  LOGIN                          ############################

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))






#########################                   MICROSERVICE 1                 ###############################


## Menampilkan menu utama user
@app.route('/user', methods=['GET','POST'])
def user():
    # if request.method =='POST':
    #     request_id = request.form['btnCancel']

        
        listRequestLaporanUser = RequestLaporan()
        return render_template('menu.html', listReqUser = listRequestLaporanUser.listRequestUser(session['user_id']),
                            listKelar = listRequestLaporanUser.listFinished(session['user_id']))

### Cancel Detail Task to menuTaskProgrammer
@app.route('/cancelTask')
def cancelTask():
    return redirect(url_for('task'))



## Jika programmer mengklik tombol Finish pada menu Task Programmer
@app.route('/finishRequest', methods = ['POST'])
def finishRequest():
    if request.method == 'POST':
        finishreq = RequestLaporan()
        request_id = request.form['finishReq']
        kodLap = request.form['kodLap']
        return redirect(url_for("task"), finishreq.finishRequest(request_id)
                        , finishreq.inputKodeFinish(request_id, kodLap))


## Jika user mengklik tombol confirm
@app.route('/confirmRequest', methods = ['POST','GET'])
def confirmRequest():
    if request.method =='POST':
        confirm = RequestLaporan()
        request_id = request.form ['confirmReq']

        return redirect(url_for("user"), confirm.confirmRequest(request_id))






### Untuk Button Cancel di Menu User
@app.route('/cancel', methods = ['POST'])
def cancel():
    if request.method == 'POST':

        cancel = RequestLaporan()
        request_id = request.form['btnCancel']

        return redirect(url_for("user", listReqUser = cancel.listRequestUser(session['user_id']),cancel_request = cancel.cancelRequest(request_id)))


#BUAT CALL REQUEST
@app.route('/formRequest', methods=['GET', 'POST'])
def formRequest():
    newRequest = RequestLaporan()
    return render_template("requestLaporan.html", listOrg = newRequest.namaOrganisasi(), listDept = newRequest.namaDept(), listPIC = newRequest.namaPIC())

@app.route('/newReq', methods = ['POST'])
def newReq():
     if request.method == 'POST':
            reqSch_hari = ''
            reqSch_bulan = ''
            reqSch_tanggal = ''
            newRequest = RequestLaporan()
           
            title = request.form['inputTitle']
            purpose = request.form['inputPurpose']
            description = request.form['keteranganlaporan']
            Organization = request.form['Organization']
            Department = request.form['Department']
            Display = request.form['inputDisplay']
            Period = request.form['inputPeriode']
            # tanggalSelesai = request.form['tanggalSelesai']
            # bulanSelesai = request.form['bulanSelesai']
            # tahunSelesai = request.form['tahunSelesai']
            deadline = request.form['deadline']
            inputFile = request.form['inputFile']
            
            #PIC = request.form['boxPIC']
            
            #inputFile.save(secure_filename(f.filename))
            
            # report_id = request.form['']
            # query_id = request.form              reqSch_hari = request.form.get['hari']
            # for checkHari in ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Ming']:
            
            #     if request.form.get(checkHari) is not None:
            #         if reqSch_hari == '':
            #             reqSch_hari +=  request.form.get(checkHari)
            #         else:
            #             reqSch_hari +=  ", "+request.form.get(checkHari)
            # print (reqSch_hari)

            reqSch_hari = request.form.getlist('haritest')
            print(reqSch_hari)

            for checkBulan in ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agus', 'Sept', 'Okt', 'Nov', 'Des']:
                if request.form.get(checkBulan) is not None:
                    if reqSch_bulan == '':
                        reqSch_bulan += request.form.get(checkBulan)
                    else:
                        reqSch_bulan +=  ", "+request.form.get(checkBulan)
            print (reqSch_bulan) 
            for checkTgl in ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27', 't28', 't29', 't30', 't31']:
                if request.form.get(checkTgl) is not None:
                    if reqSch_tanggal == '':
                        reqSch_tanggal += request.form.get(checkTgl)
                    else:
                        reqSch_tanggal +=  ", "+request.form.get(checkTgl)
            print (reqSch_tanggal)

            flash('Request berhasil dibuat')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            # reqSch_groupBy = 'Dr. Andre Lembong'
            # reqSch_reportPIC = request.form['PIC']
            # reqSch_lastUpdate = None
            # reqSch_aktifYN = 'Y'


            newRequest.requestLaporanBaru( None, session['user_id'], Organization, Department, None, title, description,
                             purpose, Display, Period, deadline, "\bin", None, None,
                             reqSch_hari, reqSch_bulan, reqSch_tanggal,
                             Organization,Department, None, None)
            # newRequest.requestSchedule(reqSch_hari, reqSch_bulan, reqSch_tanggal, 'Dr. Andre Lembong',
            #                  None, None, 'Y')
           # return render_template("menu.html",listReqUser = newRequest.listRequestUser(session['username']))
            
            
            return redirect(url_for('user'))
#EDIT REQUEST
@app.route('/editRequest',methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        newRequest = TemplateLaporan()
        return render_template("Edit2.html", listKodeReport = newRequest.getReportID())
    
    
@app.route('/formEdit', methods=['POST','GET'])
def formEdit():
        newRequest = TemplateLaporan()
        session['kodeLaporan'] = request.form['kodeLaporan']
        print("test",session['kodeLaporan'])
        cur = newRequest.getCurrentDisplay(session['kodeLaporan'])
        return render_template("EditKolom.html",listcurrentdisplay = cur)

@app.route('/newEdit', methods = ['POST'])
def newEdit():
    if request.method == 'POST':
        newRequest = RequestLaporan()

        filterBaru = request.form['inputFilterBaru']
        newDisplay = request.form['inputNewDisplay']
        deadline = request.form['deadline']
        # tanggalSelesai = request.form['tanggalSelesai']
        # bulanSelesai = request.form['bulanSelesai']
        # tahunSelesai = request.form['tahunSelesai']
        #inputFile = request.form['inputFile']


        newRequest.requestEditLap( None, session['username'],session['kodeLaporan'], None, filterBaru,
                             newDisplay, deadline, "\bin",
                                None, None)
    
        return render_template("menu.html",listReqUser = newRequest.listRequestUser(session['username']))


# @app.route('/EditRev', methods = ['POST'])
# def newEdit():
#     if request.method == 'POST':
#         newRequest = RequestLaporan()
#         kodLap = request.form['submitRev']
#         filterBaru = request.form['inputFilterBaru']
#         newDisplay = request.form['inputNewDisplay']
#         deadline = request.form['deadline']
#         # tanggalSelesai = request.form['tanggalSelesai']
#         # bulanSelesai = request.form['bulanSelesai']
#         # tahunSelesai = request.form['tahunSelesai']
#         #inputFile = request.form['inputFile']


#         newRequest.requestEditLap( None, session['user_id'],kodLap, 'K271', filterBaru,
#                              newDisplay, deadline, "\bin", None, None)
        
#         return redirect(url_for("menu"), listReqUser = newRequest.listRequestUser(session['username']))
#         #return render_template("menu.html")


@app.route('/revisi', methods = ['GET', 'POST'])
def revisi():
    revisi = TemplateLaporan()
    revisi_id = request.form['btnRevisi']
    cur = revisi.getRevisiDisplay(revisi_id)
    return render_template("EditRevisi.html",listrevisidisplay = cur)









#######################                  MICROSERVICE 2             #################################


@app.route('/menu2')
def menu2():
    return render_template('taskSPV.html')

@app.route('/task')

def task():
    availTask = RequestLaporan()
    return render_template('task2.html', listAvailTask = availTask.availableTask(), listTask = availTask.listTask()
                           ,listKodeLap = availTask.listKodeLaporan())

@app.route('/detailReq', methods=['GET', 'POST'])
def detailReq():
    detTask = RequestLaporan()
    request_id = request.form['buttonDetail']
    cur = detTask.getDetailTask(request_id)
    return render_template('detailTask.html', detail_task = cur)


###########################################PROSES
@app.route('/authLogin', methods=['GET','POST'])
def authLogin():
    auth.auth_login()
    return auth.auth_login()


@app.route('/listAvailTask', methods=['GET','POST'])
def listAvailTask():
    microservice2.listTask()
    return microservice2.listTask()

# @app.route ('/openDetail', methods=['GET','POST'])
# def openDetail():
#     RequestLaporan().detailTask()
#     return RequestLaporan().getDetailTask()

@app.route('/accRequest', methods = ['POST','GET'])
def confirm1():
    if request.method == 'POST':

        confirm = RequestLaporan()
        request_id = request.form['btnConfirmReq']

        return redirect(url_for("task",  confirmReq = confirm.accRequest(request_id)))
        








if __name__ == "__main__":
    app.run(debug=True)
