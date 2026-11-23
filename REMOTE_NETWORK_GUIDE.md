# 🌐 How to Use Carryo Zoom Across Different Networks (Internet Access)

By default, `http://192.168.1.7:7000` is a **Local Area Network (LAN) IP**. It only works when devices are connected to the **same Wi-Fi router**.

To let friends, team members, or clients join from **different networks** (e.g. mobile 4G/5G, different homes, offices, or other cities), you need a public address with **HTTPS** (required by mobile phones for camera & mic permissions).

---

## ⚡ Method 1: Instant One-Click Public Tunnel (Cloudflare - Recommended)
We have pre-configured and downloaded `cloudflared.exe` directly inside your project folder!

### How to Start:
1. Make sure your server is running (double-click `run.bat`).
2. Double-click **`start_public_tunnel.bat`**.
3. A command window will open and display your public link:
   ```
   https://random-words.trycloudflare.com
   ```
4. **Share this HTTPS link with anyone!**
   - Works on **mobile data (4G/5G)**, external Wi-Fi, and anywhere worldwide.
   - Automatically provides a verified **SSL/HTTPS certificate**, so cameras, microphones, screen sharing, and the PWA "Install App" button work seamlessly on Android and iOS.
   - 100% Free, no account or sign-up needed.

---

## 🚀 Method 2: Ngrok (Popular Alternative)
If you prefer [ngrok](https://ngrok.com/):
1. Sign up for a free account at `https://ngrok.com`.
2. Download `ngrok.exe` and authenticate:
   ```powershell
   ngrok config add-authtoken YOUR_TOKEN
   ```
3. Forward port 7000:
   ```powershell
   ngrok http 7000
   ```
4. Copy the `https://...ngrok-free.app` URL and share it.

---

## ☁️ Method 3: 24/7 Cloud Hosting (No PC Required)
If you don't want to keep your computer turned on:
1. **Render.com / Railway.app**:
   - Push your `carryo_chat` folder to a GitHub repository.
   - Connect the repo to Render or Railway.
   - Set build command: `pip install -r requirements.txt`.
   - Set start command: `python app.py`.
   - You get a free permanent URL like `https://carryo-zoom.onrender.com` that stays online 24/7.

---

## 🔒 Method 4: Private Team Network (Tailscale VPN)
If you want private access without exposing your server to the public internet:
1. Install **Tailscale** on your PC and your phone (or team member devices).
2. Sign in with the same account.
3. Tailscale assigns your PC a private 100.x.x.x IP (e.g. `http://100.85.12.34:7000`).
4. Any connected device can access the chat and meetings securely from any network.

---

## 💡 Important Note: Why HTTPS is Required for Video Calls
Mobile browsers (Android Chrome, iOS Safari) strictly block camera and microphone access (`navigator.mediaDevices.getUserMedia`) over insecure `http://` when outside `localhost`.

Using **`start_public_tunnel.bat`** automatically gives you a secure **`https://`** URL, ensuring cameras, microphones, and screen sharing work out of the box!
