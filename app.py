from flask import Flask, render_template, request, redirect, flash, url_for, session, g, Response, send_file, make_response
import pymongo
import os
from pymongo import MongoClient
import requests
import pandas as pd
import json
import time
import datetime
import math
import gspread as gs
from werkzeug.security import generate_password_hash, check_password_hash
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import xlsxwriter
import pdfkit
import smtplib
from email.message import EmailMessage
import myEnvVal
import math
import random

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'skn-hackclub-287609-4a1b8cc8cdf4.json', scope)
gc = gs.authorize(credentials)

app = Flask(__name__)


app.config.from_pyfile('config.cfg')
mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')

API_KEY = os.environ.get('API_KEY')
myclient = pymongo.MongoClient(API_KEY) #imp


mydb = myclient["Yashdb1"]
mycol = mydb["Yashdb1"]

mydb1 = myclient["app"]
mycol1 = mydb["users1"]

myEnvVal.setVar()

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/google6d50026f7b3d14d5.html')
def google6d50026f7b3d14d5():
    return render_template('google6d50026f7b3d14d5.html')


@app.route('/signup', methods=['GET'])
def register_page():
    ishwar_tu_chutiya_hain = '8602842290'
    return render_template('signup.html', ishwar_tu_chutiya_hain=ishwar_tu_chutiya_hain)


@app.route('/mainlogin', methods=['POST'])
def register():
    password = generate_password_hash(request.form['Password'])
    ishwar_tu_chutiya_hain = '8602842290'

    none = "none"

    try:
        
        if(request.form['Email'] != '' or request.form['Name'] != '' or request.form['Password'] != '' or request.form['CPassword'] != ''):
            
            if(request.form['Password'] == request.form['CPassword']):
                
                if(request.form['SID'] == ishwar_tu_chutiya_hain):
                    
                    record = {
                        "Email": request.form['Email'],
                        "Name":  request.form['Name'],
                        "Password":  password,
                        "SID": request.form['SID'],
                        "Period1": {
                            "College": request.form['College'],
                            "Dept": request.form['Department'],
                            "Year": request.form['Year'],
                            "Subject": request.form['Subject'],
                            "Div": request.form['Div'],

                        },
                        "Period2": {
                            "College": request.form['College1'],
                            "Dept": request.form['Department1'],
                            "Year": request.form['Year1'],
                            "Subject": request.form['Subject1'],
                            "Div": request.form['DivA'],

                        },
                        "Period3": {
                            "College": request.form['College2'],
                            "Dept": request.form['Department2'],
                            "Year": request.form['Year2'],
                            "Subject": request.form['Subject2'],
                            "Div": request.form['DivB'],

                        },
                        "Period4": {
                            "College": request.form['College3'],
                            "Dept": request.form['Department3'],
                            "Year": request.form['Year3'],
                            "Subject": request.form['Subject3'],
                            "Div": request.form['DivC'],

                        },
                        "Period5": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        },
                        "Period6": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        },
                        "Period7": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        },
                        "Period8": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        },
                        "Period9": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        },
                        "Period10": {
                            "College": none,
                            "Dept": none,
                            "Year": none,
                            "Subject": none,
                            "Div": none

                        }


                    }
                    
                    mycol.insert_one(record)
                    
                    return render_template('index.html')
    except:
        print("Something went wrong")


@app.route('/login')
def check1():
    return render_template('check.html')


