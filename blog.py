# blog.py - controller

# imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g

import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the DATABASE
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run(debug=True)