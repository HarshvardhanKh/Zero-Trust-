import sys
import ctypes
from PySide6.QtCore import QCoreApplication
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent
target_mac = "74:F6:7A:3E:8C:92"
global found_devices,counter,app
found_devices = []
counter=1
app = QCoreApplication(sys.argv)

def device_discovered(device):
    name = device.name() or "Unknown"
    mac = device.address().toString().upper()
    print(f"Name: {name}, MAC: {mac}")
    found_devices.append(mac)

def device_discovered1(device):
    global counter
    name = device.name() or "Unknown"
    mac = device.address().toString().upper()
    print(f"{counter}. Name: {name}, MAC: {mac}")
    counter+=1
    found_devices.append([name,mac])

def devi(device):
    name1 = device.name() or "Not Resolved"
    mac1 = device.address().toString().upper()
    print(f"Name: {name1}, MAC: {mac1}")
    found_devices.append(mac1)

def discovery_finished():
    print("Scanning finished.")
    print(target_mac)
    if target_mac not in found_devices:
        print("Owner's device not found, initiating lockdown")
        ctypes.windll.user32.LockWorkStation()
    else:
        print("Owner's device found")
    QCoreApplication.quit()

def discovery_finished1():
    print("Scanning finished.")
    QCoreApplication.quit()
    

def setupScan():
    global counter,found_devices
    counter=1
    found_devices=[]
    
    agent = QBluetoothDeviceDiscoveryAgent()

    agent.deviceDiscovered.connect(device_discovered1)
    agent.finished.connect(discovery_finished1)

    print("Scanning for Bluetooth devices...")
    agent.start()

    app.exec()
    app.quit()
    

def scan():
    found_devices=[]

    agent = QBluetoothDeviceDiscoveryAgent()

    agent.deviceDiscovered.connect(device_discovered)
    agent.finished.connect(discovery_finished)

    print("Scanning for Bluetooth devices...")
    agent.start()

    sys.exit(app.exec())

if __name__ == "__main__":
    #scan1() #PRINTS THE LIST
    #scan()        #ACTUAL FUNCTION
    quit
