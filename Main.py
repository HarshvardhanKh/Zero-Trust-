from datetime import datetime
import random
import os

#---------CUSTOM---------
import userInput
import EmailAndLog
import Bluetooth
import faceRecog
#------------------------

header=r"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐ _____                _____               _   ▌
▐|__  /___ _ __ ___   |_   _| __ _   _ ___| |_ ▌
▐  / // _ \ '__/ _ \    | || '__| | | / __| __|▌
▐ / /|  __/ | | (_) |   | || |  | |_| \__ \ |_ ▌
▐/____\___|_|  \___/    |_||_|   \__,_|___/\__|▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
"""
def emailVerify():
    print(header)
    print("Email Verification".center(48,'='))
    print("An OTP will be sent to your registered E-mail for verification")
    input("(Press Enter to continue <make sure internet is connected>)\n")
    with open("userData/emailData.txt") as f:
        email=f.read()
    print()
    otp=str(random.randint(1000,9999))
    EmailAndLog.sendEmail(email,f"You OTP for access for Email: {email} to Zero Trust is {otp}")
    print("An OTP Has been sent to your Email Address!!")
    n=input("Enter the OTP: ")

    #Creates a log
    EmailAndLog.Log("Your E-mail was verified")

    os.system('cls')
    if n==otp:
        return True
    return False
    


def emailSetup():
    print(header)
    print("Setup Email".center(48,'='))
    email=input("(Make sure Internet is connected)\nEnter a user Email: ")
    print()
    while True:
        otp=str(random.randint(1000,9999))
        EmailAndLog.sendEmail(email,f"You OTP for access for Email: {email} to Zero Trust is {otp}")
        print("An OTP Has been sent to your Email Address!!")
        print("(If you want to re-enter the E-mail address type -1)")
        n=input("Enter the OTP: ")
        if n=='-1':
            email=input("\nEnter the email address again:")
            print("\nNew email saved!!")
            print("Generating New OTP.......\n")
            continue
        if n==otp:
            break
        print("\nInvalid OTP!!!!")
        print("Generating New OTP.......\n")
    with open("userData/emailData.txt",'w') as f:
        f.write(email)

    #Creates a log
    EmailAndLog.Log("You E-mail was changed")

    os.system('cls')

def faceSetup():
    print(header)
    print("Face ID Setup".center(48,'='))
    print("\nNow We are gonna take a photo for the Face ID Make sure you are in camera frame:-")
    print("(Press Enter to Take the Photo)")
    input()
    while True:
        userInput.takePhoto()
        print("Photo taken sucessfully!!!\nARE YOU SURE YOU WERE IN FRAME??")
        print("If no them you can retake by typing '-1'\nOr continue with 0")
        n=input("->")
        if n=='0':
            break
        print()

    #Creates a log
    EmailAndLog.Log("Your Face Recognition was reset")

    os.system('cls')

def btSetup():    
    print(header)
    print("Setup Bluetooth Device Proximity".center(48,'='))
    print("\nNow We are gonna setup the bluetooth device for the Proximity Unlock:-")
    input("(Make sure your bluetooth is enabled and then press enter to scan for devices)\n")
    while True:
        os.system('cls')
        print(header)
        print("Setup Bluetooth Device Proximity".center(48,'='))
        print()
        Bluetooth.setupScan()
        print("\nSelect the desired bluetooth device for proximity unlock:-")
        print("(if the device isn't visible in the list, kindly check that the bluetooth of the device is enabled then type '-1' to refresh )")
        n=input('->')
        if n=='-1' or (not n.isdigit()) or int(n)>=len(Bluetooth.found_devices):
            continue
        n=int(n)
        print(f"\nName: {Bluetooth.found_devices[n-1][0]}\nMAC Address: {Bluetooth.found_devices[n-1][1]}")
        print("Are you sure you want to set this device for proximity?(y/n)")
        c=input("->")
        if c=="y":
            break
        else:
            continue
    with open("userData/btData.txt",'w') as f:
        f.write(Bluetooth.found_devices[n-1][1])

    #Creates a log
    EmailAndLog.Log("Your Bluetooth device was changed")

    os.system('cls')

def setup():
    emailSetup()
    faceSetup()
    btSetup()
    print(header)
    print("".center(48,"=")+"\n"+"SETUP COMPLETED".center(48)+"\n"+"".center(48,'='))
    EmailAndLog.Log("Your Setup was completed sucessfully")
    input("(Press Enter to continue to main menu)")
    os.system('cls')
            

def menu():
    print(header)
    print("CONTROL PANEL".center(48,'='))
    print("\n1) Reset your Face Recognition")
    print("2) Reset you Bluetooth proximity Setting")
    print("3) Test Facial recognition")
    print("4) Paranoia Mode (Work In Progress)")
    print("5) Exit the program")
    n=int(input("\n(Select an option)\n->"))
    os.system('cls')
    match n:
        case 1: #Email Verification + Reset face if verified
            EmailAndLog.Log("Face ID change attempted")
            if emailVerify():
                faceSetup()
                menu()
            else:
                print(header)
                print("Email Verification Failed".center(48,'='))
                EmailAndLog.Log("Email Verification Failed!!!")
                input("(Press Enter to go back to the Main Menu)\n")
                os.system('cls')
                menu()
        case 2: #Email Verification + Reset BT if verified
            EmailAndLog.Log("BT Device Change attempted")
            if emailVerify():
                btSetup()
                menu()
            else:
                print(header)
                print("Email Verification Failed".center(48,'='))
                EmailAndLog.Log("Email Verification Failed!!!")
                input("(Press Enter to go back to the Main Menu)\n")
                os.system('cls')
                menu()
        case 3: #Check face recognition
            EmailAndLog.Log("Face ID checkked")
            if faceRecog.checkFace():
                print(header)
                print("FACE RECOGNITION RESULT".center(48,'='))
                print("\nFace Matched!!!")
                EmailAndLog.Log("Face Recognition matched!!")
                input("(Press Enter to return to main menu)\n")
                os.system('cls')
                menu()
            else:
                print(header)
                print("FACE RECOGNITION RESULT".center(48,'='))
                print("\nFace NOT Matched!!!")
                EmailAndLog.Log("Face Recognition Failed!!")
                input("(Press Enter to return to main menu)\n")
                os.system('cls')
                menu()
        case 4: #Paranioa Menu
            return
        case 5:
            EmailAndLog.Log("Main Menu closed")
            quit

if __name__ == "__main__":
    if not os.path.exists("userData/faceData.jpg"):
        setup()
    EmailAndLog.Log("Main Menu was accessed")
    menu()
