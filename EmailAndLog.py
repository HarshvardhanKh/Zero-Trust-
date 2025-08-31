import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import requests
import geocoder

#------------------------------------------------------------------------------------

global logFile
logFile = "Logs/logs-"

#------------------------------------------------------------------------------------


def sendEmail(rEmail, email_content):
    sEmail = "cloudcodingbpsk@gmail.com"
    sPass = "phtv xpdw ocwg xcgv"
    msg = MIMEMultipart()
    msg['From'] = sEmail
    msg['To'] = rEmail
    msg['Subject'] = "Subject of the Email"
    msg.attach(MIMEText(email_content, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sEmail, sPass)
        
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as excep:
        print(f"Failed to send email: {excep}")
    finally:
        server.quit()

def getIP():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        ipData = response.json()
    except requests.exceptions.RequestException as excep:
        print(f"Error fetching IP address: {excep}")
        return "Not Found" , "xxx", "[xx, xx]"
    gData = geocoder.ip(ipData['ip'])
    return ipData['ip'], gData.city, gData.latlng

def Log(message):
    cData = datetime.now()
    cData = str(cData)
    cDate = cData[:10]
    cTime = cData[11:19]
    accessFile = logFile+cDate+".txt"
    if not os.path.exists(accessFile):
        f=open(accessFile,"w")
        f.close()
    ip,loc,lat = getIP()
    with open(accessFile,'a') as file:
        file.write(f"[{cData} IP: {ip} Loc: {loc} {lat}] : {message}\n")
