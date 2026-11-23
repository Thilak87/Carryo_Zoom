# Carryo Zoom Chat & Meet

A complete, feature-rich Zoom-like collaboration and communication platform built with **Python (Flask-SocketIO)**, **WebRTC**, and modern web technologies.

![Carryo Zoom Chat](static/uploads/preview.png)

---

## 🌟 Key Features

### 1. 💬 Zoom Team Chat & Direct Messaging
- **Public & Private Channels**: `#general`, `#dev-squad`, `#design-sync`, `#watercooler`, with ability to create new custom channels.
- **1-on-1 Direct Messaging (DMs)**: Private real-time messaging between teammates.
- **Rich Text Formatting**: Markdown support, syntax-highlighted code blocks, bold, italics, bullet lists.
- **Emoji Reactions**: React with 👍, ❤️, 😂, 🚀, 🎉 directly on messages with real-time counters.
- **Threaded Quote Replies**: Reply directly to any message with an instant visual quote banner.
- **Pinned Messages**: Pin important announcements or links for quick reference in any channel.
- **Voice Memos**: Record voice messages from your microphone using the browser MediaRecorder API and send them as interactive audio bubbles.
- **File & Image Attachments**: Drag-and-drop or upload images with lightbox preview, documents, PDFs, and files with size indicators and download buttons.
- **Typing Indicators**: Real-time "*[User] is typing...*" indicators.
- **User Presence**: Live status badges (*Available*, *In a Meeting*, *Away*, *Offline*) and custom status messages.
- **Sound Notifications**: Web Audio API synthesized soft chimes on new messages (zero audio file dependencies).

---

### 2. 🎥 Live Video & Audio Meetings (Zoom Meetings Clone)
- **Instant Meeting**: One-click "New Meeting" or "Meet Now" directly from channels and DMs.
- **Zoom-Style Meeting IDs**: Formatted 9-digit meeting codes (e.g., `482-910-384`).
- **WebRTC Peer-to-Peer Video & Audio**: Real-time camera streams with automatic fallback avatars.
- **Native Screen Sharing**: Share full desktop, application windows, or browser tabs with meeting members.
- **Active Speaker Border**: Visual audio indicator highlighting speaking participants.
- **In-Meeting Chat**: Real-time side drawer chat for meeting participants.
- **Virtual Hand Raise (✋)**: Raise hand with audible chime and visual notification for host.
- **Zoom Floating Reactions**: Floating reaction emojis (👏, 👍, ❤️, 🎉, 😂) floating up on the screen for all participants.
- **Host Controls**: View all participants and host-mute controls.
- **QR Code & Invite Links**: Built-in QR code generator using the `qrcode` library for mobile/guest access.

---

### 3. 🎨 Collaborative Whiteboard (Zoom Whiteboard)
- **Shared Digital Canvas**: Pen, highlighter, straight line, rectangle, circle, and eraser tools.
- **Color Palette & Brush Thickness**: Real-time synchronized drawing strokes across all participants via WebSockets.
- **Export to PNG**: One-click download of the whiteboard drawing.

---

### 4. 📝 Meeting Notes & AI-Ready Minutes Generator
- **Collaborative Notes Editor**: Shared scratchpad for recording meeting agenda and discussion minutes.
- **Interactive Action Items Checklist**: Add items, toggle completion `[x]`, and track progress.
- **✨ AI Summary Generator**: Automatically synthesizes meeting notes and chat into structured executive minutes with key decisions and assigned action items.
- **Export to Markdown**: Download meeting minutes as clean `.md` documents.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure Python 3.10+ is installed on your system.

### 2. Run the Application
Open PowerShell or Command Prompt, navigate to the folder, and run:
```powershell
python run.py
```
*(Or double-click `run.bat` on Windows)*

The application server will start at **http://localhost:7000** and will automatically open in your default web browser.

---

## 👥 How to Test Multi-User Real-Time Features

1. Open **http://localhost:7000** in your primary browser tab (logged in as *Alex Rivera*).
2. Open **http://localhost:7000** in an **Incognito / Private tab** or another browser (e.g. Edge / Chrome / Firefox).
3. In the second tab, click the profile pill at the top right and switch to another user (e.g., *Sarah Connor* or *David Chen*).
4. Send messages, voice memos, files, or click **"New Meeting"** to experience real-time two-way video, audio, screen share, and whiteboard collaboration!

---

## 📁 Project Architecture

```
carryo_chat/
├── app.py                      # Flask & SocketIO application entry point
├── config.py                   # App configuration & upload limits
├── models/
│   ├── database.py             # SQLAlchemy models (User, Channel, Message, Reaction, Meeting, etc.)
│   └── __init__.py
├── routes/
│   ├── auth_routes.py          # User session, presence & switcher APIs
│   ├── chat_routes.py          # Channels, DMs, uploads & search APIs
│   ├── meeting_routes.py       # Meetings, QR codes & notes APIs
│   └── __init__.py
├── sockets/
│   ├── chat_sockets.py         # Real-time messages, typing & reactions
│   ├── meeting_sockets.py      # WebRTC signaling, hand raise & reactions
│   ├── whiteboard_sockets.py   # Whiteboard drawing synchronization
│   └── __init__.py
├── static/
│   ├── css/
│   │   ├── style.css           # Zoom dark theme & chat styles
│   │   └── meeting.css         # Video grid, dock controls & whiteboard styles
│   ├── js/
│   │   ├── app.js              # State management & modal orchestration
│   │   ├── chat.js             # Chat feed, voice notes, attachments & reactions
│   │   ├── meeting.js          # WebRTC video/audio, screen share & in-meeting chat
│   │   ├── whiteboard.js       # Collaborative HTML5 canvas whiteboard
│   │   └── notes.js            # Meeting notes & AI summary generator
│   └── uploads/                # User uploaded files, images & voice memos
├── templates/
│   └── index.html              # Main Zoom interface single-page app
├── run.py                      # Launcher with automatic browser startup
├── run.bat                     # Double-click Windows batch runner
└── requirements.txt            # Python dependencies
```
