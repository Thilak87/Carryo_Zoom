import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'carryo-zoom-secret-key-2026-xyz')
    
    # Support both local SQLite and Cloud PostgreSQL
    db_url = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "carryo_chat.db")}')
    if db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = db_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB max file upload
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'pdf', 'txt', 'docx', 'xlsx', 'pptx', 'zip', 'mp3', 'wav', 'webm', 'ogg'}

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
