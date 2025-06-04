from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '3890582d8508ea85e20ec48533a40759')

# MySQL database connection
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="your_password"
        )
        if connection.is_connected():
            return connection
        else:
            return None
    except Exception as e:
        print("❌ Database connection failed:", e)
        return None

# -------------------------
# 🟡 LOGIN ROUTE
# -------------------------
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        connection = connect_to_db()
        if connection is not None:
            cursor = connection.cursor(dictionary=True)  # ✅ dictionary=True allows accessing rows as dicts
            cursor.execute("USE login")
            cursor.execute("SELECT * FROM accounts WHERE username=%s AND password=%s", (username, password))
            account = cursor.fetchone()  # ✅ Use fetchone() instead of fetchall()
            if account:
                session['loggedin'] = True  # ✅ Fixed key: use 'loggedin' (not 'loggedIn')
                session['id'] = account['id']
                session['username'] = account['username']
                return render_template('index.html', msg="✅ Logged in successfully")
            else:
                msg = '❌ Incorrect username/password'
        else:
            msg = "❌ Database connection failed"
    return render_template('login.html', msg=msg)

# -------------------------
# 🟡 LOGOUT ROUTE
# -------------------------
@app.route('/logout')
def logout():
    session.pop('loggedin', None)  # ✅ Fixed key: must match the login session
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# -------------------------
# 🟡 REGISTER ROUTE
# -------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # ✅ Fixed bug: 'password ' had a space after it in your condition
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        connection = connect_to_db()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("USE login")
            cursor.execute("SELECT * FROM accounts WHERE username=%s", (username,))
            account = cursor.fetchone()
            if account:
                msg = "❌ Account already exists!"
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = '❌ Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = '❌ Username must contain only letters and numbers!'
            elif not username or not password or not email:
                msg = '❌ Please fill out the form!'
            else:
                # ✅ Fixed bug: SQL INSERT should use %s placeholders and pass variables as a tuple
                cursor.execute("INSERT INTO accounts(username, password, email) VALUES (%s, %s, %s)", (username, password, email))
                connection.commit()  # ✅ Required to save changes in DB
                msg = "✅ You have successfully registered!"
        else:
            msg = "❌ Database connection failed"
    return render_template("register.html", msg=msg)

# -------------------------
# 🟡 RUN APP
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
