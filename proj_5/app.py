from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import string
import random

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original TEXT,
                    short TEXT
                )""")
    conn.commit()
    conn.close()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO urls (original, short) VALUES (?, ?)", (original_url, short_code))
        conn.commit()
        conn.close()

        return render_template("index.html", short_url=request.host_url + short_code)
    
    return render_template("index.html")

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT original FROM urls WHERE short=?", (short_code,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