@app.route('/check', methods=['POST'])
def check():
    password = generate_password_hash(request.form['Password'])
    newpassword = generate_password_hash(request.form['NPassword'])
    print(request.form['Email'])
    for x in mycol.find():

        if x['Email'] == request.form['Email'] and check_password_hash(x['Password'], request.form['Password']):
            record = x

            if(request.form['MName'] != '' or request.form['NPassword'] != '' or request.form['NEmail'] != ''):

                newrecord = {"$set": {"Email": request.form['NEmail'],
                                      "Name": request.form['MName'],
                                      "Password": newpassword,

                                      "Period1": {
                    "College": request.form['College'],
                    "Dept": request.form['Department'],
                    "Year": request.form['Year'],
                    "Subject": request.form['Subject'],
                    "Div": request.form['Div'],

                },
                    "Period2": {
                    "College": request.form['College1'],
                    "Dept": request.form['Department1'],
                    "Year": request.form['Year1'],
                    "Subject": request.form['Subject1'],
                    "Div": request.form['DivA'],

                },
                    "Period3": {
                    "College": request.form['College2'],
                    "Dept": request.form['Department2'],
                    "Year": request.form['Year2'],
                    "Subject": request.form['Subject2'],
                    "Div": request.form['DivB'],

                },
                    "Period4": {
                    "College": request.form['College3'],
                    "Dept": request.form['Department3'],
                    "Year": request.form['Year3'],
                    "Subject": request.form['Subject3'],
                    "Div": request.form['DivC'],

                }
                }
                }

                mycol.update_many({"_id": record['_id']}, newrecord)
                return render_template('mainlogin.html')
    Response.flash = 'Wrong Password'
    return render_template('check.html')


# Main Login
# @app.route('/mainlogin')
# def register_page_main():
#   return render_template('mainlogin.html')

# Kuch bhasad hi hain yaha yaad rakhna
@app.route('/maincheck', methods=['GET', 'POST'])
def checkmain():
    if request.method == 'POST':
        session.pop('user', None)
        password = generate_password_hash(request.form['Password'])
        for x in mycol.find():
            if x['Email'] == request.form['Email'] and check_password_hash(x['Password'], request.form['Password']):
                name = x['Name']
                email = x['Email']
                session['user'] = x['Name']
                # session['email']=x['Email']
                print(request.form['Password'])
                session['email'] = x['Email']
                session['period1'] = x['Period1']['College']+" "+x['Period1']['Dept']+" " + \
                    x['Period1']['Year']+" " + \
                    x['Period1']['Subject']+" "+x['Period1']['Div']
                session['period2'] = x['Period2']['College']+" "+x['Period2']['Dept']+" " + \
                    x['Period2']['Year']+" " + \
                    x['Period2']['Subject']+" "+x['Period2']['Div']
                session['period3'] = x['Period3']['College']+" "+x['Period3']['Dept']+" " + \
                    x['Period3']['Year']+" " + \
                    x['Period3']['Subject']+" "+x['Period3']['Div']
                session['period4'] = x['Period4']['College']+" "+x['Period4']['Dept']+" " + \
                    x['Period4']['Year']+" " + \
                    x['Period4']['Subject']+" "+x['Period4']['Div']
                g.user = session['user']
                return redirect(url_for('protected'))
                """return render_template('checkstatus.html',name=name,email=email)"""

    return render_template('index.html')


@app.route('/protected', methods=['GET', 'POST'])
def protected():
    print(g.user)
    if g.user:
        subjects = [session['period1'], session['period2'],
                    session['period3'], session['period4']]
        return render_template('checkstatus.html', user=session['user'], subjects=subjects)
    return redirect(url_for('/'))


@app.before_request
def before_request():
    if 'user' in session:
        g.user = session['user']


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('index.html')
#############

# Forget Password


@app.route('/forgetpassword', methods=['GET', 'POST'])
def forget():
    return render_template('forget.html')


@app.route('/OTPforpassword', methods=['GET', 'POST'])
def forgetpassword():
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random.random() * length)]
    myEnvVal.setVar()
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    msg = EmailMessage()
    msg['Subject'] = 'OTP For attendance tracker V1'
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = request.form['Email']
    msg.set_content('your OTP is ' + OTP + ', it will expire in 10 min')
    session['Email'] = request.form['Email']
    g.email = request.form['Email']

    session['OTP'] = OTP
    g.otp = session['OTP']
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print(OTP)
    print(g.otp)
    print(session['OTP'])
    return render_template('OTP.html', OTP=OTP, Email=g.email)


