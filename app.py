import os
import sys

# Ensure utf-8 encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from flask import Flask, render_template, send_from_directory, redirect, url_for
from flask_socketio import SocketIO
from config import Config
from models import db, seed_initial_data
from routes import auth_bp, chat_bp, meeting_bp
from sockets import register_all_sockets

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(meeting_bp)

    # Initialize SocketIO
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",
        manage_session=False,
        ping_timeout=20,
        ping_interval=10
    )

    # Register real-time Socket.IO event handlers
    register_all_sockets(socketio)

    # Database initialization & seeding
    with app.app_context():
        db.create_all()
        seed_initial_data()

    # Frontend routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/meeting/<meeting_code>')
    def meeting_redirect(meeting_code):
        return redirect(f"/{'#meeting/' + meeting_code}")

    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    return app, socketio

app, socketio = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7000))
    print(f"\n=======================================================")
    print(f"  Carryo Zoom Chat & Meet Server is running!")
    print(f"  Open your browser at: http://localhost:{port}")
    print(f"=======================================================\n")
    socketio.run(app, host='0.0.0.0', port=port, debug=True, allow_unsafe_werkzeug=True)
