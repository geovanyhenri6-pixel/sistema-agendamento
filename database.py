import sqlite3
from flask import g
from config import Config

def get_db():

    if not hasattr(g, "db"):
        g.db = sqlite3.connect(Config.DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")

    return g.db