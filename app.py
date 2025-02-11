from flask import Flask, request, redirect, jsonify
import sqlite3
import random
import string

app = Flask(__name__)
DB_FILE = "urls.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, short TEXT, long TEXT)")
    conn.commit()
    conn.close()

init_db()

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")
    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    short_key = generate_short_url()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (short_key, long_url))
    conn.commit()
    conn.close()

    return jsonify({"short_url": f"http://{VM1_IP}/{short_key}"})

@app.route("/<short_key>", methods=["GET"])
def redirect_url(short_key):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT long FROM urls WHERE short = ?", (short_key,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    return jsonify({"error": "Short URL not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