@app.route('/updatepassword', methods=['GET', 'POST'])
def updatepassword():
    

    print(session['OTP'])
    print(request.form['OTP'])
    if(session['OTP'] == request.form['OTP']):
        print("OTP match")
        for x in mycol.find():
            if x['Email'] == session['Email']:
                print("mail found")
                record = x
                if(request.form['Password'] != '' or request.form['CPassword'] != ''):
                    if(request.form['Password'] == request.form['CPassword']):
                        print("password check")
                        password = generate_password_hash(request.form['Password'])
                        newrecord = {"$set": {"Password": password,
                                            "CPassword": password
                                            }

                                    }
                        
                        mycol.update_many({"_id": record['_id']}, newrecord)
                        print("successfully")
                        return render_template('index.html')
    else:
        otp1="bhaibhai"
        return render_template('OTP.html',otp1=otp1)


@app.route('/upload', methods=['GET', 'POST'])
def dashboard():
    print(g.user)
    if g.user:
        subjects = [session['period1'], session['period2'],
                    session['period3'], session['period4']]
        return render_template('upload.html', subjects=subjects)


@app.route('/uploadfile', methods=['POST'])
def download():
    for x in mycol.find():
        email = x['Email']
    title = request.form['attendance']
    print("Bruh")
    df = pd.read_csv(request.files.get('myfile'),
                     encoding='utf-16', delimiter='\t')
    print(email)
    print(title)
    print(df)
    date = str(df['Timestamp'][0]).split()[0][:-1]
    df1 = df.sort_values(['Full Name', 'Timestamp'])
    XD = df1[(df1['Full Name'] == 'useradmin') | (
        df1['Full Name'] == 'Ravindra Apare')]
    mh, mm, ms = str(XD['Timestamp']).split()[2].split(':')
    basetime = int(datetime.timedelta(
        hours=int(mh), minutes=int(mm), seconds=int(ms)).total_seconds())
    endtime = basetime + 3900
    df1.reset_index(inplace=True)
    df1.drop('index', inplace=True, axis=1)
    i = 0
    a = 0
    b = 0
    j = 0
    jo = 0
    seconds1 = 0
    seconds2 = 0
    b1 = 0
    grandtotal = []
    while a < len(df1['Full Name'].unique()):
        if df1['Full Name'].value_counts().sort_index()[a] == 1:
            h, m, s = df1.iloc[i]['Timestamp'].split()[1].split(':')
            seconds = int(datetime.timedelta(
                hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
            seconds1 = endtime - seconds
            i = i + 1
        elif df1['Full Name'].value_counts().sort_index()[a] % 2 != 0:
            while b1 < math.trunc(df1['Full Name'].value_counts().sort_index()[a]/2):
                j = df1.iloc[i]['Timestamp'].split()[1]
                l = df1.iloc[i+1]['Timestamp'].split()[1]
                h, m, s = j.split(':')
                h1, m1, s1 = l.split(':')
                seconds = int(datetime.timedelta(hours=int(
                    h1)-int(h), minutes=int(m1)-int(m), seconds=int(s1)-int(s)).total_seconds())
                seconds1 = seconds1 + seconds
                b1 = b1 + 1
                i = i + 2
            b1 = 0
            jo = df1.iloc[i]['Timestamp'].split()[1]
            h, m, s = jo.split(':')
            seconds = int(datetime.timedelta(
                hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
            seconds2 = seconds1 + (endtime - seconds)
            seconds1 = seconds2
            i = i + 1
        elif df1['Full Name'].value_counts().sort_index()[a] % 2 == 0:
            while b < df1['Full Name'].value_counts().sort_index()[a]/2:
                j = df1.iloc[i]['Timestamp'].split()[1]
                l = df1.iloc[i+1]['Timestamp'].split()[1]
                h, m, s = j.split(':')
                h1, m1, s1 = l.split(':')
                seconds = int(float(datetime.timedelta(hours=int(
                    h1)-int(h), minutes=int(m1)-int(m), seconds=int(s1)-int(s)).total_seconds()))
                seconds1 = seconds1 + seconds
                b = b + 1
                i = i + 2
        b = 0
        grandtotal.append(seconds1)
        seconds = 0
        seconds1 = 0
        a = a+1
    new = pd.DataFrame()
    grandtotal1 = []
    Attendance = []
    for i in grandtotal:
        grandtotal1.append(str(datetime.timedelta(seconds=abs(i))))
        if(abs(i) >= 1800):
            Attendance.append('P')
        else:
            Attendance.append('A')
    new['Full Name'] = df1['Full Name'].unique()
    #new['Total Attendance Time'] = grandtotal1
    new[date] = Attendance
    newAttendance = dict(zip(list(new['Full Name']), list(new[date])))
    try:
        spreadSheet = gc.open(title)
        print(spreadSheet.id)
        attendanceSheet = spreadSheet.get_worksheet(1)
        data = attendanceSheet.get_all_values()
        i = 1
        Names = []
        while i < len(data):
            Names.append(data[i][1])
            i = i+1
        newnames = set(list(df['Full Name'].unique())).difference(Names)
        print(newnames)
        for i in list(newnames):
            attendanceSheet.append_row(
                [i], table_range="B"+str(len(attendanceSheet.get_all_records())+2))
            Names.append(i)
        newAttendance1 = [str(df['Timestamp'][0]).split()[0][:-1]]
        print("Sppoky1")
        for i in Names:
            try:
                newAttendance1.append(newAttendance[i])
            except:
                newAttendance1.append("A")
        newArray = np.array(newAttendance1, dtype="object").reshape(
            len(newAttendance1), 1)
        attendanceSheet.get_all_records()[0]
        attendanceSheet.append_rows(newArray.tolist(), table_range=xlsxwriter.utility.xl_col_to_name(
            len(attendanceSheet.get_all_records()[0]))+"1")
        if len(newnames) == 0:
            print("Yes they are 0")
            url1 = attendanceSheet.spreadsheet.url
            return render_template('download.html', name=url1)
        else:
            srno = []
            i = 0
            length = len(attendanceSheet.get_all_records())
            print(length)
            while i < length-1:
                i = i + 1
                srno.append(i)
            attendanceSheet.append_rows(np.array(srno[-(len(newnames)):]).reshape(
                (len(newnames), 1)).tolist(), table_range="A"+str(srno[-len(newnames)]+2)+":"+"A"+str(length+1))
            cell_list = attendanceSheet.findall("")
            for cell in cell_list:
                cell.value = "A"
            attendanceSheet.update_cells(cell_list)
            url = attendanceSheet.spreadsheet.url
            return render_template('download.html', name=url)
    except:
        newsheet = gs.oauth()
        s1 = newsheet.create(title)
        id = s1.id
        url = s1.url
        newsheet.insert_permission(
            s1.id, 'attendance@skn-hackclub-287609.iam.gserviceaccount.com', perm_type='user', role='writer')
        newsheet.insert_permission(
            s1.id, session['email'], perm_type='user', role='writer')
        print(new)
        print(date)  # Date required for final csv
        # mycol1.insert_many(data)
        print(id)
        d2g.upload(new, id, 'Attendance', credentials=credentials)
        return render_template('download.html', name=url)


@app.route('/download', methods=['GET', 'POST'])
def ok():

    #config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
    subject = request.form['attendance1']
    spreadSheet = gc.open(subject)
    attendanceSheet = spreadSheet.get_worksheet(1)
    data = attendanceSheet.get_all_values()
    rendered = render_template('html2pdf.html', email=data, subject=subject)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Contents-Disposition'] = 'attachment; filename=Attendance.pdf'
    return response


if __name__ == '__main__':
    app.run(debug=True)
