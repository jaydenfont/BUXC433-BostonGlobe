from __future__ import print_function
import re
from google.cloud import vision
import io
import os
from dotenv import load_dotenv
import csv
import mysql.connector
from mysql.connector import Error

load_dotenv()


def getText(uri):
    image_uri = uri
    client = vision.ImageAnnotatorClient()
    with io.open(image_uri, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    return response.text_annotations[0].description


def getData(text):
    field_dict = {'institution': ["Institution", "Date"], 'complaint': ["Informal filed", "Remedy"], 'remedy': ["Requested", "Recipient"], 'finaldecision': ["Final", ""], 'housing': ["Housing", "Informal"], "cosignature": [
        "INMATE RECEIPT", ""], "recieveddate": ["INMATE RECEIPT", ""], "decisiondate": ["RECEIPT", "appealed"], 'grievancedate': ["Housing", "Informal"], 'incidentdate': ["Housing", "Informal"], "corecipient": ["Requested", "Recipient"]}
    return_dict = {}
    for i in field_dict:
        data = ""
        string1 = field_dict[i][0]
        string2 = field_dict[i][1]
        if string1 in text and string2 in text:
            if string2 != "":
                data = text[text.index(string1)+len(string1)
                                       :text.index(string2)].strip()
            else:
                data = text[text.index(string1)+len(string1):].strip()

            if i == "complaint":
                if "No" in data:
                    data = data[data.index("No")+len("No"):].strip()
                if data == "":
                    data = None
            if i == "remedy":
                if "Staff" in data:
                    data = data[:data.index("Staff")].strip()
                if data == "":
                    data = None
            if i == "finaldecision":
                if "Signature" in data:
                    data = data[:data.index("Signature")].strip()
                if data == "":
                    data = None
            if i == "housing":
                if data[0].isnumeric():
                    data = None
                else:
                    data = data[:7].strip()
                if data == "":
                    data = None
            if i == "cosignature":
                if "Signature" in data:
                    data = data[data.index(
                        "Signature")+len("Signature"):].strip()
                if data == "":
                    data = None
            if i == "recieveddate":
                if "Received" in data and "Signature" in data:
                    data = data[data.index(
                        "Received")+len("Received"):data.index("Signature")].strip()
                if data == "" or len(data) > 8:
                    data = None
            if i == "decisiondate":
                if "Decision Date" in data and "Signature" in data:
                    data = data[data.index(
                        "Decision Date")+len("Decision Date"):data.index("Signature")].strip()
                if data == "" or len(data) > 8:
                    data = None
            if i == "grievancedate":
                if "Incident" in data:
                    data = data[:data.index("Incident")]
                    data = data[-9:].strip()
                else:
                    data = data[-9:].strip()
                if data == "" or len(data) > 8:
                    data = None
            if i == "incidentdate":
                if "Incident" in data:
                    data = data[:data.index("Incident")]
                    data = data[-18:-9].strip()
                else:
                    data = data[-18:-9].strip()
                if data == "" or len(data) > 8:
                    data == None
            if i == "corecipient":
                if "Staff" in data:
                    data = data[data.index("Staff") + len("Staff"):].strip()
            if data == "":
                data == None
        else:
            data = None
        if data != None:
            return_dict[i] = data.strip('\n').replace('\n', '')
    return return_dict

def clearDB():
    try:
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=PWD,
        database="grievancesDB")

        if conn.is_connected():
            print("Connected to db")
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS grievances_auto;')
            print('Creating table....')
            cursor.execute("CREATE TABLE grievances_auto (institution CHAR(255), housing CHAR(255), incidentdate CHAR(255), grievancedate CHAR(255), complaint LONGTEXT, remedy LONGTEXT, corecipient LONGTEXT, cosignature CHAR(255), recieveddate CHAR(255), decisiondate CHAR(255), finaldecision LONGTEXT)")
            print("grievances_auto table is created....")
    except Error as e:
        print("Error while connecting to MySQL", e)


def addGrievance(data):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=PWD,
            database="grievancesDB")
        if conn.is_connected():
            print("Connected to db")
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('grievances_auto', columns, placeholders)
            cursor.execute(sql, list(data.values()))
            conn.commit()
            print("All records inserted")
    except Error as e:
        print("Error while connecting to MySQL", e)


def ocr():
    directory = '/Users/momol/BU/BUXC433-BostonGlobe/code/ocr_scan/grievances'
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            grievancetext = getText(os.path.join(directory, filename))
            grievancedata = getData(grievancetext)
            addGrievance(grievancedata)
            count += 1
            print(count)


def showResults):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MYSQLPWD',
            database="grievancesDB")
        if conn.is_connected():
            print("Connected to db")
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            sql = "SELECT * FROM grievances_auto"
            cursor.execute(sql)
            result = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            fp = open('test.csv', 'w')
            myFile = csv.writer(fp)
            myFile.writerow(column_names)
            myFile.writerows(result)
            fp.close()
    except Error as e:
        print("Error while connecting to MySQL", e)