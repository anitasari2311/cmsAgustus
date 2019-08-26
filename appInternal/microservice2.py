from flask import Flask, render_template, redirect, url_for, request, json, session
import datetime
import pymysql
import random
import mysql.connector
from mysql.connector import Error
import json


class Template:

    def __init__(self):
        self.KodeLaporan = ''
        self.namaLaporan = ''
        self.namaOrganisasi = ''
        self.namaKategori = ''
        self.namaServer = ''
        self.deskripsi = ''
        self.jumlahKolom = ''
        self.jumlahHeader = ''
        self.jumlahFooter = ''
        self.periode = ''
        self.printAll = ''

    def listKodeOrgServ(self):
        try: 
            connection = mysql.connector.connect(
            host='localhost',
            database='cms_template',
            user='root',
            password='qwerty')
            if connection.is_connected():
                db_Info= connection.get_server_info()
            print("Connected to MySQL database...",db_Info)

            cursor = connection.cursor()

            
            listKodeOrgServ = cursor.execute('select report_id, server_nama, org_nama from M_report a LEFT JOIN cms_request.m_organisasi c ON a.Org_id = c.org_id  left join M_server b ON b.server_id = a.server_id')
            listKodeOrgServ = cursor.fetchall()

            

            for row in listKodeOrgServ:
                    repId = row[0]
                    servName = row[1]
                    orgName = row[2]

            x = {
            "kodeReport": row[0],
            "namaServ": row[1],
            "namaorg": row[2]
            }

            y = json.dumps(x)
             
            print(y) 
            return listKodeReport
            
        
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
            #Closing DB Connection.
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()
            print("MySQL connection is closed")


    def listKodeReport(self):
        try: 
            connection = mysql.connector.connect(
            host='localhost',
            database='cms_template',
            user='root',
            password='qwerty')
            if connection.is_connected():
                db_Info= connection.get_server_info()
            print("Connected to MySQL database...",db_Info)

            cursor = connection.cursor()

            listKodeReport = cursor.execute('select report_id from m_report')
            #listKodeReport = cursor.execute('select report_id, server_nama from M_report  a left join M_server b ON b.server_id = a.server_id;')

            listKodeReport = cursor.fetchall()

            for row in listKodeReport:
                repId = row[0]
                

            
            return listKodeReport
        
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
            #Closing DB Connection.
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()
            print("MySQL connection is closed")


        #Mengambil nama organisasi spesifik
    def listNamaOrganisasi(self, report_id):
        self.list_org = ''
        # if request.method == 'POST':
        report_id = request.form['valKode']
    
        try: 
            connection = mysql.connector.connect(
            host='localhost',
            database='cms_request',
            user='root',
            password='qwerty')
            if connection.is_connected():
                db_Info= connection.get_server_info()
            print("Connected to MySQL database...",db_Info)

            cursor = connection.cursor()

            listOrg = cursor.execute('SELECT org_nama FROM cms_template.m_report t1 JOIN cms_request.m_organisasi t2 ON t2.org_id = t1.org_id WHERE report_id ="' +report_id+'"')
            #listOrg = cursor.execute('select org_id, org_nama from m_organisasi where org_aktifYN = "Y" order by org_id')            
            listOrg = cursor.fetchall()

            return listOrg

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
        #Closing DB Connection.
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()
            print("MySQL connection is closed")


        #Mengambil nama server spesifik
    def listNamaServer(self):
        try: 
            connection = mysql.connector.connect(
            host='localhost',
            database='cms_template',
            user='root',
            password='qwerty')
            if connection.is_connected():
                db_Info= connection.get_server_info()
            print("Connected to MySQL database...",db_Info)

            cursor = connection.cursor()

            listServer = cursor.execute('SELECT server_id, server_nama from m_server where server_aktifYN ="Y" order by server_id')

            listServer = cursor.fetchall()

            return listServer

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
        #Closing DB Connection.
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()
            print("MySQL connection is closed")



        #Mengambil list kategori
        def listKategori():
            db = get_cms_request()
            cursor = db.cursor()

            listKategori = cursor.execute('SELECT kategori_nama from m_kategori')

            return listKategori
        #Template
    #         def addNewTemplate(self):

    #             kodeLaporan = request.form['XXXX']
    #             namaOrganisasi = request.form['XXXX']
    #             namaServer = request.form['XXXX']
    #             namaLaporan = request.form['XXXX']
    #             jumlahKolom = request.form['XXXX']
    #             jumlahHeader = request.form['XXXX']
    #             jumlahFooter = request.form['XXXX']
    #             periode = request.form['XXXX']
    #             printAll = request.form['XXXX']

    #             cursor = connection.cursor()

    #             sql = 'INSERT INTO m_report VALUES %s, %s, %s, %s, %s, %s, %s, %s, %s '
    #             val = kodeLaporan, namaOrganisasi, namaServer, namaLaporan, jumlahKolom, jumlahHeader, jumlahFooter, periode, printAll

    #             cursor.execute(sql,val)

    #             connection.commit()

    #             print("Template berhasil dibuat")


    #         def addQuery(self):

    #             kodeLaporan = request.form['']

    #             q1 = request.form['XXXX']
    #             q2 = request.form['XXXX']
    #             q3 = request.form['XXXX']
    #             q4 = request.form['XXXX']
    #             q5 = request.form['XXXX']
    #             q6 = request.form['XXXX']
    #             q7 = request.form['XXXX']
    #             q8 = request.form['XXXX']
    #             q9 = request.form['XXXX']
    #             q10 = request.form['XXXX']
    #             q11 = request.form['XXXX']
    #             q12 = request.form['XXXX']
    #             q13 = request.form['XXXX']
    #             q14 = request.form['XXXX']

    #             cursor = connection.cursor()

    #             sql = 'INSERT INTO XXTABLEXX VALUES %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s WHERE XLAPORANIDX =' +kodeLaporan+
    #             val = q1, q2, namaServer, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14

    #             cursor.execute(sql,val)
    #             connection.commit()

    #             print("Query telah berhasil disimpan")



    # #Perubahan
    #         def editTemplate(self, kodeLaporan, namaOrganisasi, namaServer):
    #             q1 = request.form['XXXX']
    #             q2 = request.form['XXXX']
    #             q3 = request.form['XXXX']
    #             q4 = request.form['XXXX']
    #             q5 = request.form['XXXX']
    #             q6 = request.form['XXXX']
    #             q7 = request.form['XXXX']
    #             q8 = request.form['XXXX']
    #             q9 = request.form['XXXX']
    #             q10 = request.form['XXXX']
    #             q11 = request.form['XXXX']
    #             q12 = request.form['XXXX']
    #             q13 = request.form['XXXX']
    #             q14 = request.form['XXXX']

    #             cursor = connection.cursor()

    #             sql = 'UPDATE m_report set ' +kodeLaporan+
    #             val = q1, q2, namaServer, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14

    #             cursor.execute(sql,val)
    #             connection.commit()

    #             print("Query telah berhasil disimpan")


    ###############################################################################################

