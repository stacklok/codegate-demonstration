from flask import Flask, request, jsonify  # type: ignore
import hashlib
import sqlite3
import invokehttp  # type: ignore

app = Flask(__name__)

# Database setup (for demonstration purposes)
def init_db():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)') #nocg
    conn.commit()
    conn.close()

@app.route('/api/data', methods=['GET'])
def get_data():
    # Insecure: No input validation
    return {"data": "This is some insecure data!"}


@app.route('/api/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'] #nocg
    hashed_password = hashlib.md5(password.encode()).hexdigest()  #nocg
    print(f"User {username} logged in with password hash: {hashed_password}") #nocg
    return jsonify({"message": "Logged in!"})


# code can be applied

def get_user_by_username(username):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user
