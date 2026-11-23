# 📱 Carryo Zoom - Mobile Application Guide

This guide covers everything you need to run, install, and package **Carryo Zoom** as a native mobile application on **Android** and **iOS**.

---

## ⚡ Method 1: Instant PWA Mobile Installation (Recommended)
You do not need to install Android Studio or SDKs to run Carryo Zoom as a mobile application. It is fully built as a **Progressive Web Application (PWA)** with native touch gestures and full-screen standalone mode.

### For Android (Google Chrome / Brave / Edge / Samsung Internet):
1. Connect your phone to the same Wi-Fi network as this PC.
2. Open your mobile browser and go to:
   ```
   http://192.168.1.7:7000
   ```
3. A banner will appear at the top: **"Install Carryo Zoom App"**.
4. Tap **Install**, or tap the browser menu (**⋮**) and select **"Install App"** (or **"Add to Home Screen"**).
5. The **Carryo Zoom** app icon is added to your phone's app launcher.
6. When opened, it runs **completely full-screen** with no browser address bar, identical to native Zoom Mobile!

### For iPhone / iPad (Apple Safari):
1. Open **Safari** on your iPhone and visit:
   ```
   http://192.168.1.7:7000
   ```
2. Tap the **Share button** (square with arrow pointing up) at the bottom.
3. Scroll down and tap **"Add to Home Screen"**.
4. Tap **Add**. The Carryo Zoom app icon will appear on your home screen.
5. Tap the icon to launch in full-screen standalone native mode!

---

## 🚀 Mobile App Features Included

1. **Zoom Mobile Bottom Navigation Bar**:
   - 💬 **Team Chat**: Browse channels and 1-on-1 direct messages.
   - 🎥 **Meetings**: Quick "New Meeting", "Join by ID", and meeting schedule.
   - 🎨 **Whiteboard**: Touch-sensitive drawing with finger or stylus.
   - 📝 **Notes**: Meeting notes, action items checklist, and AI minutes generator.
   - ⚙️ **More**: Switch accounts, set custom status, and user profile.

2. **Mobile Two-Screen Chat Navigation**:
   - Tapping any channel or contact slides into the conversation view.
   - Top header features a prominent **`←` Back button** to return to the channels list.
   - Full touch target sizing (44px+) for comfortable one-handed mobile use.

3. **Mobile Video Calling & Camera Flip**:
   - Live WebRTC audio and video streaming.
   - **Flip Camera Button**: Seamlessly toggle between front-facing (selfie) camera and rear camera (`facingMode: "environment"`).
   - Touch-friendly mute, reactions, and slide-up in-meeting chat bottom sheet.

4. **Touch-Optimized Whiteboard**:
   - Full `touchstart`, `touchmove`, and `touchend` multi-touch support for drawing and sketching on mobile screens.

---

## 📦 Method 2: Export as Standalone Android APK (Using Capacitor)

If you need a `.apk` file to distribute or publish to the Google Play Store:

### 1. Requirements
- Node.js (v18+)
- Android Studio with Android SDK

### 2. Steps to Build APK:
Open PowerShell inside `E:\Project\carryo_chat`:
```powershell
# 1. Initialize Capacitor
npm install @capacitor/core @capacitor/cli @capacitor/android

# 2. Add Android platform
npx cap add android

# 3. Sync web assets and configuration
npx cap sync

# 4. Open project in Android Studio
npx cap open android
```

### 3. Generate Signed APK:
In Android Studio:
1. Go to **Build** > **Build Bundle(s) / APK(s)** > **Build APK(s)**.
2. Locate the generated `app-debug.apk` in `android/app/build/outputs/apk/debug/`.
3. Transfer the `.apk` to your phone and install!

---

## 🌐 Method 3: One-Minute APK via PWABuilder (Zero Code)
1. Deploy or tunnel your local port `7000` to a public URL (e.g. using `ngrok http 7000` or Cloudflare Tunnels).
2. Go to **[https://www.pwabuilder.com](https://www.pwabuilder.com)** in your desktop browser.
3. Enter your URL and click **Start**.
4. Click **"Package for Android"** > **Download Package**.
5. PWABuilder will automatically build a signed Google Play-ready Android `.apk` / `.aab` file!