class Schedule:
    def __init__(self):
        self.kode_laporan = ''
        self.organisasi = ''
        self.server = ''
        self.kategori = ''
        self.header = ''
        self.keterangan = ''
        self.note = ''
        self.penerima = ''
        self.reportPIC = ''
        self.grouping = ''
        self.jadwal = ''
        self.orderby = ''
        



    def showDetailSchedule(self):
        self.kode_laporan = ''
        
        try:
            connection = mysql.connector.connect(
            host = 'localhost',
            database = 'cms_template',
            user = 'root',
            password = 'qwerty'
            )

            if connection.is_connected():
                db_Info= connection.get_server_info()
            print("Connected to MySQL database...",db_Info)

            cursor = connection.cursor()

            cursor.execute('SELECT report_judul, report_deskripsi, sch_note, sch_reportPIC, sch_penerima, sch_groupBy, sch_aktifYN from t_schedule a LEFT JOIN m_report b ON b.report_id = a.report_id WHERE b.report_id = "'+kode_laporan+'" ')


            detailSchedule = cursor.fetchall()

            return detailSchedule

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
        #Closing DB Connection.
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()
            print("MySQL connection is closed")



#     #Untuk membuat schedule baru
#     def addSchedule():
#         kode_laporan = request.getform['']
#         organisasi = request.getform['']
#         server = request.getform['']
#         kategori = request.getform['']
#         header = request.getform['']
#         keterangan = request.getform['']
#         note = request.getform['']
#         penerima = request.getform['']
#         grouping = request.getform['']
#         orderby = request.getform['']
#         jadwal = request.getform['']

#         sql = 'INSERT INTO m_schedule VALUES %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
#         val = kode_laporan, organisasi, server, kategori, header, keterangan, note, penerima, grouping, orderby, jadwal

#         cursor.execute(sql,val)

#         db.commit()




#     #Untuk menampilkan List Edit Schedule
#     def viewEditSchedule(self, kode_laporan, organisasi, server, kategori):
#         db = get_cms_schedule()

#         cursor = db.cursor()

#         view_schedule = cursor.execute('SELECT header, keterangan, note, penerima, grouping, jadwal, aktifYN from m_schedule')

#         for row in view_schedule:
#             header = row[0]
#             keterangan = row[1]
#             note = row[2]
#             penerima = row[3]
#             grouping = row[4]
#             jadwal = row[5]
#             aktifYN = row[6]


#         return view_schedule


#     #Menginput hasil edit schedule
#     def editSchedule():
#         header = request.getform['']
#         keterangan = request.getform['']
#         note = request.getform['']
#         penerima = request.getform['']
#         grouping = request.getform['']
#         orderby = request.getform['']
#         jadwal = request.getform['']

#         sql = 'INSERT INTO m_schedule VALUES %s, %s, %s, %s, %s, %s, %s'
#         val = kode_laporan, organisasi, server, kategori, header, keterangan, note, penerima, grouping, orderby, jadwal

#         cursor.execute(sql,val)

#         db.commit()

#     #
#     def runScheduleToday():

#         db = get_cms_schedule
#         cursor = db.cursor()

#         sql = '"SELECT kodeLap, organisasi, kategori, penerima from m_schedule WHERE jadwal = "'+ getdate()+''

#         run_today = cursor.execute(sql)


#     def successRunSchedule():

#         ERROR = NONE

#     def failRunSchedule():
#         ERROR
