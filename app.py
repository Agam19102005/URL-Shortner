from flask import Flask, request, redirect, render_template
import sqlite3
import string

app = Flask(__name__)

# ==============================
# Base62 Encoding
# ==============================

BASE62 = string.ascii_letters + string.digits

def encode(num):
    base = len(BASE62)
    short = []
    while num > 0:
        short.append(BASE62[num % base])
        num //= base
    return ''.join(reversed(short)) or '0'


# ==============================
# Database
# ==============================

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT,
            short_code TEXT UNIQUE,
            clicks INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()


def get_db():
    return sqlite3.connect('database.db')


# ==============================
# Routes
# ==============================

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    error = None
    
    if request.method == 'POST':
        long_url = request.form['url']
        custom_code = request.form.get('custom_code')
        
        conn = get_db()
        c = conn.cursor()
        
        # 🔥 CUSTOM SHORT URL
        if custom_code:
            # Check if already exists
            c.execute("SELECT id FROM urls WHERE short_code=?", (custom_code,))
            exists = c.fetchone()
            
            if exists:
                error = "Custom URL already taken!"
            else:
                c.execute(
                    "INSERT INTO urls (long_url, short_code) VALUES (?, ?)", 
                    (long_url, custom_code)
                )
                conn.commit()
                short_url = request.host_url + "u/" + custom_code
        
        # 🔥 AUTO GENERATED
        else:
            c.execute("INSERT INTO urls (long_url) VALUES (?)", (long_url,))
            conn.commit()
            
            url_id = c.lastrowid
            short_code = encode(url_id)
            
            c.execute("UPDATE urls SET short_code=? WHERE id=?", (short_code, url_id))
            conn.commit()
            
            short_url = request.host_url + "u/" + short_code
        
        conn.close()
    
    return render_template('index.html', short_url=short_url, error=error)


# 🔗 REDIRECT ROUTE
@app.route('/u/<short_code>')
def redirect_url(short_code):
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT long_url, clicks FROM urls WHERE short_code=?", (short_code,))
    result = c.fetchone()
    
    if result:
        long_url, clicks = result
        
        # Update clicks
        c.execute(
            "UPDATE urls SET clicks=? WHERE short_code=?", 
            (clicks + 1, short_code)
        )
        conn.commit()
        conn.close()
        
        return redirect(long_url)
    
    return "URL not found"


# 📊 ANALYTICS ROUTE
@app.route('/stats/<short_code>')
def stats(short_code):
    conn = get_db()
    c = conn.cursor()
    
    c.execute(
        "SELECT long_url, short_code, clicks FROM urls WHERE short_code=?", 
        (short_code,)
    )
    result = c.fetchone()
    
    conn.close()
    
    if result:
        long_url, short_code, clicks = result
        return render_template(
            "stats.html", 
            long_url=long_url, 
            short_code=short_code, 
            clicks=clicks
        )
    
    return "No data found"


# ==============================
# Run App
# ==============================

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)