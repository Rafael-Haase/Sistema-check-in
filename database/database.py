from pathlib import Path
import sqlite3 as sq

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "checkin.db"
connection = sq.connect(DB_PATH)
cursor = connection.cursor()