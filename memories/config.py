import pathlib

APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
#SECRET_KEY = b'\xa8\xcf\xb5\xe1\xe07YH\xe0xD\xda\x87c\xf1\xb4e\x97Rk\xe2mW\xe1'
#SESSION_COOKIE_NAME = 'login'


MEMORIES_ROOT = pathlib.Path(__file__).resolve().parent.parent

# File Upload to var/uploads/
"""
UPLOAD_FOLDER = MEMORIES_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
"""

DATABASE_FILENAME = MEMORIES_ROOT/'var'/'memories.sqlite3'
