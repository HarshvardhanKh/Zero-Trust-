Zero Trust – Cyber Vigilance Prototype
Overview

Zero Trust is a prototype cyber protection system that integrates Face Recognition, Bluetooth Proximity Unlock, and Email Verification for strong user authentication.

This prototype demonstrates the concept of combining biometric security, trusted device verification, and real-time logging/alerts to secure a laptop.

The Paranoia Mode is also included (for system lockdown & stealth operations), but in this prototype it only runs via a separate temporary terminal window. A GUI version is planned for the future.

Features

Face Recognition Login (via webcam & stored reference photo)

Bluetooth Device Proximity Unlock (system unlock only if trusted device is nearby)

Email Verification with OTP

Logging of all login attempts with timestamp, IP & geolocation

Paranoia Mode (Prototype): Blocks network, Bluetooth, mic/camera, and spoofs system details

Project Structure
├── Main.py              # Entry point (control panel & setup)
├── faceRecog.py         # Facial recognition logic
├── userInput.py         # Captures user face image
├── Bluetooth.py         # Bluetooth scanning & proximity detection
├── EmailAndLog.py       # Email OTP + logging
├── Paranoia.py          # Paranoia mode (system lockdown features)
├── userData/            # Stores face & email data
├── Logs/                # Login attempt logs
└── Zero_Trust.pptx      # Presentation explaining concept

Requirements
Install Dependencies

Run this in your terminal:

pip install opencv-python
pip install face-recognition
pip install PySide6
pip install requests
pip install geocoder

Additional Notes

Windows Only: Some functions (lock workstation, paranoia features) use ctypes and netsh, which are Windows-specific.

Face Recognition requires dlib (installed automatically with face-recognition, but make sure you have CMake installed on your system).

Make sure your webcam and Bluetooth are enabled.

How to Run

Clone or download this repository.

Ensure you have Python 3.9+ installed.

Run the main script:

python Main.py


On the first run, you’ll go through Setup:

Register Email (with OTP verification)

Register Face ID (webcam capture)

Register Bluetooth Device (trusted device scan)

After setup, the Control Panel opens where you can:

Reset Face ID

Reset Bluetooth device

Test Face Recognition

Enter Paranoia Mode (prototype)

Paranoia Mode

Currently, Paranoia Mode is not connected to the main terminal control panel. It can be run separately:

python Paranoia.py


Features include:

Blocking camera & microphone

Disabling Bluetooth & network interfaces

Disabling location services

Blocking ICMP (ping) requests

System identity spoofing

(In future versions, this will be integrated with GUI controls.)

Future Enhancements

GUI-based dashboard for setup & control

AES-256 encryption of sensitive data

Automatic decoy environment deployment

Boot-time integrity checks

Geo-fencing for login attempts
