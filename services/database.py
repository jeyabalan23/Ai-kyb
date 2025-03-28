import sqlite3

class Database:
    def __init__(self, db_path="data/agents.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_agents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                version TEXT,
                features TEXT,
                use_case TEXT
            )
        """)
        self.conn.commit()

    def check_agent_exists(self, name, version):
        self.cursor.execute("SELECT * FROM ai_agents WHERE name = ? AND version = ?", (name, version))
        return self.cursor.fetchone()

    def save_new_agent(self, name, version, features, use_case):
        self.cursor.execute("INSERT INTO ai_agents (name, version, features, use_case) VALUES (?, ?, ?, ?)",
                            (name, version, features, use_case))
        self.conn.commit()

    def update_agent(self, name, version, features, use_case):
        self.cursor.execute("UPDATE ai_agents SET features = ?, use_case = ? WHERE name = ? AND version = ?",
                            (features, use_case, name, version))
        self.conn.commit()
