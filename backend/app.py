from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/health")
def health():
    return {"status": "OK"}, 200

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json.get("content")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (data,))
    conn.commit()
    conn.close()
    return {"message": "Data inserted"}, 201


@app.route("/fetch")
def fetch():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)