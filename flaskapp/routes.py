# imports
from flask import Flask, render_template, request, redirect, url_for
from flaskapp import app
# if forms exsist remove the comment and import classes as needed
'''from flaskapp.forms import "form classes" if any '''

# route configuration examples
@app.route('/')
def home():
    return render_template('index.html')
