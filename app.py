import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            port=os.environ.get("DB_PORT", "5432"),
            dbname="campus",
            user="campus",
            password="dev-password",
            connect_timeout=3,
        )
        conn.close()
        return jsonify(status="ok", db="reachable")
    except Exception as e:
        return jsonify(status="error", db=str(e)), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
