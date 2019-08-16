from flask import Flask, render_template, redirect, url_for, request, json, session, flash
import datetime
import pymysql
import random
import mysql.connector
from auth import auth_login
from mysql.connector import Error
from templatelaporan import TemplateLaporan


class RequestLaporan:
   
    def __init__(self):
        self.req_id = ''
        self.org_id = ''
        self.ktgri_id = ''
        self.req_kodeLaporan = ''
        self.req_judul = ''
        self.req_deskripsi = ''
        self.req_tujuan = ''
        self.req_tampilan = ''
        self.req_periode = ''
        self.req_deadline = ''
        self.req_file = ''
        self.req_PIC = ''
        self.req_penerima = ''
        self.sch_id = ''
        self.report_id = ''
        self.query_id = ''
        self.reqSch_hari = ''
        self.reqSch_bulan = ''
        self.reqSch_tanggal = ''
        self.reqSch_groupBy = ''
        self.reqSch_reportPIC = ''
        self.reqSch_orgNama = ''
        self.reqSch_ktgriNama = ''
        self.reqSch_lastUpdate = ''
        self.reqSch_aktifYN = ''
        self.reqSch_reportPenerima = ''
        
       
        

    #BUAT GENERATE REQUESTID SECARA OTOMATIS
    def get_numberID(self):
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
     
            cursor.execute('select count(req_id) from t_request where month(req_date) = month(now())')
            
            record = cursor.fetchone()
            clear = str(record).replace('(','').replace(',)','')
            return int(clear)

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")
        
    def generateRequestID(self):
        now  = datetime.datetime.now()
        requestID = 'REQ_'+str(now.strftime('%Y%m'))+str(self.get_numberID()).zfill(5)
        return requestID
    
    
    #BUAT MENDAPATKAN ORGANISASI DARI MYSQL
    def namaOrganisasi(self):
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
        
            listOrg = cursor.execute('select org_id, org_nama from m_organisasi where org_aktifYN = "Y" order by org_id')
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
                    
    #BUAT MENDAPATKAN KATEGORI DARI MYSQL
    def namaDept(self):
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
     
            cursor.execute('select ktgri_id, ktgri_nama from m_kategori where ktgri_aktifYN = "Y" Order by ktgri_id')
            
            listDept = cursor.fetchall()
   
            return listDept
            

        except Error as e :
                print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

    #BUAT MENAMPILKAN LIST PIC DARI MYSQL
    def namaPIC(self):
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
     
            cursor.execute(''.join(['select user_id, user_name, user_email from m_user where user_flag = "User" ']))
            
            listPIC = cursor.fetchall()

             
            return listPIC
            

        except Error as e :
                print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")
                    
    #BUAT MENAMPILKAN LIST REQUEST PADA /MENU
    def listRequestUser(self, username):
        #session['user_id'] = auth_login()
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
            cursor.execute  (''.join(['SELECT req_id ,IFNULL(req_judul,""), IFNULL(req_date,""),IFNULL(req_deadline,""), IFNULL(req_status,""), IFNULL(req_PIC,""), IFNULL(req_kodelaporan, "") from t_request WHERE req_status IN ("On Process" , "Waiting")  AND user_id="'+session['user_id']+'" ORDER BY req_id desc']))
            listReqUser = cursor.fetchall()
            return listReqUser
        
        except Error as e :
                print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

    # def convertToBinaryData(self, filename):      
    #     #Convert digital data to binary format
    #     with open(filename, 'rb') as file:
    #         binaryData = file.read()
    #     return binaryData           

    #BUAT NAMPILIN REQUEST YANG UDAH KELAR
    def listFinished(self, username):
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
            listFinished = cursor.execute(''.join(['SELECT req_kodeLaporan, req_judul, req_date, req_PIC FROM t_request WHERE req_status = "Finished" and user_id="'+session['user_id']+'"']))
            listFinished = cursor.fetchall()
            return listFinished

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
            print("MySQL connection is closed")

    #BUAT INSERT REQUEST BARU                
    def requestLaporanBaru(self, prog_id, user_id, org_id, ktgri_id, req_kodeLaporan, req_judul, req_deskripsi,
                           req_tujuan, req_tampilan, req_periode, req_deadline, req_file, req_PIC, req_penerima,
                           reqSch_hari, reqSch_bulan, reqSch_tanggal, 
                           reqSch_orgNama,reqSch_ktgriNama, reqSch_lastUpdate, reqSch_reportPIC, 
                           reqSch_aktifYN = 'Y', reqSch_groupBy = 'Dr. Andre Lembong', 
                           req_dateAccept = None, req_endDate=None, 
                           req_status='Waiting', req_prioritas='1'
                          ):
        self.req_id = self.generateRequestID()
        self.prog_id = prog_id
        self.user_id  = user_id
        self.org_id = self.namaOrganisasi()
        self.ktgri_id = ktgri_id
        self.req_kodeLaporan = req_kodeLaporan
        self.req_judul = req_judul
        self.req_deskripsi = req_deskripsi
        self.req_tujuan = req_tujuan 
        self.req_tampilan = req_tampilan
        self.req_periode = req_periode                                          
        self.req_deadline = req_deadline
        self.req_file = req_file
        self.req_date  = datetime.datetime.now()
        self.req_dateAccept = req_dateAccept
        self.req_endDate = req_endDate
        self.req_status = req_status
        self.req_PIC = req_PIC
        self.req_penerima = req_penerima
        self.req_prioritas = req_prioritas

        
        self.reqSch_hari = reqSch_hari
        self.reqSch_bulan = reqSch_bulan
        self.reqSch_tanggal = reqSch_tanggal
        self.reqSch_groupBy = reqSch_groupBy
        self.reqSch_reportPIC = self.namaPIC()
        self.reqSch_orgNama = self.namaOrganisasi()
        self.reqSch_ktgriNama = reqSch_ktgriNama
        self.reqSch_lastUpdate = datetime.datetime.now()
        self.reqSch_aktifYN = reqSch_aktifYN


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
            cursor.execute('INSERT INTO t_request VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (self.req_id, prog_id, user_id, org_id, ktgri_id, req_kodeLaporan, req_judul, req_deskripsi,
                           req_tujuan, req_tampilan, req_periode,req_deadline,req_file, self.req_date,
                            req_dateAccept, req_endDate, self.req_status, req_PIC, req_penerima, 
                            req_prioritas))
            connection.commit()

            print("Successed")

            cursor.execute('INSERT INTO t_reqSchedule VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                        (self.req_id, reqSch_hari, reqSch_bulan, reqSch_tanggal, reqSch_groupBy, reqSch_reportPIC, reqSch_orgNama, reqSch_ktgriNama, self.reqSch_lastUpdate, reqSch_aktifYN))
            connection.commit()

            record = cursor.fetchone()
            print ("Your connected...",record)

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")
             

    #BUAT INSERT REQUEST EDIT 
    def requestEditLap(self, prog_id, user_id,req_report, req_kodeLaporan, req_deskripsi,
                           req_tampilan, req_deadline, req_file, req_PIC, req_penerima,
                           req_dateAccept = None, req_endDate=None, req_status='Waiting', req_prioritas='1'):
        self.req_id = self.generateRequestID()
        self.prog_id = prog_id
        self.user_id  = user_id
        self.org_id = ''
        self.ktgri_id = ''
        self.req_kodeLaporan = req_kodeLaporan
        self.req_deskripsi = req_deskripsi
        self.req_tampilan = req_tampilan
        self.req_periode = ''                                         
        self.req_deadline = req_deadline
        self.req_file = req_file
        self.req_date  = datetime.datetime.now()
        self.req_dateAccept = req_dateAccept
        self.req_endDate = req_endDate
        self.req_status = req_status
        self.req_PIC = req_PIC
        self.req_penerima = req_penerima
        self.req_prioritas = req_prioritas
        self.last_report = TemplateLaporan().getDataReport(req_report)
        self.req_judul = self.last_report[1]
        self.req_tujuan = self.last_report[2]
        
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
            try:
                cursor.execute('INSERT INTO t_request VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (self.req_id, prog_id, user_id, self.org_id, self.ktgri_id, req_kodeLaporan, self.req_judul, req_deskripsi,
                           self.req_tujuan, req_tampilan, self.req_periode, req_deadline, req_file, self.req_date,
                            req_dateAccept, req_endDate, self.req_status, req_PIC, req_penerima, req_prioritas))
            except Error as e:
                print(e)
            connection.commit()

            record = cursor.fetchone()
            print ("Your connected...",record)

            flash('Request berhasil dibuat')

        except Error as e :
            print("Error while connecting file MySQL", e)
            flash('Error,', e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")


    def cancelRequest(self, request_id):
        self.cancel_request=''
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
            cursor.execute(''.join(['UPDATE t_request SET req_status = "Cancel"  WHERE req_id = "'+request_id+'"']))            
            
            connection.commit()
           
            cancel_request = cursor.fetchone()
           
            return cancel_request
        except Error as e : 
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

    
                          


    ##################################################################################################
    def availableTask(self):
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

            listAvailTask = cursor.execute('''SELECT req_id, req_judul, user_name, ktgri_nama,
                                        req_date, req_deadline, req_prioritas
                                        FROM t_request a
                                        LEFT JOIN m_user b
                                            ON  a.user_id = b.user_id
                                        LEFT JOIN m_kategori c
                                            ON  a.ktgri_id = c.ktgri_id
                                        WHERE req_status LIKE 'Waiting%' ORDER BY req_id desc''')
            listAvailTask = cursor.fetchall()


            for row in listAvailTask:
                requestId = row[0]
                requestJudul = row[1]
                requestNama = row[2]
                requestKategori = row[3]
                requestTanggal = row[4]
                requestDeadline = row[5]
                requstPrioritas = row[6]

            return listAvailTask
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
            print("MySQL connection is closed")

    def listTask(self):
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

            #listTask = cursor.execute(''.join(['SELECT req_id, req_judul, user_name, ktgri_nama, req_date, req_deadline, req_prioritas FROM t_request a LEFT JOIN m_user b ON  a.user_id = b.user_id LEFT JOIN m_kategori c ON  a.ktgri_id = c.ktgri_id WHERE req_PIC = "'+session['username']+'" ORDER BY req_id']))
            listTask = cursor.execute('SELECT req_id, req_judul, user_name, ktgri_nama, req_date, req_deadline, req_prioritas, req_status FROM t_request a LEFT JOIN m_user b ON  a.user_id = b.user_id LEFT JOIN m_kategori c ON  a.ktgri_id = c.ktgri_id WHERE req_status = "On Process" and req_PIC = "'+session['username']+'" ORDER BY req_id desc')
            listTask = cursor.fetchall()


            
            return listTask



        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
            print("MySQL connection is closed")



    #GATAU BUAT APA
    # def getRequestId(self):
    #         request_id = request.form['buttonDetail']
    #         try: 
    #             connection = mysql.connector.connect(
    #             host='localhost',
    #             database='cms_template',
    #             user='root',
    #             password='qwerty')
    #             if connection.is_connected():
    #                 db_Info= connection.get_server_info()
    #             print("Connected to MySQL database...",db_Info)

    #             cursor = connection.cursor()
         
    #             cursor.execute(''.join(['select req_id from t_request where req_id = "'+request_id+'"']))
                
    #             listKodeReport = cursor.fetchall()
                
    #             return listKodeReport

    #         except Error as e :
    #             print("Error while connecting file MySQL", e)
    #         finally:
    #                 #Closing DB Connection.
    #                     if(connection.is_connected()):
    #                         cursor.close()
    #                         connection.close()
    #                     print("MySQL connection is closed")


    def getDetailTask(self, request_id):
        self.detail_task=''
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
            cursor.execute(''.join(['SELECT a.req_id, req_judul, req_deskripsi, org_nama, ktgri_nama, req_tampilan, req_periode, req_deadline, req_file, reqSch_tanggal, reqSch_bulan, reqSch_hari  FROM t_request a LEFT JOIN m_organisasi b ON a.org_id = b.org_id LEFT JOIN m_kategori c ON a.ktgri_id = c.ktgri_id LEFT JOIN t_reqSchedule d ON a.req_id = d.req_id  WHERE a.req_id = "'+request_id+'"']))            
           

           
            detail_task = cursor.fetchone()
         
            return detail_task

        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")


    def accRequest(self, request_id):
        self.confirm=''
        self.accReq = datetime.datetime.now()
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

            cursor.execute('update t_request set req_dateAccept = "'+str(self.accReq)+'",req_status = "On Process", req_PIC = "'+session['username']+'" where req_id = "'+request_id+'"')

            connection.commit()
            confirmReq = cursor.fetchall()


            return confirmReq

            print ("Record Updated successfully ")
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

    # def finishRequest(self, request_id):
    #     self.finish_request =''
    #     try: 
    #         connection = mysql.connector.connect(
    #         host='localhost',
    #         database='cms_request',
    #         user='root',
    #         password='qwerty')
    #         if connection.is_connected():
    #             db_Info= connection.get_server_info()
    #         print("Connected to MySQL database...",db_Info)

    #         cursor = connection.cursor()
    #         cursor.execute(''.join(['UPDATE t_request SET req_status = "Finished"  WHERE req_id = "'+request_id+'"']))            
            
    #         connection.commit()
            
    #         finish_request = cursor.fetchone()
         
    #         return finish_request
    #     except Error as e :
    #         print("Error while connecting file MySQL", e)
    #     finally:
    #             #Closing DB Connection.
    #                 if(connection.is_connected()):
    #                     cursor.close()
    #                     connection.close()
    #                 print("MySQL connection is closed")

    def confirmRequest(self, request_id):
        self.confirm_request =''
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
            cursor.execute(''.join(['UPDATE t_request SET req_status = "Confirmed"  WHERE req_id = "'+request_id+'"']))            
            
            connection.commit()
            
            confirm_request = cursor.fetchone()
         
            return confirm_request
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

        # def availableTaskSPV(self):
        #     try:
        #         connection = mysql.connector.connect(
        #         host='localhost',
        #         database='cms_request',
        #         user='root',
        #         password='qwerty')
        #         if connection.is_connected():
        #             db_Info= connection.get_server_info()
        #         print("Connected to MySQL database...",db_Info)

        #         cursor = connection.cursor()

        #         listAvailTask = cursor.execute('''SELECT req_id, req_judul, user_name, ktgri_nama,
        #                                     req_date, req_deadline, req_prioritas
        #                                     FROM t_request a
        #                                     LEFT JOIN m_user b
        #                                         ON  a.user_id = b.user_id
        #                                     LEFT JOIN m_kategori c
        #                                         ON  a.ktgri_id = c.ktgri_id
        #                                     WHERE req_status LIKE 'Waiting%' ORDER BY req_id''')
        #         listAvailTask = cursor.fetchall()


        #         for row in listAvailTask:
        #             requestId = row[0]
        #             requestJudul = row[1]
        #             requestNama = row[2]
        #             requestKategori = row[3]
        #             requestTanggal = row[4]
        #             requestDeadline = row[5]
        #             requstPrioritas = row[6]

        #         return listAvailTask
        #     except Error as e :
        #         print("Error while connecting file MySQL", e)
        #     finally:
        #             #Closing DB Connection.
        #         if(connection.is_connected()):
        #             cursor.close()
        #             connection.close()
        #         print("MySQL connection is closed")


        #=========================================BUAT PANGGIL=======================================================================
        #RequestLaporan().requestSchedule('SCH-004', 'DGM-0330', 'Q123', 'Senin', 'Januari', '4','Dr. Andre Lembong',
        #                       'Monic', 'Pharos', 'Sales Management', datetime.datetime.now(), 'Y')        
        #           
        #RequestLaporan().requestLaporanBaru('BM-01', 'UU-01', '2', 'BD-01', 'DGM-001', 'Laporan Sales', 'filter<5000', 'untuk mengetahui',
        #                               'outcode', 'B1', datetime.date(2019,7,12), 'laporan', None, None,
        #                               'confirmed', 'Monic', 'jhgygvy', 'N')
        #

        #print(RequestLaporan().test())
        #print(RequestLaporan().prosesLogin('Monica','1234'))
        #print (RequestLaporan().getUserID('yoona'))

        #Programmer telah selesai mengerjakan request dan menginput kode Laporan untuk request tsb
    def listKodeLaporan(self):
        try:
            connection = mysql.connector.connect(
            host = 'localhost',
            database = 'cms_template',
            user = 'root',
            password = 'qwerty')
            if connection.is_connected():
                db_Info = connection.get_server_info()
            print("Connected to MySQL database...", db_Info)

            cursor = connection.cursor()
            cursor.execute('SELECT report_id from m_report')

            listKodeLap = cursor.fetchall()

            return listKodeLap
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed") 

    def finishRequest(self, request_id):
        self.finish_request =''
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
            cursor.execute(''.join(['UPDATE t_request SET req_status = "Finished"  WHERE req_id = "'+request_id+'"']))            
            
            connection.commit()
            
            finish_request = cursor.fetchone()
         
            return finish_request
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")    

    def inputKodeFinish(self, request_id, kodLap):
        self.endDate = datetime.datetime.now()
        
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
            cursor.execute(''.join(['UPDATE t_request SET req_endDate = "'+str(self.endDate)+'", req_kodeLaporan = "'+kodLap+'"  WHERE req_id = "'+request_id+'"']))            
            
            connection.commit()

            kode_finish = cursor.fetchone()

            return kode_finish
            
            print(request_id, kodLap)
         
            
        except Error as e :
            print("Error while connecting file MySQL", e)
        finally:
                #Closing DB Connection.
                    if(connection.is_connected()):
                        cursor.close()
                        connection.close()
                    print("MySQL connection is closed")

# print(RequestLaporan().listRequestUser("P190360"))
#print(RequestLaporan().listFinished("P190360"))