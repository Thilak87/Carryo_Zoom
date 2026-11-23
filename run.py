import os
import sys
import threading
import time
import webbrowser

# Ensure utf-8 encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from app import app, socketio

def open_browser(port):
    time.sleep(1.2)
    url = f"http://localhost:{port}"
    print(f"\n[Browser] Launching {url} in your default browser...")
    webbrowser.open(url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7000))
    
    print("=" * 60)
    print("  Starting Carryo Zoom Chat & Meet Application")
    print("=" * 60)
    print(f"  * Real-Time Chat: Channels, 1:1 DMs, Voice Memos, Files")
    print(f"  * Live Meetings:  WebRTC Video, Audio, Screen Share, Whiteboard")
    print(f"  * Meeting Notes:  Collaborative Scratchpad & AI Minutes")
    print(f"  * Local Access:   http://localhost:{port}")
    print(f"  * Other Network:  Run start_public_tunnel.bat for public HTTPS link")
    print("=" * 60)
    
    # Auto-launch browser in separate thread
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    
    # Run SocketIO Server
    try:
        socketio.run(app, host='0.0.0.0', port=port, debug=False, allow_unsafe_werkzeug=True)
    except KeyboardInterrupt:
        print("\n[Server] Shutdown signal received. Exiting gracefully.")
        sys.exit(0)
