import os
import subprocess
import ctypes
import socket
import platform

# Admin check
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

### ===============================
### PARANOIA MODE FEATURES
### ===============================

def enable_camera_microphone_block():
    print("[+] Blocking camera and microphone")
    os.system('pnputil /disable-device "USB\\VID_*"') 
    # For microphone, you’d need specific device IDs or use Group Policy/scripts

def disable_camera_microphone_block():
    print("[-] Re-enabling camera and microphone")
    os.system('pnputil /enable-device "USB\\VID_*"')

def enable_bluetooth_block():
    print("[+] Disabling Bluetooth")
    os.system('sc stop bthserv')

def disable_bluetooth_block():
    print("[-] Enabling Bluetooth")
    os.system('sc start bthserv')

def enable_network_block():
    print("[+] Disabling Network Interfaces")
    os.system('netsh interface set interface "Wi-Fi" admin=disabled')
    os.system('netsh interface set interface "Ethernet" admin=disabled')

def disable_network_block():
    print("[-] Enabling Network Interfaces")
    os.system('netsh interface set interface "Wi-Fi" admin=enabled')
    os.system('netsh interface set interface "Ethernet" admin=enabled')

def enable_location_block():
    print("[+] Disabling Location Services")
    subprocess.call('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location" /v Value /t REG_SZ /d Deny /f', shell=True)

def disable_location_block():
    print("[-] Enabling Location Services")
    subprocess.call('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location" /v Value /t REG_SZ /d Allow /f', shell=True)

### ===============================
### STEALTH MODE
### ===============================

def enable_netbios_disable():
    print("[+] Disabling NetBIOS")
    os.system('wmic nicconfig where IPEnabled=true call SetTcpipNetbios 2')

def disable_netbios_disable():
    print("[-] Enabling NetBIOS")
    os.system('wmic nicconfig where IPEnabled=true call SetTcpipNetbios 1')

def enable_icmp_block():
    print("[+] Blocking ICMP (Ping Requests)")
    os.system('netsh advfirewall firewall add rule name="Block ICMP" protocol=icmpv4:8,any dir=in action=block')

def disable_icmp_block():
    print("[-] Allowing ICMP (Ping Requests)")
    os.system('netsh advfirewall firewall delete rule name="Block ICMP"')

### ===============================
### SPOOFING SYSTEM INFO
### ===============================

original_hostname = socket.gethostname()

def enable_system_spoofing():
    print("[+] Spoofing system identity")
    os.environ['COMPUTERNAME'] = "ANONYMIZED"
    os.environ['USERNAME'] = "ghost_user"
    os.environ['OS'] = "Windows 13 Pro"

def disable_system_spoofing():
    print("[-] Reverting system spoofing")
    os.environ['COMPUTERNAME'] = original_hostname
    # Resetting env vars doesn’t fully revert state; reboot may be needed

### ===============================
### DARK MODE / ACCESSIBILITY
### ===============================

def enable_dark_mode():
    print("[+] Enabling dark mode for apps")
    os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 0 /f')

def disable_dark_mode():
    print("[-] Disabling dark mode for apps")
    os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 1 /f')

### ===============================
### MAIN MENU STYLE TRIGGER
### ===============================

def main():
    if not is_admin():
        print("[-] Run this script as Administrator!")
        return

    print("""
=== Privacy / Stealth Mode Control Panel ===

1. Enable camera & mic block
2. Disable camera & mic block
3. Enable Bluetooth block
4. Disable Bluetooth block
5. Enable network block
6. Disable network block
7. Enable location block
8. Disable location block
9. Enable NetBIOS disable
10. Disable NetBIOS disable
11. Enable ICMP block
12. Disable ICMP block
13. Enable system spoofing
14. Disable system spoofing
15. Enable dark mode
16. Disable dark mode
0. Exit
""")
    while True:
        choice = input("Choose an option: ").strip()
        if choice == "1":
            enable_camera_microphone_block()
        elif choice == "2":
            disable_camera_microphone_block()
        elif choice == "3":
            enable_bluetooth_block()
        elif choice == "4":
            disable_bluetooth_block()
        elif choice == "5":
            enable_network_block()
        elif choice == "6":
            disable_network_block()
        elif choice == "7":
            enable_location_block()
        elif choice == "8":
            disable_location_block()
        elif choice == "9":
            enable_netbios_disable()
        elif choice == "10":
            disable_netbios_disable()
        elif choice == "11":
            enable_icmp_block()
        elif choice == "12":
            disable_icmp_block()
        elif choice == "13":
            enable_system_spoofing()
        elif choice == "14":
            disable_system_spoofing()
        elif choice == "15":
            enable_dark_mode()
        elif choice == "16":
            disable_dark_mode()
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
