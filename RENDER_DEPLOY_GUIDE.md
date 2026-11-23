# ☁️ How to Deploy Carryo Zoom to Render (100% Free 24/7 Cloud Hosting)

This guide walks you through deploying **Carryo Zoom** to **Render.com** for free, so anyone in the world can use the chat, mobile app, and video calls without keeping your computer turned on.

---

## 📋 Summary of Cloud Settings
- **Hosting Provider:** [Render.com](https://render.com)
- **Cost:** **$0 / month (Free Tier)**
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`

---

## 🚀 Step-by-Step Deployment (Takes ~5 Minutes)

### Step 1: Upload Your Code to GitHub
1. Open [github.com](https://github.com) and create a **New Repository** (e.g. named `carryo-chat`). Keep it *Public* or *Private*.
2. In PowerShell, push your folder to GitHub:
   ```powershell
   cd E:\Project\carryo_chat
   git init
   git add .
   git commit -m "Deploy Carryo Zoom Chat"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/carryo-chat.git
   git push -u origin main
   ```

---

### Step 2: Create a Free Web Service on Render
1. Go to **[https://dashboard.render.com](https://dashboard.render.com)** and sign in with your GitHub account (free, no credit card required).
2. Click **New +** at the top right and select **Web Service**.
3. Select **Build and deploy from a Git repository**, then choose your `carryo-chat` repository.

---

### Step 3: Configure Settings on Render
Fill in these exact fields:
- **Name:** `carryo-zoom` *(or any name you like)*
- **Region:** Choose the closest region (e.g., *Singapore*, *Frankfurt*, or *Oregon*)
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Instance Type:** Select **Free** ($0 / month)

Click **Deploy Web Service**!

---

### Step 4: Your App is Live!
- Render will install dependencies and start your app in ~2 minutes.
- When done, you will receive your permanent public URL at the top of the dashboard:
  ```
  https://carryo-zoom.onrender.com
  ```
- Open that link on **any phone, tablet, or laptop on 4G, 5G, or Wi-Fi** anywhere in the world!
- Install it as a mobile app directly using the **"Install App"** button!
