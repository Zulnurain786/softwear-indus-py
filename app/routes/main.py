from datetime import datetime

from flask import render_template, jsonify
from app import app
from app.utils.db import get_mysql_time


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home Page', year=datetime.now().year)

@app.route('/version')
def version():
    return jsonify({"version": "2.00"})

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', year=datetime.now().year, message='Your contact page.')

@app.route('/about')
def about():
    return render_template('about.html', title='About', year=datetime.now().year, message='Your application description page.')

@app.route('/mysql-time')
def mysql_time():
    """Returns the current MySQL server timestamp."""
    try:
        ts = get_mysql_time()
        return jsonify({"mysql_current_timestamp": str(ts), "status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500